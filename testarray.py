abc=[1,2,3,4,5,6]
print(type(abc))
print('the length is '+ str(len(abc)))
print(abc[0])
print(abc[len(abc)-1])

for i in abc:
    b=i+i
    print(b)
    if(b<8):
        c=b+8
        print(c)

listname=['md','mehedi','zaman']
name='mehedi zaman himel'
print('kkkk'+name)
print(listname[0])
print(listname[1])
print(listname[2])
name.split('@')
print(name)

#initializing a list
fruits=['pineapple', 'banana', 'apple','melon','kiwi']
print(fruits)

#inserting into the list
fruits.insert(0,'órange')
fruits.insert(25,'grapes')
print(fruits)

#deleting particular content from list by value
fruits.remove('banana')
print(fruits)

#removing last index content from list
fruits.pop(0)
print(fruits)

#changing the value of existing by index
fruits[0]='ábra ka dabra'
print(fruits)