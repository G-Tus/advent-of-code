import { readFileSync } from 'fs';

const lines: string[] = readFileSync('../input.txt', 'utf8').split("\n");

let elf: number = 0;
let backpacks: number[] = [0];

for (let line of lines) {
    if (line == "") {
        elf += 1;
        backpacks[elf] = 0;
    }
    backpacks[elf] += Number(line);
}

console.log(`Calories of most filled backpack: ${Math.max(...backpacks)}`);

backpacks.sort((n1, n2) => {return n2 - n1;});
console.log(`Sum of 3 most filled backpacks ${backpacks.slice(0, 3).reduce((sum, a) => sum + a, 0)}`)