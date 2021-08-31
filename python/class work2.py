word = input("Enter a sentence: ").lower()
# count = 0

#for letter in word:
#    if letter in 'aeiou':
#        count += 1

vowel_list = [letter for letter in word if letter in "aeiou"]

print('The number of vowels in {0} is {1}'.format(word, len(vowel_list)))
