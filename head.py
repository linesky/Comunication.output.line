print("\x1bc\x1b[47;34m")
filename = input("text file: ")

# Lê o arquivo de texto
f1=open("output.txt","w")
ff=""
for a in range(95):
    ff=ff+str(chr(85))
ff=ff+str(chr(0))
f1.write(ff)
with open(filename, 'r') as f:
    text = f.read()
    f1.write(text)

f1.close()