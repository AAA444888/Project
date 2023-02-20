def add(name,nid,age,sex,height,weight,BMI,BMR):
    #將輸入的資料存進nid.txt
    with open(nid+".txt",mode='w') as file:
        file.write(name + "\n"+nid + "\n"+age + "\n"+sex + "\n"+height + "\n"+weight + "\n"+BMI + "\n"+BMR + "\n")
    print("檔案新增成功")