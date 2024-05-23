a= ('Konnichiwa')
print(a.center(40))
print('')
print('')
A=('-------------')
print(A)
print('')
print('')
b = '= difficult + _ ( ( * '
print(len(b)) #len a is a function by which we find length of a string
print(b.upper()) 
print(b.lower())
print(b.rstrip ("+_)(*")) #rstrip removes any word
print(b.replace("difficult" , "very difficult"))
print(b.upper()) ,(b.split(" "))
print('')
print('')
print('-------------')
print('')
print('')
c = ('i am not ImpOSteR')
print(c.capitalize()) #automatically arrange capital wordb
print(A.count('-')) #it counts how many time a word is used
d=('Purple was the imposter.')
print(d.startswith('p'))
print(d.endswith('.'))
print(d.endswith('was', 7, 10))
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
# print(str1.index("ishh"))
# index shows an errorwhen the word is not present
str1 = "hello2everyone"
print(str1.isalnum()) # isalnum contains A-Z, a-z, 0-9 only then it shows true

str1 = "Hellotoeveryone"
print(str1.isalpha()) #isalpha contains A-Z, a-z

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle()) # it will show true when every word's first letter is capital

str2 = "To kill a Mocking bird"
print(str2.istitle()) # false

str3= "You Are No One"
print(str3.swapcase()) #it swop capital letter with smaller

a='earth is flat'
print(a.title()) #it capitalise the first letter of each eord
