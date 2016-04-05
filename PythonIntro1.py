#For python 2.7
#Based on Derek Banas Python in 1 video
#Importing various library modules
import random
import os
import sys

#printing a variable, string, number etc. simply print keyword followed by variable's name
print "hello world"

# a single line comment in python, begins with "#" followed by whatever
#Whatever
#Multiline comment begins and ends with 3 single quotes

'''
a multiline comment
in python
'''

name ="Ulfric Stormcloak"
print name

'''
Five main data types in Python are:
1. Strings 2. Numbers 3. Lists 4. Tuples 5. Dictionaries/Maps
'''

'''
7 different types of operators:
+, -, *, /, %, ** is exponent, // is integer division
'''
print "5%2 =",5%2
print "5**2 =",5**2
print "5//2 =", 5//2

'''
Precedence of Operators
*, / > +, - etc.
'''
#String
quote ="\"Always remember you are awesome!\""
print quote

#Lists are like arrays

topics_to_revise =['OS', 'DBMS', 'Networking']
print "topics to revise:", topics_to_revise[0]

to_code =['sorting', 'searching', 'medians']
to_do = [topics_to_revise, to_code]

print to_do[0][2]
print to_do[1][2]
# Append at the end
topics_to_revise.append('Digital Logic')
print topics_to_revise

#Insert at a particulat index
to_code.insert(3,'graphs')
print to_code
#Similarly we have delete too by remove()
#Other functions are sort() and reverse() for reverse sort
topics_to_revise.sort()
print topics_to_revise

#To find the length of a list, we use len()
print len(to_code)

#TUPLES IN PYTHON
#TUPLES ARE SURROUNDED BY () like a ball
#TUPLES can NOT change
pi_tuple =(3,1,4,1,5,9)
#list(param) can convert tuple to list
new_list =list(pi_tuple)
#tuple(param) can convert a list to tuple
new_tuple =tuple(new_list)
print pi_tuple

#len(p) returns length, min(p) and max(p) return min and max of p

#DICTIONARIES or MAPS
#can NOT join dictionaries like lists
# Dictionaries have key value pair. For each key there is a value

super_heroes ={'Spider-Man': 'Peter Parker',
               'SuperMan' : 'Clark Kent',
               'Batman': 'Bruce Wayne',
               'The Flash': 'Barry Allen'
               }
print super_heroes['Batman']
#Can delete using del followed by map entry
del super_heroes['The Flash']
# We can replace like this:
super_heroes['Batman'] ="Dick Grayson"
print super_heroes['Batman']

#To get dictionary keys use keys(), values() for values, get to get value for a key
print super_heroes.get('Spider-Man')
print super_heroes.keys()
print super_heroes.values()

###############################

#CONDITIONALS IN PYTHON
# if else and elif are used as conditionals
# Both loops and conditionals are followed by a colon :
# Relational operators are <, <=, ==, !=, > and >=

age = 20

if age>=21:
    print "yes, you can drive truck "
elif age>=16:
    print " you can drive car"
else:
    print "You can not drive"

#In python logical operators are 'and', 'or' and 'not'
age = 22
if(age>=16 and age <=21):
    print "You can drive car but not truck"
elif (age >=21):
    print "You can drive anything"
else:
    print "You can not drive yet kiddo"

##################################################

#LOOPS IN PYTHON
#for, while and do while can be used
#range() is inclusive of the first number and exclusive of the second number
for x in range(0,10):
    print x, ' '

#can go through lists too:
for i in topics_to_revise:
    print i

#Going through specific instance/increasing specifically
for y in [1,3,5,7,9,11]:
    print y

#Can use nested for loops to cycle through nested lists

for j in range(0,4):
    for k in range(0,3):
        print to_do[j][k]











