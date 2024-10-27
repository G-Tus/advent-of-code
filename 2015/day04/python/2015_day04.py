from hashlib import md5

def hashing():
    with open("../input.txt", "r") as file:
        secret = file.read()

    number = 0
    
    while True:
        hashed = md5(f"{secret}{number}".encode()).hexdigest()

        if hashed[:5] == "00000":
            break
        
        number += 1

    print(f"Number for 5 leading zeroes: {number}")

if __name__ == "__main__":
    hashing()
