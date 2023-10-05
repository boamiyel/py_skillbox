a = input()
vowel_let = 'аеёиоуыэюя'
consonant_let = 'бвгджзйклмнпрстфхцчшщьъ'
vowel_flag = 0
consonant_flag = 0
for i in a:
    if i in vowel_let:
        vowel_flag += 1
    if i in consonant_let:
        consonant_flag += 1
print(vowel_flag, consonant_flag)