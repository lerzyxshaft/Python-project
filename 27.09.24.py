#6 27.09.24 py lesson
data = input()
number = 8 if data == 8 or 9 else 0
print()

password = input("Print your password")
for i in password:
    if i == 1345:
        print("You was logged in!")
    else :
        break

count = 0
word = "Hello world"
for i in word:
    if i == "l":
        count +=1

print("Count", count)

i = 5
while i <= 15:
    print(i)
    i +=2

isHisCar = True
while isHisCar:
    question = input("Just print magic word!")
    if question == "stop":
        isHisCar = False
        print("here you go!")
        break
    else :
        print(question)

for i in range(1, 11):
    if i == 5:
        break

    if i % 2 == 0:
        continue

    print(i)

found = None
for i in "hello":
    if i == "l":
        found = True
        break
    else :
        found = False
print(found)