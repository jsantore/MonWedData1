import string
#cpoied from slide 29 of the dictionaries slides = removes puctuation
translator = str.maketrans('', '', string.punctuation)
word_counts = {} #currently empty dictionary to hold word counts
with open("warpeace.txt", 'r', encoding='utf-8') as file:
    all_lines = file.readlines()
    for current_line in all_lines: # go through every time
        words_in_line = current_line.split(' ') #break line into words
        for word in words_in_line: # go through every word in the line
            bare_word = word.translate(translator) #remove punctuation
            bare_word = bare_word.lower()
            bare_word = bare_word.strip()
            if bare_word in word_counts:
                word_counts[bare_word] += 1
            else:
                word_counts[bare_word] = 1
for word,count in word_counts.items():
    print(f'{word}: \t{count}'"")