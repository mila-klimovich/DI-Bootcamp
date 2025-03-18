# 1
word = input("Enter a word: ")
word_dict = {}

for i in range(len(word)):
    if word[i] in word_dict:
        word_dict[word[i]].append(i)
    else:
        word_dict[word[i]] = [i]

print(word_dict)

#2
items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

for key, value in items_purchase.items():
    value = value[1:]
    if "," in value:
        value = value.replace(",", "")
    items_purchase[key] = int(value)

wallet = int(wallet[1:])

can_afford = []

# for key, value in items_purchase.items():
#     if wallet > value:
#         wallet = wallet - value
#         can_afford.append(key)
#         # print(wallet)

can_afford = [key for key, value in items_purchase.items() if wallet > value]

if len(can_afford) > 0: 
    print(sorted(can_afford))
else:
    print("Nothing")
