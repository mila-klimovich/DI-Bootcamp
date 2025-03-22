# matrix = '''
# 7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%
# ^r!
# '''

matrix = [
    ["7", "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]


def decrypt_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = ""
    
    for c in range(columns):  
        for r in range(rows):  
            char = matrix[r][c]
            if char.isalpha():
                result += char
            elif len(result) and result[-1] != " ": 
                result += " "

    return result
    
print(decrypt_matrix(matrix))