import { readFileSync } from 'fs';

const matches: string[] = readFileSync('../input.txt', 'utf8').split("\n");

type ScoreMatrix = {[key: string]: {[key: string]: number}};

const part1: ScoreMatrix = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6
    }
};

const part2: ScoreMatrix = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
};

let score1: number = 0;
let score2: number = 0;
let you: string;
let me: string;

for (let match of matches) {
    [you, me] = match.split(" ");
    score1 += part1[you][me];
    score2 += part2[you][me];
}

console.log(`Final score part 1: ${score1}`);
console.log(`Final score part 2: ${score2}`)
