import datetime
def days_in_month(year, month):
    xval = [1, 3, 5, 7, 8, 10, 12]
    yval = [4, 6, 9, 11]
    if (month in xval):
        return 31
    elif (month in yval):
        return 30
    elif (year % 4 == 0 and month == 2):
        return 29
    elif (year % 4 != 0 and month == 2):
        return 28
    else:
        return 0
        
def is_valid_date(years, months, days):
    if((0 < years < 9999) and (0 < months < 13) and (0 < days < 32)):
        val = days_in_month(years, months)
        xval = [1, 3, 5, 7, 8, 10, 12]
        yval = [4, 6, 9, 11]
        if (val == 31):
            if(months in xval):
                if(1 <= days <= 31):
                    return True
        elif (val == 30):
            if (months in yval):
                if(1 <= days <= 30):
                    return True
        elif (val == 29):
            if (years %4 == 0  and  months == 2):
                if(1 <= days <= 29):
                    return True
        elif (val == 28):
            if (years % 4 != 0  and  months == 2):
                if(1 <= days <= 28):
                    return True 
                else:
                    return False
            
        
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    if(is_valid_date(year1, month1, day1)):
        if(is_valid_date(year2, month2, day2)):
            if(datetime.date(year1, month1, day1) >= datetime.date(year2, month2, day2)):
                return 0
            else:
                date1 = datetime.date(year1, month1, day1)
                date2 = datetime.date(year2, month2, day2)
                finaldate = date1 - date2
                return abs((finaldate.days))
        else:
            return 0
    else:
        return 0  
       
def age_in_days(year2, month2, day2):
    cur = datetime.date.today()
    if((year2 < cur.year) or ((year2 == cur.year) and (month2 < cur.month))):
        if(days_between(year2, month2, day2, cur.year, cur.month, cur.day)):
            return(days_between(year2, month2, day2, cur.year, cur.month, cur.day))
        else:
            return(days_between(cur.year, cur.month, cur.day, year2, month2, day2))   
    elif((year2 == cur.year) and (month2 == cur.month) and (day2 < cur.day)):
        if(days_between(year2, month2, day2, cur.year, cur.month, cur.day)):
            return(days_between(year2, month2, day2, cur.year, cur.month, cur.day))
        else:
            return(days_between(cur.year, cur.month, cur.day, year2, month2, day2))   
    else:
        return 0
    
    
print(age_in_days(2020, 1, 20))
print(is_valid_date(1827, 12, 32))
