import { readFileSync } from 'fs';

const rucksacks: string[] = readFileSync('../input.txt', 'utf8').split("\n");

let priority: number = 0;
let badge: number = 0;
let lut: {[key: string]: number} = {};

for (let i = 1; i < 27; i++) {
    lut[String.fromCharCode(i + 96)] = i;
    lut[String.fromCharCode(i + 64)] = i + 26;
}

let rucksack: string;
let found: boolean[];
let half: number;

for (let i = 0; i < rucksacks.length; i++) {
    rucksack = rucksacks[i];
    found = [false, false];
    half = ~~(rucksack.length/2);

    for (let character of rucksack) {
        if (!found[0] && (rucksack.indexOf(character, half) > -1)) {
            found[0] = true;
            priority += lut[character];
        }

        if ((i % 3 === 0) && 
            !found[1] && 
            (rucksacks[i + 1].indexOf(character) > -1) && 
            (rucksacks[i + 2].indexOf(character) > -1)
        ) {
            found[1] = true;
            badge += lut[character];
        }

        if (found.every(Boolean)) {
            break
        }
    }
}

console.log(`Total priority: ${priority}`)
console.log(`Total badge priority: ${badge}`)