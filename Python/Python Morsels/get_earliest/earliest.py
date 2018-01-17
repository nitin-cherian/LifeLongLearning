from datetime import datetime

def get_earliest(date1, date2):
    try:
        d1 = datetime.strptime(date1, "%m/%d/%Y") 
        d2 = datetime.strptime(date2, "%m/%d/%Y") 
        return date1 if d1 < d2 else date2
    except ValueError as e:
        return min(date1, date2)