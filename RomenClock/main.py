import time
from time import gmtime, strftime
import asyncio

DIR_ARAB_RIM = {
    0: "",
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    20: "XX",
    30: "XXX",
    40: "XL",
    50: "L",
    60: "LX",
    70: "LXX",
    80: "LXXX",
    90: "XC",
    100: "C",
    200: "CC",
    300: "CCC",
    400: "CD",
    500: "D",
    600: "DC",
    700: "DCC",
    800: "DCCC",
    900: "CM",
    1000: "M",
    2000: "MM",
    3000: "MMM"

}

def convert(num_arab): #'1234'
    if num_arab.isdigit():
        if num_arab == "00":
            return 'N'
        else:
            num_rim = ''
            digit = 1
            for i in num_arab[::-1]:
                num_rim = DIR_ARAB_RIM[int(i)*digit] + num_rim
                digit *= 10
            return num_rim
    else:
        return 'Error'

async def arab_to_rim():
    time_and_date = strftime('%H:%M:%S %d.%m.%Y', gmtime())
    hours = time_and_date[0:2]
    hours = int(hours) + 3
    hours = '0' + str(hours)

    rim_hours = convert(hours)
    rim_minutes = convert(time_and_date[3:5])
    rim_seconds = convert(time_and_date[6:8])
    rim_day = convert(time_and_date[9:11])
    rim_month = convert(time_and_date[12:14])
    rim_year = convert(time_and_date[15:])
    my_time = 'Time: ' + rim_hours + ':' + rim_minutes + ':' + rim_seconds
    my_date = 'Date: ' + rim_day + '.' + rim_month + '.' + rim_year + ';'
    print(my_time + ';' + (23 - len(my_time))*' ' + " || " + my_date)
    return my_time + ';' + (23 - len(my_time))*' ' + " || " + my_date

async def sleep_second():
    time.sleep(1)

async def main():
    while True:
        t1 = asyncio.create_task(arab_to_rim())
        t2 = asyncio.create_task(sleep_second())
        await t1
        await t2

if __name__ == '__main__':
    asyncio.run(main())