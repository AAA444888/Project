import os
import bmi
import bmr
def search(nid):
    #當nid.txt存在，輸出nid.txt內的資料
    if os.path.exists(nid+".txt"):
        with open(nid+".txt",mode='r') as file:
            name = file.readline()
            nid = file.readline()
            age = file.readline()
            sex = file.readline()
            height = file.readline()
            weight = file.readline()
            BMI = file.readline()
            BMR = file.readline()
            print(nid + "電子健康檔案如下：")
            print("姓名：" + name.replace('\n',''))
            print("年紀：" + age.replace('\n',''))
            print("性別：" + sex.replace('\n',''))
            print("身高：" + height.replace('\n',''))
            print("體重：" + weight.replace('\n',''))
            bmi.category(BMI.replace('\n',''))
            bmr.category(sex.replace('\n',''),BMR.replace('\n',''))
    #當nid.txt不存在，輸出n找不到檔案
    else:
        print("找不到檔案")