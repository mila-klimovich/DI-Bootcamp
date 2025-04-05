class Text:
    def __init__(self, string):
        self.string = string
        self.words = self.string.lower().split(' ')
        # print(self.words)

    @classmethod
    def from_file(cls, file):
            with open(file, 'r') as file:
                string = file.read()  
            return cls(string)

    def frequency(self, word):
        count = self.words.count(word)
        if count == 0:
            return None
        return count
    
    def most_common(self):
        word_count = {}

        for word in self.words:
            word_count[word] = word_count.get(word, 0) + 1
        
        words_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        if words_sorted:
            return words_sorted[0][0]
        
        return None
    
    def unique_words(self):
        words = self.string.lower().split() 
        return list(set(words))


# text_string = "A good book would sometimes cost as much as a good house."
# my_text = Text(text_string)
# print(my_text)
# print(my_text.frequency("as"))
# print(my_text.most_common())
# print(my_text.unique_words())

instance = Text.from_file('the_stranger.txt')
print(instance.frequency('of'))  
print(instance.most_common())   
# print(instance.unique_words())