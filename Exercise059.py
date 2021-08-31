def decimal_to_binary(decimal):

    result=""
    if decimal == 0:
        return "0"
    while decimal > 0:
        result += str(decimal % 2)
        decimal = decimal // 2

    return result[::-1]
