fr = open("C:/Users/annak/Desktop/SKOLA/11.2/11.2/meteo_stanice.txt", "r", encoding="utf-8")
fw = open("C:/Users/annak/Desktop/SKOLA/11.2/11.2/meteo_stanice_vysledky.txt", "w", encoding="utf-8")
counter = 0 #1.
maxtemp = -1000 #3.
temperatures = list() #2.
station = '' #4.
for row in fr:
    proc_line = row.strip().split(' ')              #1.
    temperatures.append(float(proc_line[3].replace(',','.')))#2.
    temp = float(proc_line[3].replace(',','.')) #2.
    if temp > maxtemp: #3.
        station = proc_line[0] #4.
        maxtemp = temp #3.
    print(proc_line) #1.
    counter += 1 #1.
print(f'Pocet merani je: {counter}')#1.
fw.write(f'Pocet merani je: {counter}\n') #1. zapis do suboru
print(f'Teploty su:{temperatures}')#2.
fw.write(f'Teploty su:{temperatures}\n') #2. zapis do suboru
print(f'Nejzssia teplota je: {max(temperatures)}') #3.
fw.write(f'Nejzssia teplota je: {max(temperatures)}\n') #3. zapis do suboru
#print(f'Nejvyssia teplota je: {maxtemp}') #3. rucne
print(f'Priemerna teplota je: {round(sum(temperatures)/len(temperatures), 2)}') #5.
fw.write(f'Priemerna teplota je: {round(sum(temperatures)/len(temperatures), 2)}\n') #5. zapis do suboru
fw.close()