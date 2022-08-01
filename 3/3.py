import codecs

board = ["grabber", "wash", "tip", "reagents"]
val_board = int(input("Input namber of BOARD (grabber - 0, wash - 1, tip - 2, reagents - 3) :"))
required = "info: " + str(board[val_board]) + " : Sending command: "
required2 = "info: " + str(board[val_board]) + " : Got reply: "

ID = []
str_1 = []
str_2 = []
number_first = []
str_a = []


with codecs.open('Logs/sc_device_v.log') as f:
    for num_line, line in enumerate(f):
        if required in line:
            sub_line = line.rpartition("info: " + str(board[val_board]) + " : Sending command:")[2]
            ID = sub_line.split()[0]
            str_1.append(required + str(ID))
            str_a.append(required + str(ID))
        if required2 in line:
            sub_line = line.rpartition("info: " + str(board[val_board]) + " : Got reply: ")[2]
            ID = sub_line.split()[0]
            str_a.append(required2 + str(ID))
str_2 = list(set(str_1))
# print(str_2)
for i in range(len(str_2)):
    number_first.append(str_a.index(str_2[i]))
    # print("number ", str_a.index(str_2[i]))
# print(number_first)
# print(len(number_first))
# print(len(str_2))
for i in range(len(str_2)):
    sub_line1 = str_2[i].rpartition("info: " + str(board[val_board]) + " : Sending command: ")[2]
    ID1 = sub_line1.split()[0]
    for k in range((number_first[i]+1), len(str_a)):
        if required2 in str_a[k]:
            sub_line2 = str_a[k].rpartition("info: " + str(board[val_board]) + " : Got reply: ")[2]
            ID2 = sub_line2.split()[0]
            if (int(ID2) == (int(ID1) + 1)):
                print(str_2[i] + "\n" +str_a[k]  + "\n")
                break

