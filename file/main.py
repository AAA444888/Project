import os
import insert
import bmi
import bmr
import query
import ideal
import delete
while True:
    #選擇要執行的項目
    choice =int(input("(1)新增病患資料(2)查詢病患資料(3)刪除病患資料(4)結束程式："))
    if choice ==1:
        #輸入資料
        name = input("請輸入病患的姓名：") 
        nid = input("請輸入病患的身分證字號：") 
        age = input("請輸入病患的年紀：")
        sex = input("請輸入病患的性別(男生請輸入1，女生請輸入2：")
        height = input("請輸入病患的身高(cm)：")
        weight = input("請輸入病患的體重(kg)：")
        #計算BMI跟BMR，判定體位
        BMI=bmi.calculate(height,weight)
        bmi.category(BMI)
        ideal.weight(height,BMI)
        BMI=str(BMI)
        BMR=bmr.count(age,sex,BMI)
        bmr.category(sex,BMR)
        BMR=str(BMR)
        #建檔
        insert.add(name,nid,age,sex,height,weight,BMI,BMR)
    elif choice==2:
        #以身分證字號做資料查詢
        nid = input("請輸入病患的身分證字號：")
        query.search(nid)
    elif choice==3:
        nid = input("請輸入病患的身分證字號：")
        delete.delete(nid)
    elif choice==4:
        print("結束程式！")
        break
    else:
        print("無效指令！")
os.system('pause')