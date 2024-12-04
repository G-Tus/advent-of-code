import numpy as np

def word_search():
    with open("../input.txt", "r") as file:
        data = np.array([list(row) for row in file.read().splitlines()], dtype='U1')

    total = 0
    total_cross = 0

    for y, row in enumerate(data):
        for x, character in enumerate(row):
            if character == "X":   
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

            elif character == "A":
                if x != 0 and y != 0:
                    try:
                        if (((data[y + 1][x - 1] + character + data[y - 1][x + 1]) in ["MAS", "SAM"]) and
                            ((data[y + 1][x + 1] + character + data[y - 1][x - 1]) in ["MAS", "SAM"])):
                                total_cross += 1

                    except:
                        continue

    print(f"Number of times XMAS: {total}")
    print(f"Number of X-MAS: {total_cross}")

if __name__ == "__main__":
    word_search()
