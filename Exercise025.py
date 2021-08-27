def clean_hashtags():
    new_data=[]
    with open("hashtags.txt","r") as file:
        data=file.read()
        data=data.replace("\n"," ")
        data=data.split(" ")
        for i in data:
            if len(i)<6 and i not in new_data:
                new_data.append(i)
    return sorted(new_data)


print(clean_hashtags())