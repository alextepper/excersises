import json

# Part I

class Text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return cls(text)


    def frequency_of_word(self, word):
        list_of_words = self.text.split()
        counter = 0
        previous_word = ""
        for item in list_of_words:
            if word.lower() in previous_word.lower():
                counter += 1
            previous_word = item
        return f"word '{word}' is used {int(counter)} times in the text"

    def most_common_word(self):
        list_of_words = self.text.split()

        dict_of_words = {}
        for word in list_of_words:
            if word in dict_of_words.keys():
                dict_of_words[word] += 1
            else:
                dict_of_words[word] = 1
        max_value = max(dict_of_words, key=dict_of_words.get)
        return f"word '{max_value}' is used {dict_of_words[max_value]} times in the text"

    def get_unique_words(self):
        list_of_words = self.text.split()
        set_of_words = []
        for word in list_of_words:
            if word not in set_of_words:
                set_of_words.append(word)
        return set_of_words


my_text = Text.from_file("the_stranger.txt")
print(my_text.frequency_of_word("you"))
print(my_text.most_common_word())
# print(my_text.get_unique_words())