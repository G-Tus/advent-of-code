def cleanup():

    with open('../input.txt', 'r') as file:
        assignments = file.read().splitlines()

    full_overlap = 0
    partial_overlap = 0

    for assignment in assignments:
        numbers = [int(endpoints) for sections in assignment.split(',') for endpoints in sections.split('-')]

        part1 = ((numbers[0] <= numbers[2]) == (numbers[1] >= numbers[3]) or
                 (numbers[0] >= numbers[2]) == (numbers[1] <= numbers[3]))

        part2 = ((numbers[0] <= numbers[3]) == (numbers[1] >= numbers[2]))

        if part1:
            full_overlap += 1

        if part2:
            partial_overlap += 1
  
    print(f"Count of full overlap: {full_overlap}")
    print(f"Count of partial overlap: {partial_overlap}")

if __name__ == "__main__":
    cleanup()