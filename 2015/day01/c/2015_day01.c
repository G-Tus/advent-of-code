#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("../input.txt", "r");
    if (file == NULL) {
        printf("Error opening file");
        return 1;
    }

    int floor = 0;
    char move;

    while ((move = fgetc(file)) != EOF) {
        switch (move) {
            case '(':
                floor++;
                break;

            case ')':
                floor--;
                break;

            default:
                break;
        }
    }

    printf("Santa is on floor: %d\n", floor);

    fclose(file);
    
    return 0;
}