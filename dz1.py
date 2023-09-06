import random
import time

i = 0

while i != 1:
    i = int(input("Продовжити/Стартувати - 0, закінчити - 1 : "))
    if (i == 1):
        break
    b=random.randint(1, 3)

    a = int((input("Вибери: камінь - 1, ножниці - 2, чи папір - 3 : ")))

    print("Вибирає робот...")
    time.sleep(3)
    b=random.randint(1, 3)
    if (b == 1) and (a==3):
        print("Виграв робот")
        print("У робота камінь")
    elif(b==2) and (a == 1):
        print("Виграв робот")
        print("У нього були ножниці")
    elif(b==3) and (a == 2):
        print("Виграв робот")
        print("У нього були ножниці")
    elif (a == 1) and (b == 3):
        print("Виграла людина")
        print("І нього були ножниці")
    elif (a == 2) and (b == 1):
        print("Виграла людина")
        print("У нього камінь")
    elif (a == 3) and (b == 2):
        print("Виграла людина")
        print("У нього був папер")
    
        
    


