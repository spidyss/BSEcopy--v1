from io import BytesIO
from zipfile import ZipFile
import requests
from datetime import datetime
from api.db import get_redis_connection
import json
import csv
import logging

def get_date_suffix_string(dt):
    return dt.strftime('%d') + dt.strftime('%m') + dt.strftime('%y')

def download_file(date):
    url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ{}_CSV.ZIP".format(date)

    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if resp.status_code!=200:
        return  None

    return resp.content

def store_to_redis(content):
    zipfile = ZipFile(BytesIO(content))
    file = zipfile.namelist()[0]

    db = get_redis_connection()

    with zipfile.open(file, "r") as csvfile:
        headers = csvfile.readline()
        print (headers)
        for line in csvfile.readlines():
            row = [r.strip() for r in line.decode('utf-8').split(",")]
            data = {
                'code':row[0],
                'name':row[1],
                'group':row[2],
                'type':row[3],
                'open':row[4],
                'high':row[5],
                'low':row[6],
                'close':row[7],
                'last':row[8],
                'prevclose':row[9],
                'no_trades':row[10],
                'no_of_shares':row[11],
                'net_turnover':row[12],
                'tdcloindi':row[13]
            }
            db.set(data['name'],data)

def download_daily_bhavcopy():
    dt = datetime.now()
    date = get_date_suffix_string(dt)

    content = download_file(date)
    if not content:
        return
    try:
        store_to_redis(content)
    except Exception as e:
        logging.exception(e.message)


if __name__=="__main__":
    download_daily_bhavcopy()