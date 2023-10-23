def get_let_statistics(file):
    char_count = {}

    with open(file, 'r') as f:
        for line in f:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    sorted_count = sorted(char_count.items(), key=lambda x: x[1])
    return sorted_count


data = "input.txt"
result = get_let_statistics(data)

with open("output.txt", 'w') as f:
    for char, count in result:
        f.write(f"{char}: {count}\n")