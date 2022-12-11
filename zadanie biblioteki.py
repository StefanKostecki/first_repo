path = 'C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik:
    content = plik.readlines()

# print(content)
for i in range (len(content)):
#    print(content[i])
    content[i] = content[i].split(',')
    # print(content[i])
# print(content)
# print(content[2][2])

#obliczenie sredniej wyplaty


total = 0
for i in range (1,len(content)):
    # print(content[i][0])
    total = total + int(content[i][0])
print('Suma wynagrodzen: ', total)
average = total / (len(content)-1)
print('Srednie wynagrodzenie: ', round(average,2))

#ile kobiet na macieżyńskim
total = 0
for i in range (1,len(content)):
    # print(content[i])
    content[i][4] = content[i][4].replace('\n', '')
    if content[i][4] == 't' and content[i][3] == 'k':
        total += 1
print('Ilosc kobiet na maciezynskim: ', total)
