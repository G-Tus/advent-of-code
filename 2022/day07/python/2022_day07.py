def filesystem():

    with open("../input.txt", "r") as file:
        terminal = file.read().splitlines()

    directories = {"/": {'total': 0}}
    current_folder = directories
    path = []

    for line in terminal:
        match line.split():
            case ["$", "ls"]:
                continue
            case ["$", "cd", ".."]:
                path.pop()
                current_folder = directories[path[0]]
                for step in path[1:]:
                    current_folder = current_folder[step]
            case ["$", "cd", folder]:
                path.append(folder)
                current_folder = current_folder[folder]
            case ["dir", folder]:
                if folder not in current_folder:
                    current_folder[folder] = {"total": 0}
            case [size, _]:
                current_folder = directories[path[0]]
                current_folder['total'] += int(size)
                for step in path[1:]:
                    current_folder = current_folder[step]
                    current_folder['total'] += int(size)

    total = recursion(directories, 0)
    print(f"Total of small directories: {total}")

    full_size = directories["/"]["total"]
    minimum_deletion = full_size - (70000000 - 30000000)

    smallest_folder = find_directory(directories, 70000000, minimum_deletion)

    print(f"Size of smallest directory that can be deleted: {smallest_folder}")

def find_directory(data, size, minimum):

    if isinstance(data, dict):
        for value in data.values():
            size = find_directory(value, size, minimum)
        return size

    else:
        if data <= size and data >= minimum:
            size = data
        return size

def recursion(data, total):

    if isinstance(data, dict):
        for value in data.values():
            total = recursion(value, total)
        return total

    else:
        if data <= 100000:
            total += data
        return total

if __name__ == "__main__":

    filesystem()