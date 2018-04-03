sentence = raw_input("provide user input")
words = sentence.split()
average = sum(len(word) for word in words) / len(words)
print average
