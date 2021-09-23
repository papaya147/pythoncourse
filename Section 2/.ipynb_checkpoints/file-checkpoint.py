with open("data.txt") as f:
    for line in f:
        line = line.strip() # line is always a string unless type casted
        line = int(line)
        print(line * 2)