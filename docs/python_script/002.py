#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import datetime


def get_time():
    x = datetime.datetime.now()
    return x
def get_day():
    day = get_time()
    return day.strftime("%a")
def get_month():
    month = get_time()
    return month.strftime("%B")
def get_month_no():
    month = get_time()
    return month.strftime("%m")
def get_date():
    date = get_time()
    return date.strftime("%d")
def get_year():
    year = get_time()
    return year.strftime("%Y")


file_name = get_date() + "-" + get_month_no() + "-" + get_year() + ".html"


def get_table():
    url = "https://www.mohfw.gov.in/"
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html5lib')
    data = soup.find('div', attrs={'class': 'data-table table-responsive'})
    return data

def get_html(p_href, n_href, name):
    n1 = 'refer_previous'
    n2 = 'refer_next'
    n3 = 'day_month_dd_yyyy'
    with open("111.html", "rt") as fin:
        with open(file_name, "wt") as fout:
            for line in fin:
                if n1 in line:
                    fout.write(line.replace(n1, p_href))
                elif n2 in line:
                    fout.write(line.replace(n2, n_href))
                elif n3 in line:
                    fout.write(line.replace(n3, name))
                else:
                    fout.write(line)



date =get_date()
date = int(date)
date -= 1
date = str(date)
p_href = date + "-" + get_month_no() + "-" + get_year()
date = get_date()
date = int(date)
date += 1
date = str(date)
n_href = date+ "-" + get_month_no() + "-" + get_year()
name = get_day() + "\t" + get_month() + "\t" + get_date() + "\t" + get_year()

get_html(p_href, n_href, name)

with open(file_name, "a") as fedit:
    string = "</body> </html>"
    fedit.write(str(get_table()))
    fedit.write(string)
with open(file_name,"rt") as html:
    with open("today.html","wt") as today:
        for line in html:
            today.write(line)
