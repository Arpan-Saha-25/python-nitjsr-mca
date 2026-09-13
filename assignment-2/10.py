# Q.10) Write a program in Python to enter a sentence and calculate its length including whitespaces and excluding whitespaces. Also count number of words in that sentence.

sentence = input("Enter a sentence: ")

length_with_spaces = len(sentence)

length_without_spaces = len(sentence.replace(" ", ""))

number_of_words = len(sentence.split())

print("Length including whitespaces:", length_with_spaces)
print("Length excluding whitespaces:", length_without_spaces)
print("Number of words:", number_of_words)