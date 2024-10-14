#8 python lesson

word = 'shaft, skate, kebab'
print(word[1])

#як результат коду ми отримаємо літеру 's', викликану функцією прінт на екран

print(len(word))
print(word.count('a'))

#ми можемо використовувати для змінної всі ті самі функції які використовуються для списку

print(word.isupper())
print(word.islower())#опускає всі літери рядка
print(word.istitle())#
print(word.lower())#понижує літери
print(word.capitalize())#робить першу літеру рядка великою і понижує всі наступні
print(word.find('a'))#знаходить поставлені в дужки символи з рядку

hobby = word.split(',')#ця функція розділяє рядок на символ зазначений в дужках
print(hobby[1])

for i in  range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ', '.join(hobby)

print(result)


dan = 'Football'

print(dan[4:8])