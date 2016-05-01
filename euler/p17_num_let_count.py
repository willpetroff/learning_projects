def num_block_con(num, level):
    num_alpha_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                      10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                      16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
                      40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    levels_dict = {0: '', 1: 'thousand', 2: 'million', 3: 'billion'}
    num_string = str(num)
    position_count = len(num_string)
    word = ''
    for item in num_string:
        if position_count == 3 and item != '0':
            word += num_alpha_dict[int(item)] + ' ' + 'hundred'
            if num_string[-2:] != '00':
                word += ' and '
            position_count -= 1
        elif position_count == 2 and int(item) != 1:
            word += num_alpha_dict[int(item)*10] + ' '
            position_count -= 1
        elif position_count == 2 and int(item) == 1:
            word += num_alpha_dict[int(item+num_string[-1])]
            break
        else:
            word += num_alpha_dict[int(item)]
            position_count -= 1
    word += ' ' + levels_dict[level]
    return word


def num_to_block(num):
    num_string = str(num)
    num_len = len(num_string)
    word = []
    level = 0
    while num_len >= 3 and num_string:
        word.append(num_block_con(num_string[-3:], level))
        num_string = num_string[:-3]
        level += 1
    while num_len < 3 and num_string:
        word.append(num_block_con(num_string[-num_len:], level))
        num_string = num_string[:-num_len]
    return ''.join(word[::-1])

all_words = []
letter_count = 0
for number in range(1, 1001):
    all_words.append(num_to_block(number))
for word in all_words:
    for letter in word:
        if letter.isalpha():
            letter_count += 1
print(letter_count)
