import codecs

board = ["grabber", "wash", "tip", "reagents"]
val_board = int(input("Input namber of BOARD (grabber - 0, wash - 1, tip - 2, reagents - 3) :"))
required = "info: " + str(board[val_board]) + " : Sending command: "
required2 = "info: " + str(board[val_board]) + " : Got reply: "

ID = []
str_a = []


with codecs.open('Logs/sc_device_v.log') as f:
    for num_line, line in enumerate(f):
        if required in line:
            sub_line = line.rpartition("info: " + str(board[val_board]) + " : Sending command:")[2]
            ID = sub_line.split()[0]
            str_a.append(required + str(ID))
        if required2 in line:
            sub_line = line.rpartition("info: " + str(board[val_board]) + " : Got reply: ")[2]
            ID = sub_line.split()[0]
            str_a.append(required2 + str(ID))


for i in range(len(str_a)):
    if required in str_a[i]:
        sub_line1 = str_a[i].rpartition("info: " + str(board[val_board]) + " : Sending command: ")[2]
        ID1 = sub_line1.split()[0]
        for j in range((i+1), len(str_a)):
            if required2 in str_a[j]:
                sub_line2 = str_a[j].rpartition("info: " + str(board[val_board]) + " : Got reply: ")[2]
                ID2 = sub_line2.split()[0]
                if (int(ID2) == (int(ID1) + 1)):
                    print(str_a[i] + "\n" +str_a[j]  + "\n")
                    break

            else:
                continue

