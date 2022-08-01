import codecs

required = "grabber : ntc reply = NTC,0000,0370,"

comp_number = int(input("Enter a number to compare: "))

with codecs.open('Logs/sc_device.log') as f:
    for num_line, line in enumerate(f):
        if required in line:
            number = int(line.rpartition('grabber : ntc reply = NTC,0000,0370,')[2])
            if number>=comp_number:
                print("OK :", number, ">=", comp_number, " : string ", num_line)
            else:
                print("ERR :", number, "<", comp_number, " : string ", num_line)





