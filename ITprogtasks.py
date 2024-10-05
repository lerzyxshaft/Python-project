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
print(cont.items())
print.countries
for key, value in cont.items():
    print(key, "-", value)

