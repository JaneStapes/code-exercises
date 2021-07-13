f = open("teams.txt", "r")

lines = list(f)

f.close()

f = open("teams.txt", "w")

lines.insert(0, "this is a newline\n")

liststr = "".join(lines)

f.write(liststr)

for 1 in lines:
    print(1)

    f.close()