#!/usr/bin/env python
from datetime import timedelta, datetime

def sub30():
    rn = datetime.now()
    newdate = rn - timedelta(days=30)
    print("Date 30 days ago: " , newdate.strftime("%d/%m/%Y"))

if __name__ == "__main__":
    sub30()