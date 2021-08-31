def decimal_to_binary(decimal):
    result = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        result += str(decimal % 2)
        decimal = decimal // 2

    return result[::-1]


def bitwise_or(x, y):

    if x < 0 or y < 0:
        raise ValueError("Both numbers must be positive.")

    x=decimal_to_binary(x)
    y=decimal_to_binary(y)

    x_y_len = max(len(x),len(y))
    x_filled = x.zfill(x_y_len)
    y_filled = y.zfill(x_y_len)

    bin_or = [str(int(char_x == "1" or char_y == "1")) for char_x, char_y in zip(x_filled, y_filled)]
    bin_res = "".join(bin_or)
    dec_res = int(bin_res, base=2)

    return dec_res

print(bitwise_or(15,13))
