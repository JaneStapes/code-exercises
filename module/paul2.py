f = open(Wteams.txt", "x")

teams = ["Wanborough", "Eldene", "Nythe", "Liden", "Dorcan"]

for n in range(1,6):
    newline = "This is line" + "for the team of " + teams[n-1] + "\n"
    f.write(newline)

f.close()

f = open("teams.txt", "r")
lines = list(f)

print("line 1 contents: " + lines[0])
print("line 4 contents: " + lines[3]

f.close()