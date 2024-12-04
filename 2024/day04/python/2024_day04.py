import numpy as np

def word_search():
    with open("../input.txt", "r") as file:
        data = np.array([list(row) for row in file.read().splitlines()], dtype='U1')

    total = 0

    for y, row in enumerate(data):
        for x, character in enumerate(row):
            if character != "X":
                continue

            for x_delta in [-1, 0, 1]:
                for y_delta in [-1, 0, 1]:
                    if x_delta == 0 and y_delta == 0:
                        continue

                    word = character

                    try:
                        for step in range(1, 4):
                            if (y_index := y + y_delta * step) < 0 or (x_index := x + x_delta * step) < 0:
                                raise Exception
                            
                            word += data[y_index][x_index]

                    except:
                        continue

                    if word == "XMAS":
                        total += 1

    print(f"Number of times XMAS: {total}")

if __name__ == "__main__":
    word_search()
