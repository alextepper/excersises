matrix = [
    ["7", "i", 'i'],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

def decrypt_the_matrix(matrix):
    string_matrix = []

    for a in range(0, 3):
        for i in range(0, len(matrix)):
            string_matrix.append(matrix[i][a])

    decrypted_matrix = ""

    for item in string_matrix:
        if item.isalpha():
            decrypted_matrix += item
    print(decrypted_matrix)

decrypt_the_matrix(matrix)
