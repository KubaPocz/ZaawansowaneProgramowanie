from time import sleep
id=''
status=''
while(true):
    with open("data.txt","r",encoding="utf-8") as file:
        for line in file:
            id,status = line.split(";")
            if(status != "pending"):
                continue
            break
        
