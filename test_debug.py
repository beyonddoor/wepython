from icecream import ic 

from datetime import datetime
from icecream import ic 
import time
from datetime import datetime

def time_format():
    return f'{datetime.now()}|> '

# ic.configureOutput(includeContext=True)
ic.configureOutput(prefix=time_format)

for _ in range(3):
    time.sleep(1)
    ic('Hello')

def hello(user:bool):
    if user:
        print("I'm user")
    else:
        print("I'm not user")

hello(user=True)

def hello(user:bool):
    if user:
        ic()
    else:
        ic()

hello(user=True)

def plus_five(num):
    return num + 5

ic(plus_five(4))
ic(plus_five(5))
