import codecs

string_numbers = []
str_test = []
rep = []
arr_inx = []
col_work = 0
col_work2 = 0
required = "Worklist name"

with codecs.open('Logs/200731.LOG', encoding='utf-16', errors='ignore') as f:
    for num_line, line in enumerate(f):
        if required in line:
            string_numbers.append(num_line)
            str_test.append(line.rpartition('Worklist name')[2])
    list_test = set(str_test)
    for x in list_test:
        if (str_test.count(x) > 1):
            inx = [i for i, list_test in enumerate(str_test) if list_test == x]
            rep.append((x, inx))
            arr_inx.append(inx)
set1 = set()
set2 = set()

#1_1

with codecs.open('Logs/200731.LOG', encoding='utf-16', errors='ignore') as f:
    f_list = f.readlines()
    flag = 0
    for i in range(int(string_numbers[-1]), -1, -1):
        if "CYCLE complete" in f_list[i]:
            iden = f_list[i].split("CYCLE complete")
            if iden[-1] is None:
                flag = 1
                print("пустой индетификатор в строке: ", i)
    if flag == 0:
        print("Нет пустых идентификаторов")

#1_2


with codecs.open('Logs/200731.LOG', encoding='utf-16', errors='ignore') as f:
    f_list = f.readlines()
    for j in range(int(string_numbers[0]), int(string_numbers[-1])):
        if "CYCLE complete" in f_list[j]:
            col_work = col_work+1
    for k in range(len(arr_inx)):
        for l in range(2):
            arr_inx[k][l] = string_numbers[arr_inx[k][l]]
        set2 = list(range(arr_inx[k][0], arr_inx[k][1]))
        set1 = set1.union(set2)
    print("Number of CYCLE complete <iden> between the first 'Worklist name' and last 'Worklist name':", col_work)
    for m in set1:
        if "CYCLE complete" in f_list[m]:
            col_work2 = col_work2+1
    print("Number of CYCLE complete <iden> between the 'Worklist name' with the same filenames :", col_work2)



