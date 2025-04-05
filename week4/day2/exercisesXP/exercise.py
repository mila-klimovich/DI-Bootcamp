import random
#1
def get_words_from_file():
    with open("sowpods.txt", "r") as f:
        words = [word.strip() for word in f]

    return words

# words = get_words_from_file()

# for i in range(5):
#     print(repr(words[i]))

def get_random_sentence(length):
    words = get_words_from_file()
    random_words = random.sample(words, length)
    random_sentence = " ".join(random_words).lower()

    return random_sentence

# print(get_random_sentence(5))

def main():
    print("This program is a random sentence generator.")
    input_length = input("How long do you want this sentence to be? Enter a number from 2 to 20: ")
    
    try:
        length = int(input_length)
    except ValueError:
        print("Please enter a number from 2 to 20")
        return
       
    if length > 20 or length < 2:
        print("Please enter a number from 2 to 20")
        return

    sentence = get_random_sentence(length)

    return sentence

result = main()
print(result)


#2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# print(sampleJson)
sample_py = json.loads(sampleJson)
print(sample_py)

salary = sample_py["company"]["employee"]["payable"]["salary"]
print(salary)

sample_py["company"]["employee"]["birth_date"] = "1989-10-28"

with open("info.json", "w") as file_obj:
    json.dump(sample_py, file_obj, indent=2, sort_keys=True)