def check_palindrome_possibility(word):
    char_count = {}

    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    return odd_count <= 1


def get_palindrome(pal):
    if check_palindrome_possibility(pal):
        char_count = {}
        palindrome = []

        for char in pal:
            char_count[char] = char_count.get(char, 0) + 1

        for char, count in char_count.items():
            half_count = count // 2
            palindrome.extend([char] * half_count)

        if 1 in char_count.values():
            for char, count in char_count.items():
                if count == 1:
                    palindrome.insert(len(palindrome) // 2, char)
        ans = str(''.join(palindrome))
        return ans + ans[::-1]
    else:
        return 'Палиндром невозможен'


a = input('Введите строку: ')
print(get_palindrome(a))


