def move(a, st, fn):
    if n == 1:
        print(a, st, fn)
    else:
        cnt = 6 - st - fn
        move(a -1, st, cnt)
        print(a - 1, cnt, fn)
        move(a - 1, cnt, fn)
a = int(input())
move(a, 1, 3)
print(n)
