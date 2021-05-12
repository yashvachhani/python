message = "Hello World"

three_quots = 'what\'s up'

multi_line_string = """hii this is test of multiline string
and it worked well 
also try comma "in to "" the string"""

print(message)

print(three_quots)

print(multi_line_string)

# returning lanth of string
print(len(multi_line_string))

#use sub string by index
print(multi_line_string[8:20])

#use sub string starting form first character to midway
print(multi_line_string[:16])

#use sub string starting form midway till end
print(multi_line_string[81:])

#print lowercase
print(message.lower())

#print uppercase
print(message.upper())

#count surtain number of character in to the string
print(multi_line_string.count("string"))
print(multi_line_string.count("i"))

#replace some caracter
new_message = message.replace("World","universe")
print(new_message)

#concatinte string
name = "Yash"
greeting = "Hello"
print( greeting + ', ' + name + ". Welcome")

#using place order
print("{}, {}. Welcome!".format(greeting,name))

# f string
print(f"{greeting}, {name.upper()}. Welcome!")

# show all pre defined methods
print(dir(name))

#run help on class of purticuler datatype
#print(help(str))
print(help(str.lower))