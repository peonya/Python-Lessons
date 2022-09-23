from datetime import datetime as dt
from time import time
import init

def sum_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}, addition, {}'
                    .format(time,data))

def diff_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}, difference, {}'
                    .format(time,data))

def mult_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}, multiplication, {}'
                    .format(time,data))

def div_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}, division, {}'
                    .format(time,data))