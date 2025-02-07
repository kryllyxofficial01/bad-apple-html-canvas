import os

output = open("output.txt", "w")

for file in os.scandir("frames"):
    print(file.name)
    output.write(f"<img src=\"frames/{file.name}\" id=\"{file.name[:-4]}\" style=\"display: none\"/>\n")