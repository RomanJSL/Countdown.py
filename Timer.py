# Code writen by Roman J.S. Lewandowski 27/08/20

import json
import time

localtime = time.localtime(time.time())

print(localtime)

def countdown(targettime):
    years = targettime[0] - time.localtime(time.time())[0]
    months = targettime[1] - time.localtime(time.time())[1]
    days = targettime[2] - time.localtime(time.time())[2]
    hours = targettime[3] - time.localtime(time.time())[3]
    minutes = targettime[4] - time.localtime(time.time())[4]
    tuple = [years,months,days,hours,minutes]
    return tuple