import { readFileSync } from 'fs';

const steps: string = readFileSync('../input.txt', 'utf8')

let floor: number = 0;

for (let step of steps) {
    if (step == "(") {
        floor += 1;
    } else if (step == ")") {
        floor -= 1;
    } else {
        continue
    }
}

console.log(`Santa ends up at floor: ${floor}`);
