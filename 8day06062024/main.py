def last_word_length(string):
    count = 0
    v1 = len(string)
    words = string.split()

    return words[-1]


store = str(input("Enter a String: \n"))
print(last_word_length(store))
