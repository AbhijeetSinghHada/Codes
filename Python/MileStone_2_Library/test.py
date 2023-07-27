with open("data.csv","r") as db:
    datas = db.readlines()
    datas = [data.split(', ') for data in datas]
    datas = [data[0].strip().split(',') for data in datas]
    print(datas)

with open("data.csv","+a") as db:
    for data in datas:
        temp = ','.join(i for i in data)
        db.writelines('\n'+temp)
            