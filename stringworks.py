from operator import index

str='abcdefghijk'

for char in str:
    print(char)

print(str[:4])
print(str[4:])
print(str[1])

print(str[:4]+str[4:])
print(str.index('abcdefghijk'))
print(str.index('bcdefghijk'))
print(str.index('cdefghijk'))
print(str.index('cdefghijk'))
print(str.index('defghijk'))
print(str.index('efghijk'))
print(str.index('efghijk'))
print(str.index('fghijk'))

#print if there's a substring available in a string
print('str' in 'string')
print('str' in 'dogs')

#changing a substring of a string from "old" to "new"
message='this is an old message'
print(message)
new_message = message[0:9]+' new'+message[14:]
print(new_message)




#writing a function to change the domain of an email
def replace_domain(email, old_domain, new_domain):
    # checking if there's an @ in the string to identify it as an email
  if "@" + old_domain in email:
    #initializing the index for old domain
    index = email.index("@" + old_domain)
    print(index)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

print(replace_domain('bdc@abc.com','abc.com','efg.com'))


#changing the domain of an email based on availability of email and if the domain is old
old='mehedi@gmail.com'
domainold='gmail.com'
domainnew='outlook.com'
newemail=''

print(old)

if '@'+domainold in old:
    indexstring= old.index('@'+domainold)
    newemail=old[:indexstring]+'@'+domainnew
else:
    newemail=old

print(newemail)

#making a string to all uppercase and all lower case
print("mehedi".upper())
print("mehedi".lower())


#setting a condition on string
def functionforCheckingName(name):
    if name.lower() == 'himel' and name.upper() =='HIMEL':
        print('the name is correct')
    else:
        print('the name is incorrent')
functionforCheckingName('Himel')

# spliting a single string to an array of string based on spaces
print('md. mehedi zaman himel'.split())

#join a string of array in a string
print(' '.join(['this','ís', 'á','string','line']))


#string to integar and making a operation
print(int('2345235235')+int('566758567865'))
print(float('2345235235')+int('566758567865'))
print(float('2345235235')+float('566758567865'))

#calculate the lucky number of a name by length multiplication and formatting
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(number, name))
print("Hello {}, your lucky number is {}".format(name, number))


#calculating a tax
def taxcalculate(price):
    with_tax=price*1.09
    print(price, with_tax)
    print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
    print("Base price: ${mainprice}. With Tax: ${tax}".format(mainprice=price, tax=with_tax))

taxcalculate(10)

#writing a function to calculate a weather from given string
def number_to_celcius(x):
    return (x-32)*5/9

for x in range (0,101,10):
    print(x, number_to_celcius(x))


#generating a lucky number from a given name
def generateLuckyNumber(name):
    luckynumber=len(name)*3
    print(f'hi {name}, you lucky number is :{luckynumber}'.format(name=name,luckynumber=luckynumber))

generateLuckyNumber('himel')


def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
  #the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places.

