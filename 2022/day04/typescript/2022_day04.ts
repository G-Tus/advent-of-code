import { readFileSync } from 'fs';

const assignments: string[] = readFileSync('../input.txt', 'utf8').split("\n");

let full_overlap: number = 0;
let partial_overlap: number = 0;

for (let assignment of assignments) {
    let numbers: number[] = assignment.split(/-|,/).map(Number);

    if ((numbers[0] <= numbers[2]) == (numbers[1] >= numbers[3]) ||
        (numbers[0] >= numbers[2]) == (numbers[1] <= numbers[3])) {
            full_overlap += 1;
        }

    if ((numbers[0] <= numbers[3]) == (numbers[1] >= numbers[2])) {
        partial_overlap += 1;
    }
}

console.log(`Count of full overlap ${full_overlap}`)
console.log(`Count of partial overlap: ${partial_overlap}`)