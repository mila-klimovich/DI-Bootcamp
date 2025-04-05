class AnagramChecker:
    def __init__(self, word_list):
        self.all_words = set()
        with open(word_list, 'r') as f:
            for line in f:
                word = line.strip().lower()
                self.all_words.add(word)

    def is_valid_word(self, word):
        return word.lower() in self.all_words
    
    def is_anagram(self, first_word, second_word):
        return sorted(first_word.lower()) == sorted(second_word.lower())
    
    def get_anagrams(self, word):
        anagrams_list = []
        for a in self.all_words:
            if self.is_anagram(word, a) and a != word.lower():
                anagrams_list.append(a)
        return anagrams_list

