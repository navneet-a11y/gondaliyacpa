"""Family 14 date module.

6(c) names the unique data source for this family as a "Server-side date module,
Ontario statutory holiday table maintained by Navneet". This is that module.

T2 due date rule, per the plan's copy-paste block: a return is due within six
months of the fiscal year-end. Where the year-end is the last day of a month,
the due date is the last day of the sixth month after. The plan's own exemplar
confirms it: a December 31 year-end makes the T2 due June 30.

The Ontario statutory holiday table is Navneet's to maintain. The dates here are
computed from the standard Ontario rules rather than hardcoded per year, but they
are not a substitute for his verified table: CRA's own list of recognised public
holidays governs whether a filing lands on time, and Navneet signs that off.
"""
from datetime import date, timedelta
import calendar

MONTHS = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

def last_day(year, month):
    return calendar.monthrange(year, month)[1]

def due_date(ye_year, ye_month):
    """Concrete due date for a last-day-of-month year-end."""
    m = (ye_month + 6 - 1) % 12 + 1
    y = ye_year + (1 if ye_month + 6 > 12 else 0)
    return date(y, m, last_day(y, m))

def due_month_name(ye_month):
    return MONTHS[((ye_month + 6 - 1) % 12)]

def nth_weekday(year, month, weekday, n):
    d = date(year, month, 1)
    d += timedelta(days=(weekday - d.weekday()) % 7)
    return d + timedelta(weeks=n - 1)

def easter(year):
    a=year%19; b=year//100; c=year%100; d=b//4; e=b%4; f=(b+8)//25
    g=(b-f+1)//3; h=(19*a+b-d-g+15)%30; i=c//4; k=c%4
    l=(32+2*e+2*i-h-k)%7; m=(a+11*h+22*l)//451
    month=(h+l-7*m+114)//31; day=((h+l-7*m+114)%31)+1
    return date(year, month, day)

def ontario_holidays(year):
    """Ontario statutory holidays. Navneet verifies this table against CRA's
    recognised list before any deadline page publishes."""
    return {
        "New Year's Day": date(year,1,1),
        'Family Day': nth_weekday(year,2,0,3),
        'Good Friday': easter(year) - timedelta(days=2),
        'Victoria Day': max(d for d in (date(year,5,x) for x in range(18,25)) if d.weekday()==0),
        'Canada Day': date(year,7,1),
        'Labour Day': nth_weekday(year,9,0,1),
        'Thanksgiving': nth_weekday(year,10,0,2),
        'Christmas Day': date(year,12,25),
        'Boxing Day': date(year,12,26),
    }

def is_business_day(d, holidays=None):
    if d.weekday() >= 5: return False
    hol = holidays if holidays is not None else set(ontario_holidays(d.year).values())
    return d not in hol

def next_business_day(d):
    hol = set(ontario_holidays(d.year).values()) | set(ontario_holidays(d.year+1).values())
    while not is_business_day(d, hol):
        d += timedelta(days=1)
    return d

if __name__ == '__main__':
    print('Year-end -> T2 due date, worked for 2026 year-ends')
    for m in range(1,13):
        ye = date(2026, m, last_day(2026,m))
        dd = due_date(2026, m)
        nbd = next_business_day(dd)
        note = '' if nbd == dd else f'   falls on a {dd.strftime("%A")}, so next business day is {nbd.strftime("%B %d")}'
        print(f'  {ye.strftime("%B %d"):14s} ->  {dd.strftime("%B %d, %Y"):20s}{note}')
    print()
    print('Ontario statutory holidays 2027, for the table Navneet verifies:')
    for n,d in sorted(ontario_holidays(2027).items(), key=lambda x:x[1]):
        print(f'  {d.strftime("%Y-%m-%d")}  {n}')
