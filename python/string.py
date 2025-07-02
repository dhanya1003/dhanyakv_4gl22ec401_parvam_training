name = "Dhanya K V"
print(name)
print(type(name))

# Lower method is used to convert the string to lowercase
print(name.lower())

# Upper method is used to convert the string to uppercase
print(name.upper())

# Title method is used to convert the string to titlecase
print(name.title())

para = "  this is a paragraph with multiple space  "
print(para)

# Strip method is used to remove all the whitespaces from the string
print(para.strip())

# lstrip method is used to remove all the whitespaces from the starting of the string
print(para.lstrip())

# rstrip method is used to remove all the whitespaces from the ending of the string
print(para.rstrip())

name = "Dhanya K V"
# Replace method is used to replace the word from the string
print(name.replace("K V", "Veer"))
# Replecing the original string
print(name.replace("Dhanya", "Nandu"))
print(name)
# But here jist we are printing the repleced string instead of replacing the original of the string
print(name.replace("Dhanya", "K V"))

fruits = "Apple, Mango, Jackfruit, Orange"
print(fruits)
#split method is used to split the string into multiple list item with a seperator
print(fruits.split(", "))
print(type(fruits.split(", ")))

students = "'Akash', 'Vikas', 'Adarsh', 'Guru'"
students = students.split("', ")
print("----------------")
print(students)
print(type(students))
students = str(students)  #typecasted the list to string
print(type(students))
students = students.replace("'","")
print(students)

sentence = "This is a first line. This is a second line. This is a third line"
print(sentence)
sentence = sentence.split(". ")
print(sentence)

#join method is used to combine the multiple list items into single string
print(" ".join(sentence))

#find method is used to get the index of the respective keyword
name = "Dhanya K V"
print(name.find("K V"))
print(name.find("y"))
print(name.find("D"))

#startswith method is used to check whether the given string starts with given value
print(name.startswith("Dhanya"))
print(name.startswith("K"))

#endswith method is used to check whether the given string ends with given value
print(name.endswith("Dhanya"))
print(name.endswith("V"))
print(name.endswith("A"))

word = "ABCD1234"
print(word.isalpha()) #checks whether the given string contains only alphabets
print(word.isnumeric()) #checks whether the given string contains only numbers
print(word.isalnum()) #checks whether the given string contains both alphabets & numbers