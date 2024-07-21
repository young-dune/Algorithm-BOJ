while 1:
    line = input()
    if line == '0':
        break
    elif line == line[::-1]:
        print('yes')
    else:
        print('no')