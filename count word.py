def count_words(input_string):
    
    words = input_string.split()
    
    return len(words)


text = "My age is age?"
word_count = count_words(text)
print(f"The number of words in the string is: {word_count}")
