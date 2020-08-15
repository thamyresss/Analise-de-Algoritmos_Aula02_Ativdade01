import csv

n=0
t=0
D=[]
itensDoAquivo=[]

with open("dataset-1-a.csv", "r") as arquivo_csv:
  arquivo = csv.reader(arquivo_csv, delimiter=',')
  
  for i in arquivo:
    itensDoAquivo.append(i)

n = itensDoAquivo[0][0]
t = itensDoAquivo[1][0]
D = itensDoAquivo[2:]


novorquivo = open('saida.txt','a')
for i in D:
  if n in i:
    novorquivo.write("True")
    
  else:
    novorquivo.write("False")
 
novorquivo.close()
    


print('n',n)
print('d',D)
#print(itensDoAquivo)