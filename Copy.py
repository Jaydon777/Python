fin = open(r"F:\Class 12 python files\abbreviations.txt","r")
fout = open(r"F:\Class 12 python files\abbreviationsnew.txt", "w")
for line in fin:
 if 'A' not in line:
     fout.write(line)
print("Contents copied successfully.")
fin.close()
fout.close()
