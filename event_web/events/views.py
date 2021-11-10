from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
def home (request, year , month):
    name =  "Stephen"
    month = month.title()
    #convert month from name to number
    month_number =  list(calendar.month_name).index(month)
    month_number = int(month_number) #ensure that calendar number is actually a number

    #creating a calender object
    cal = HTMLCalendar().formatmonth(year,month_number)
    return render(request,'home.html',{
        "name": name,
        "year": year,
        "month": month,
        "month_number":month_number,
        "cal": cal
    })
