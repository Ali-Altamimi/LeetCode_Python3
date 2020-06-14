def reverse(x: int) -> int:
    y = str(x)
    if y[0] != '-':
        y = int(y[::-1])
        if y >= 2_147_483_647:
            return 0
        else:
            return y
    else:
        y = y[1::]
        y = y[::-1]
        if y <= -2_147_483_647:
            return 0
        else:
            return y

