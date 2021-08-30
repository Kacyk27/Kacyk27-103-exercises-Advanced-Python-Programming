def binary_to_int():
    result = []
    with open("binary.txt","r") as file:
        data=file.read()
        data_as_list=data.split("\n")
        for i in data_as_list:
            result.append(int("0b"+i,base=2))

    return result

print(binary_to_int())

#This one work on Jupyter and Pycharm, but doesn't work at udemy. 