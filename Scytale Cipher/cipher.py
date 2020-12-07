
def encrypt(key, plaintext):

    grid = []
    row = []

    for letter in plaintext:
        row.append(letter)
        if len(row) == key:
            grid.append(row)
            row = []

    text = []

    for col in range(key):
        temp = []
        for row in grid:
            temp.append(row[col])
        text.append(str.join('', temp))

    return str.join('', text)


def decrypt(key, ciphertext):

    rows = len(ciphertext) // key
    grid = []

    for row in range(rows):
        temp_row = []
        for i in range(key):
            temp_row.append(ciphertext[row + i * rows])
        grid.append(temp_row)

    rows = []

    for i in range(len(grid)):
        rows.append(str.join('', grid[i]))

    return str.join('', rows)
