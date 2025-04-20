
data = []
for _ in range(5):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    score = input("Enter Score: ")
    data.append((name, age, score))

data_sorted = sorted(data, key=lambda x: (x[0], int(x[1]), int(x[2])))

print(data_sorted)
