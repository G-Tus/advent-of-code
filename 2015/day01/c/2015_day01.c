#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("../input.txt", "r");
    if (file == NULL) {
        printf("Error opening file");
        return 1;
    }

    int floor = 0;
    int position = 0;
    int first = 0;
    char move;
    
    while ((move = fgetc(file)) != EOF) {
        position++;
        switch (move) {
            case '(':
                floor++;
                break;

            case ')':
                floor--;
                break;
        }

        if (first == 0 && floor == -1) {
            first = position;
        }
    }

    printf("Santa is on floor: %d\n", floor);
    printf("Santa first entered basement on position: %d\n", first);

    fclose(file);
    
    return 0;
}