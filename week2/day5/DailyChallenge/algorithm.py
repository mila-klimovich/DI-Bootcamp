import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

seen_numbers = set()

pairs = []

for num in list_of_numbers:
    complement = target_number - num
    
    if complement in seen_numbers:
        pairs.append((complement, num))
    
    seen_numbers.add(num)

for pair in pairs:
    print(f"{pair[0]} and {pair[1]} sums to {target_number}")
