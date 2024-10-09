#####03.10.24#####
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem < 5:
        print(elem)
        break

#####04.10.24#####
#tuples lesson
data = (5, 6, 3, 4, True, 3.4, 'Hello')#you also can create tuples without brackets,
# but you need to put ',' after element

# #data[0] = 1 in tuples you can't change anything
#print(data.count(60))
#print(len(data))
print(data[1])

nums = [4, 56, 2, 463,]
new_nums = tuple(nums)
print(new_nums)

word = tuple("hello world")
print(word)

#####05.10.24#####
#DICTIONARIES
countries = {'code': 3, 'numb' : 144 }#you can use '()' inside dict and bulls
print(countries['code'])
cont = dict(code = 'UA', number = '+1', name = 'Ukraine')
print(cont['code'])
print(countries.get("code"))
countries.popitem()
#countries.clear()
print(cont)
countries["3"] = "USA"
print(cont.items())
for key, value in cont.items():
    print(key, "-", value)
print(countries.values())

person = {
    'user_1' : {
        'first_name' : "John",
        'last_name' : "Marley",
        'age' : '45',
        'address' : ["New York", "Washington Street", "32"],
        'marks' : {"math" : 5, "chemistry" : 6}
    },
    'user_2' : {

    }
}
print(person["user_1"]["address"][1])


#####06.10.24#####
#SET FROZENSET
data = {3, 5, 6, 2, 4}
data.update([32, True, 3, 4, 3.4, 'hello'])
data.remove(True)
data.pop()

nums = [3, 2, 2, 3]
new_nums = set(nums)

new_data = frozenset([32, True, 3, 4, 3.4, 'hello', 3, 4321, 34, 345, 35])

print(data)
print(new_data)

#####07.10.24#####
#DEF, LAMBDA
def test_func(word):
    print(word, end = "")
    print("!")


test_func("hello")

#####08.10.24#####
data = {3, 5, 6, 2, 4}
data.update([32, True, 3, 4, 3.4, 'hello'])
data.remove(True)
data.pop()