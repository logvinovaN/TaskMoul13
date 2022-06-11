tiсkets = int(input("Введите количество билетов "))
count = 0
for i in range(tiсkets):
   age = int(input("Введите возраст посетителя "))
   if age < 18:
      count = 0
   elif 18 <= age < 25:
      count += 990
   elif 25 <= age:
      count += 1390
for c in range(tiсkets):
   stoimost = count
   if tiсkets >= 3:
      stoimost *= 0.9
print(stoimost)
