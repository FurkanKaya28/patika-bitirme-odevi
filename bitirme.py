# 1. ödev
a = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]


def list_flatter(l: list):

    return str(l).replace('[', '').replace(']', '').split(',')


print(list_flatter(a))

# 2. ödev

f = [[1, 2], [3, 4], [5, 6, 7]]

def list_reverse(l:list):
    ret = []
    l.reverse()
    for i in l:
        i.reverse()
        ret.append(i)
    return ret
print(list_reverse(f))