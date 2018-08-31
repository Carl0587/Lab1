# Carlos Ortega
# Capstone Lab1
# camelCase Program
#08/30/18



#we are asking the user for some input
sentence =(input('Please enter a sentence'))
# I created a variable called word to store the new input and Uppercasing the first letter
word = sentence.title()
#this line will remove any white space in between the words
word = "".join(word.split())
#I jsut printed the variable word
print(word)