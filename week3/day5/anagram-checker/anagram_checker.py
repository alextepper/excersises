


class AnagramChecker:
    def __init__(self):
        result = []
        words = open('sowpods.txt')
        for line in words:
            result.append(line.replace("\n", '').lower())
        self.words = result

    def is_valid_word(self, word):
        if word in self.words:
            return True
        else:
            return False

    @staticmethod
    def is_anagram(word1, word2):
        if word1 == word2:
            return False
        elif sorted(word1) == sorted(word2):
            return True
        else:
            return False

    def get_anagrams(self, word):
        list_of_anagrams = []
        for item in self.words:
            if self.is_anagram(word, item):
                list_of_anagrams.append(item)
        return list_of_anagrams
