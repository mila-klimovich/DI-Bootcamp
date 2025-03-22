# #1
users_input = input("Please enter words separated by commas: ")

sorted_users_input = ",".join(sorted([i for i in users_input.split(",")]))

print(sorted_users_input)

#2
def longest_word(string):
    list_of_words = string.split()
    
    longest = list_of_words[0]
    
    for s in list_of_words:
        if len(s) > len(longest):
            longest = s
    
    return longest

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
