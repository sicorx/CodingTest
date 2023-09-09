import datetime as dt
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

def solution(date1, date2):
    answer = 0
    
    dt1 = dt.datetime(date1[0], date1[1], date1[2])
    dt2 = dt.datetime(date2[0], date2[1], date2[2])
    
    if dt1 < dt2 :
        answer = 1
    else :
        answer = 0
    return answer