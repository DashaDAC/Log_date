import codecs
import pandas as pd
from datetime import datetime as dt

required = "info: Slot to run:"
str12 = []
id = []
time = []
def_time = []
dt_type = '%Y-%m-%d %H:%M:%S.%f '

with codecs.open('Logs/sc_runtime.log') as f:
    for num_line, line in enumerate(f):
        if required in line:
            str12.append(required + line.rpartition("info: Slot to run:")[2])
            id.append(line.rpartition("info: Slot to run:")[2])
            time.append(line.rpartition("info: Slot to run:")[0])

for i in range(len(str12)):

    if i > 0:
        def_time.append(str(dt.strptime(time[i], dt_type) - dt.strptime(time[i-1], dt_type)))
        print(str(str12[i-1] + str12[i])+str(dt.strptime(time[i], dt_type) - dt.strptime(time[i - 1], dt_type)))
    else:
        def_time.append("None")
        print(str("None"))
    print("\n")

id = [line.rstrip() for line in id]

df = pd.DataFrame({'ID': id,
                   'time_def': def_time,})
print(df)




