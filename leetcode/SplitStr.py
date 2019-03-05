



a_1 = input()
a_2 = input()
word_len = 8


def str_split(string, word_len):
    import re
    if len(string) <= word_len:
        print(string + '0' * (word_len - len(string)))
    else:
        rst = re.findall(r'.{%d}' % word_len, string)
        if len(string) % word_len == 0:
            for i in rst:
                print(i)
        else:
            for i in rst:
                print(i)
            rear = string[len(rst) * word_len:]
            rear = rear + '0' * (word_len - len(rear))
            print(rear)

    return


str_split(a_1, word_len)
str_split(a_2, word_len)




