file = open("ReadWrite.txt", "w")
newline = "Manchester United" + "\n"
file.write(newline)
newline = "Manchester City" + "\n"
file.write(newline)
newline = "Nigerian National Team" + "\n"
file.write(newline)
newline = "Los Angeles Lakers" + "\n"
file.write(newline)
newline = "Los Angeles Clippers" + "\n"
file.write(newline)

file = open("ReadWrite.txt", "r")
print("First Team: " + file.readline())
print("Second Team: " + file.readline())

file.close()


