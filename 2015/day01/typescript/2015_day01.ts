import { readFileSync } from 'fs';

const steps: string = readFileSync('../input.txt', 'utf8')

let floor: number = 0;
let position: number = 0;
let first: number = 0;

for (let step of steps) {
    position++;
    if (step == "(") {
        floor += 1;
    } else if (step == ")") {
        floor -= 1;
    }

    if (floor == -1 && first == 0) {
        first = position;
    }
}

console.log(`Santa ends up at floor: ${floor}`);
console.log(`Santa enters basement at step: ${first}`);
