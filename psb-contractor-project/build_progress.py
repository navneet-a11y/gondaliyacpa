"""Build the PSB project progress workbook (tasks + rate-correction pages)."""
import csv, json, sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

live = set(open(sys.argv[1]).read().split())
out = sys.argv[2]
F = Font(name="Arial", size=10); B = Font(name="Arial", size=10, bold=True)
H = Font(name="Arial", size=10, bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="0F2A4A")
FILL = {"Done": "D9F2E3", "Partly done": "FFF4D6", "Pending": "FDE2E1", "Waiting on Sharad": "E8EEF8", "Upcoming": "F2F2F2", "Check": "FFF4D6"}
S = Side(style="thin", color="9AA5B1"); G = Border(left=S, right=S, top=S, bottom=S); W = Alignment(wrap_text=True, vertical="top")

def table(ws, hdr, rows, widths, state_col=None):
    ws.append(hdr)
    for r in rows: ws.append(r)
    for c in range(1, len(hdr) + 1):
        ws.column_dimensions[get_column_letter(c)].width = widths[c - 1]
        x = ws.cell(1, c); x.font, x.fill, x.alignment, x.border = H, HF, W, G
    for r in range(2, len(rows) + 2):
        for c in range(1, len(hdr) + 1):
            x = ws.cell(r, c); x.font, x.alignment, x.border = F, W, G
        if state_col:
            v = ws.cell(r, state_col).value
            if v in FILL: ws.cell(r, state_col).fill = PatternFill("solid", fgColor=FILL[v])
    ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions

# Tasks, with state as of Nov 9 (live checks where possible)
STATE = {
 "1": ("Pending", "Not visible from the website; Navneet to confirm"),
 "2": ("Pending", "Not visible from the website; Navneet to confirm"),
 "3": ("Done", ""),
 "4": ("Partly done", "21 of 23 live; rows 22-23 now fixed on the site (checked Nov 9). Row 17 (team page postal code, Elementor) not confirmed"),
 "5": ("Done", "Oct 12"),
 "6": ("Pending", "Checked Nov 9: page 1 still has no Rank Math title, description, focus keyword or pillar setting"),
 "7": ("Done", ""), "8": ("Done", "Per Navneet"), "9": ("Done", "Oct 13"),
 "10": ("Done", "Oct 15 (1 day late)"),
 "11": ("Partly done", "Checked Nov 9: 301 redirect is live (created Nov 9). Old page 53131 is still published: move it to draft"),
 "12": ("Pending", "Navneet to confirm"), "13": ("Pending", "Navneet to confirm"),
 "14": ("Done", ""), "15": ("Done", "Oct 20 images attached"),
 "16": ("Partly done", "Posts live Oct 15; GSC, llms.txt and links not confirmed"),
 "17": ("Pending", "Navneet to confirm"),
 "18": ("Done", "Posts 6-10 published after go-ahead"),
 "19": ("Partly done", "Posts live; GSC, llms.txt and links not confirmed"),
 "20": ("Pending", "Navneet to confirm"), "21": ("Pending", "Navneet to confirm"),
 "22": ("Pending", "Not done; I can run it"), "23": ("Pending", ""), "24": ("Waiting on Sharad", ""),
 "25": ("Partly done", "Batches 1-2 (100 URLs) sent Oct 23. Batches 3+ not prepared yet"),
 "26": ("Partly done", "Checked Nov 9: 83 of 85 batch 1-2 pages that needed changes no longer show 12.2% as current. 4 to check (see Rate correction tab)"),
 "27": ("Upcoming", "Due Nov 19"), "28": ("Upcoming", "Due Dec 18"),
}
rows = []
for r in csv.DictReader(open("TASKS.csv")):
    st, note = STATE.get(r["#"], ("Pending", ""))
    rows.append([int(r["#"]), r["Task"], r["Count"], r["Owner"], r["Start"], r["Due"], st, note])
wb = Workbook(); ws = wb.active; ws.title = "Tasks"
table(ws, ["#", "Task", "Count", "Owner", "Start", "Due", "State (Nov 9)", "Notes"], rows, [5, 48, 26, 10, 11, 11, 16, 60], 7)
n = len(rows) + 3
ws.cell(n, 2, "Summary").font = B
for i, s in enumerate(["Done", "Partly done", "Pending", "Waiting on Sharad", "Upcoming"]):
    ws.cell(n + 1 + i, 2, s).font = F
    ws.cell(n + 1 + i, 3, f'=COUNTIF($G$2:$G${len(rows)+1},B{n+1+i})').font = F

# Rate-correction pages
rc = []
for b, label in (("rate-correction/batch-01", "Batch 1"), ("rate-correction/batch-02", "Batch 2")):
    for line in open(f"{b}-ids.txt"):
        i, slug = line.split()
        d = json.load(open(f"{b}/{i}.json"))
        need = sum(r["rule"] != "R3" for r in d["rows"])
        if need == 0: st, note = "Done", "Nothing to change (historical mentions only)"
        elif i not in live: st, note = "Done", "No longer shows 12.2% as current (checked Nov 9)"
        else: st, note = "Check", "Still mentions 12.2%. Built in Elementor or has historical mentions: open the page to confirm the change was made"
        rc.append([label, int(i), "https://gondaliyacpa.ca/" + slug + "/", need, st, note])
row23 = {"56870":"accountant-for-private-investigators","56869":"accountant-for-security-guard-companies","56871":"accountant-for-security-companies","56872":"accountant-for-lash-and-brow-studios","56803":"accountant-for-software-resellers","56798":"accountant-for-no-code-development-agencies","56807":"accountant-for-product-design-studios","56799":"accountant-for-denturists","56800":"accountant-for-businesses-winding-down","54831":"accountant-for-cloud-service-providers","54824":"accountant-for-data-analytics-companies","54823":"accountant-for-cybersecurity-companies","54828":"accountant-for-managed-service-providers","54734":"accountant-for-medical-device-distributors","54731":"accountant-for-sleep-clinics","54736":"accountant-for-fertility-clinics","54334":"accountant-for-second-generation-family-businesses"}
for i, s in row23.items():
    rc.append(["Row 23", int(i), f"https://gondaliyacpa.ca/{s}/", "", "Done" if i not in live else "Check", "No longer shows 12.2% (checked Nov 9)" if i not in live else ""])
ws2 = wb.create_sheet("Rate correction")
table(ws2, ["Batch", "Page ID", "URL", "Changes proposed", "State (Nov 9)", "Notes"], rc, [9, 9, 62, 10, 14, 60], 5)

# Not yet reviewed
reviewed = {str(r[1]) for r in rc} | {"57063","57084","57086","57087","57083","57085","57088","57089","57094","57096","57095","57097","57099","57098","57100","57102","57104","57101","57103","57105","48088","49284","49693","25185","54117","54086"}
todo = sorted((i for i in live if i not in reviewed), key=int, reverse=True)
ws3 = wb.create_sheet("Not yet reviewed")
table(ws3, ["#", "Page ID", "Edit link", "State"], [[k + 1, int(i), f"https://gondaliyacpa.ca/?p={i}", "Pending"] for k, i in enumerate(todo)], [5, 9, 40, 12], 4)
wb.save(out)
print(len(rows), "tasks;", len(rc), "rate pages;", len(todo), "not yet reviewed")
