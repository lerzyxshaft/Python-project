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