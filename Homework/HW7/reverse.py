import sys
finished = False
while finished == False:
    try:
        file = open(sys.argv[1], "r")
        data = [list(line.rstrip("\n")) for line in file]
        finished = True
    except IOError as error:
        print(error)
    finally:
        file.close()

finished = False 
while finished == False:
    try:
        file = open(sys.argv[1], "w")
        for x in range(0, len(data)):
            data[x].reverse()
            data[x].append("\n")
            for char in data[x]:
                file.write(char)
        finished = True
    except IOError as error:
        print(error)
    finally:
        file.close()
print("file has been reversed!")