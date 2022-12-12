class CRT:
    
    def __init__(self):

        with open("../input.txt", "r") as file:
            instructions = file.read().splitlines()

        self.height = 6
        self.width = 40
        self.pixels = []
        for _ in range(self.height):
            self.pixels.append(["."] * self.width)

        self.cycles = [20, 60, 100, 140, 180, 220]
        self.x = 1
        self.cycle = 0
        self.total = 0
        self.update_sprite()

        for instruction in instructions:
            opcode = instruction.split()
            match opcode:
                case ['noop']:
                    self.perform_cycle()
                case ['addx', amount]:
                    self.perform_cycle()
                    self.perform_cycle()
                    self.x += int(amount)

        print(f"Total signal strengths: {self.total}")
        for row in self.pixels:
            string = ""
            for character in row:
                string += character
            print(string)

    def perform_cycle(self):
        self.draw_screen()
        self.update_total()
        self.cycle += 1

    def draw_screen(self):
        self.update_sprite()
        column = self.cycle % self.width
        row = self.cycle // self.width
        if column in self.sprite:
            self.pixels[row][column] = "#"

    def update_total(self):
        if self.cycle in self.cycles:
            self.total += self.x * self.cycle

    def update_sprite(self):
        self.sprite = [self.x - 1, self.x, self.x + 1]

if __name__ == "__main__":

    CRT()