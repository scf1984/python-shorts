#  1, 11, 21, 1211, 111221
from itertools import groupby
from time import sleep


def look_and_say(number: str):
    while True:
        yield number
        number = ''.join(f'{len([*group])}' + item for item, group in groupby(number))


for x in look_and_say('1'):
    print(x)
    sleep(0.25)
