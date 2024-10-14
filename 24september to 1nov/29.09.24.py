data = [1, 2, 3, 5, 8, True,"Hello world", 6.7, [10, 20]]

data[0] = 50
data[6] = "Have a good day"

print(data)
print([6])

print(data[-1][1])
#Якщо ти хочеш дістати елемент з списку в якому знаходиться  ще один список треба в перших дужках
#викликати через '-' другі дужки і в других дужках вже потрібний нам елемент


numbers = [5, 2, 7]
numbers.append(55)#додає новий елемент в кінець списку
numbers.insert(1, True) #додає новий елемент в будь-яке місце списку
numbers.extend([3, 6, 5]) #дозволяє додати наявні елементи в список ще раз
numbers.sort() #сортує числа в списку
numbers.reverse() #перекручує сортування чисел
numbers.pop() #видаляє останній елемент, в дужках можна вибрати під яким індексом буде видалено елемент
#numbers.remove() #видаляє написаний в дужках елемент
#numbers.clear() #видаляє всі елементи в списку
print(numbers.count(5)) #рахує скільки елементів в списку (елемент котрий буде рахуватись позначений в дужках)
print(len(numbers)) #довжина всього списка (кілкість символів, чисел, слів в ньому)

nums = [3, 6, 7,  "50", False]

for el in nums:
    el *= 2
    print(el)

n = int(input("Enter lenth"))
user_list = []
i = 0
while i < n:
    string = "Enter a number #" + str(i + 1) + ":"
    user_list.append(input(string))
    i += 1
print(user_list)


print(numbers)