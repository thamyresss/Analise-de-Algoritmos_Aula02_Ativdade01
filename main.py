import csv
import time

n=0
t=0
D=[]
itensDoAquivo=[]

with open("dataset-1-a.csv", "r") as arquivo_csv:
  arquivo = csv.reader(arquivo_csv, delimiter=',')
  
  for i in arquivo:
    itensDoAquivo.append(i)

n = itensDoAquivo[0]
t = int(itensDoAquivo[1][0])
D = itensDoAquivo[2:]


novoarquivo = open('saida-a.txt','a')
start = time.time()
for i in range (t):
  
  if D[i] == n:    
    novoarquivo.write("True" + '\n')
    novoarquivo.write(str(i) + '\n')
    
  else:
    novoarquivo.write("False" + '\n')
    novoarquivo.write("-1" + '\n')
    
novoarquivo.write(str(time.time() * 1000 - start))
novoarquivo.close()

