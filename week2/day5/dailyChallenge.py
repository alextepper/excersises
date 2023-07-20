# Challenge 1 : Sorting
out_string = input("please input your words separated by comma: ")


def words_sorting(string):
    words = []
    word = ""
    for char in string:
        if char != ",":
            word += char
        else:
            words.append(word)
            word = ""
    words.append(word)
    words.sort()
    result = ''
    for item in words:
        result += item + ","
    print(result)


# words_sorting(out_string)

# Challenge 2 : Longest Word
new_string = input("please insert your sentence: ")


def long_word_searcher(string):
    words = []
    word = ""
    for char in string:
        if char != " ":
            word += char
        else:
            words.append(word)
            word = ""
    words.append(word)
    sorted_words = sorted(words, key=len)
    return sorted_words[-1]

print(long_word_searcher(new_string))

