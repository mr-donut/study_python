import re
wordfind=(input('ввести слово'))
def count_letters(wordfind):
    return len(wordfind)

text = open('гениальное решение.txt', 'r'):
    line_splitted = line.split()
    for x in line_splitted:
        word = x.lower()
        for y in r',.():;?!"/#1234567890':
            word = word.replace(y, '')
            word1 ={word}

#        print(word)
        print(len(word1))
        print (word1)
for i in range(len(word)):
    if count_letters(wordfind) == len(word[i]):
        print(word[i])
        #            for i in range(len(word)):
#                if count_letters(wordfind) == len(word[i]):
#                    print(len(word))
#                    print(word[i])









#print(word[i])
#my_list = (full_text.read()).split(' ')
#unnecessary_letter = '",.():;?!"'
#return len([letter for letter in word if letter not in unnecessary_letter])