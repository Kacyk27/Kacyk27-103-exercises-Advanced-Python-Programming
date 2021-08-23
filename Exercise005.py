def calculate():
    x=[]
    for i in range(1,10):
        for j in range(0,10):
            for k in range(0,10):
                if f"{i}{j}{k}" == f"{k}{j}{i}":
                    x.append(f"{i}{j}{k}")
    return x

print(len(calculate()))