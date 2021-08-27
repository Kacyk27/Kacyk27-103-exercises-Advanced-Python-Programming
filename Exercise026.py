def clean_hashtags(input_file,output_file,length):
    new_data=[]
    with open(input_file,"r") as file:
        data=file.read()
        data=data.replace("\n"," ")
        data=data.split(" ")
        for i in data:
            if len(i)<=length+1 and i not in new_data:
                new_data.append(i)
    new_data=sorted(new_data)
    with open(output_file,"w") as file:
        for i in new_data:
            file.write(i + "\n")

clean_hashtags("hashtags.txt","clean.txt",5)