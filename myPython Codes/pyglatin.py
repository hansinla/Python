pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first=word[0]
    if ('aeiou'.find(first) == -1):
    	new_word=word[1:len(word)]+word[0:1]+pyg
    	print(new_word)
    else:
    	new_word=word+pyg
    	print(new_word)
else:
    print('empty')
