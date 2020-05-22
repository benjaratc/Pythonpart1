#!/usr/bin/env python
# coding: utf-8

# Quiz1

# เขียนคำสั่งคำนวณหาเศษเหลือจากการหาร 2345 ด้วย 13 

# In[149]:


a = 2345 % 13
print(a)


# เขียนคำสั่งหาคำตอบจากการหาร 1567 ด้วย 17 โดยไม่เอาเศษส่วน

# In[150]:


b = int(1567 / 17)
print(b)


# FirstName กับ Firstname เป็นตัวแปรเดียวกันหรือไม่?
# 

# They are different. ("N" and "n" in Python are not the same)

# 13Friday เป็นตัวแปรที่ถูกต้องหรือไม่?

# In[151]:


var = 13Friday
print(var)      #it is string so it needs quotes 


# จง Print ผลลัพธ์จากข้อ 1,2 โดยใช้คำสั่ง format

# In[152]:


print("The first number is {} and the second number is {}".format(a,b))


# Quiz 2

# เขียนฟังก์ชั่นไม่มีชื่อให้รับพารามิเตอร์ 1 ตัว และ ปริ้นค่านั้นหารด้วย 3 
# 

# In[46]:


divideByThree = lambda a: a/3
print(divideByThree (6))


# เขียนฟังก์ชั่นธรรมดารับค่า 4 พารามิเตอร์ และหาค่าเฉลี่ย

# In[50]:


def avg(a,b,c,d):
    result = (a+b+c+d)/4
    return result

print(avg(1,2,3,4))


# เขียนฟังก์ชั่นไม่มีชื่อให้รับพารามิเตอร์ 3 ตัว และหาค่าเฉลี่ย

# In[49]:


average2 = lambda a,b,c:(a+b+c)/3
print(average(1,2,3))


# Quiz 3

# สร้างลิสต์ระบุชื่อ นามสกุล อายุ ตัวเอง

# In[52]:


name =['Benjarat','Chava',28]
print(name)


# ลบอายุออกจากลิสต์ 

# In[53]:


del name[2]
print(name)


# ลดอายุตัวเอง 10 ปี และแทรกไว้หน้าสุดของลิสต์

# In[54]:


name.insert(0,18)
print(name)


# เพิ่มส่วนสูง น้ำหนักลงในลิสต์ โดยไปต่อท้าย

# In[57]:


name.append(45)
print(name)


# In[58]:


name.append(155)
print(name)


# Print สมาชิกในลิสต์ตัวที่ 3 ถึงตัวสุดท้าย

# In[59]:


print(name[2:])


# Quiz 4

# a = [[[1,3],[3,4]],[5,[5,6],[7,8]]] แล้ว a[1][1][1] คือค่าใด

# In[60]:


a = [[[1,3],[3,4]],[5,[5,6],[7,8]]] 
print(a[1][1][1])


# เขียนชื่อนามสกุลอายุอยู่ในลิสต์เดียวของคน 4 คนแล้วใส่ไว้ในลิสต์ (Nested List) และแสดงผล

# In[94]:


name1 =['Benjarat','Chava',28]
name2 =['Ivan','Lee',30]
name3 =['Gift','Chava',20]
name4 =['Natty','Chun',29]
name_all = [name1,name2,name3,name4]
print(name_all)


# ลบคนสุดท้ายของลิสต์นั้นออกและแสดงผล

# In[96]:


name_all[3]


# In[97]:


del name_all[3]


# In[98]:


print(name_all)


# เพิ่มคนที่ 5 เข้ามาเป็นคนแรกของ Nested List และแสดงผล

# In[104]:


name5 =['Tuk','Veera',27]


# In[108]:


name_all.insert(0,name5)


# In[109]:


name_all


# แก้ไขส่วนสูงคนที่สอง +10 และแสดงผล

# In[113]:


name_all[1][2] = 38
print(name_all)


# Quiz 5

# กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10] จงเขียน Map เพื่อหาเลขยกกำลังสามทั้งหมดของ lst ในรูปแบบ Lambda Function และ ฟังก์ชั่นธรรมดา

# In[118]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda a:(a ** 3),lst)
print(list(result))


# In[119]:


def func(x):
    return x ** 3
print(list(map(func, lst)))


# กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10] จงเขียน Filter เพื่อหาเลขใดในลิสต์เมื่อยกกำลังสองแล้วหารสองไม่ลงตัว ในรูปแบบ Lambda Function และ ฟังก์ชั่นธรรมดา

# In[121]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda a:(a ** 2 % 2)!= 0 ,lst)
print(list(result))


# In[122]:


def func(x):
    return (x ** 2 % 2) != 0  
print(list(filter(func, lst)))


# Quiz 6

# กำหนดให้ lst = [1,2,3,4,5] จงเขียน List Comprehension เพื่อนำทุกตัวใน lst ไปคูณกับ 2 และลบด้วย 1 พร้อมกับแสดงผล

# In[128]:


lst = [1, 2, 3, 4, 5]
lst2 = [(item * 2) - 1 for item in lst]
print(lst2)


# กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10,11,12,13] จงเขียน List Comprehension เพื่อหาตัวที่หาร 3 ไม่ลงตัว และนำผลลัพธ์นั้นยกกำลังสาม พร้อมกับแสดงผล

# In[134]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lst2 = [item ** 3 for item in lst if (item % 3 != 0)]
print(lst2)


# Quiz 7

# จงเขียนโปรแกรมตรวจสอบคะแนนเด็กนักเรียน ถ้าเด็กได้คะแนนมากกว่า 80 เกรด A มากกว่า 70 เกรด B มากกว่า 60 เกรด C มากกว่า 50 เกรด D และต่ำกว่า 50 เกรด F

# In[136]:


grade = 77 

if grade > 80:
    print("A")
elif grade > 70: 
    print("B")
elif grade > 60: 
    print("C")
elif grade > 50: 
    print("D")
elif grade <= 50: 
    print("F")


# Quiz 8

# กำหนดให้ A = [1, 2, 3, 4, 5] และ B = [2, 3, 1, 3, 2] จงเขียน Map แบบ Multiple-list operations โดยให้ B ยกกำลังด้วย A พร้อมกับแสดงผล

# In[137]:


A = [1, 2, 3, 4, 5]
B = [2, 3, 1, 3, 2]

result = map(lambda a,b: b ** a, A,B)
print(list(result))


# จงเขียนชื่อนักเรียน เลขที่ และคะแนนสอบไฟนอล พร้อมกับใช้คำสั่ง Zip() ในการจับคู่พร้อมกับแสดงผลลัพธ์ที่ถูกต้อง

# In[138]:


name = ["Ben","Nuk","Gift","Ivan"]
number = [29,45,32,2]
score = [100,95,99,100]

mapped = list(zip(name,number,score))
print(mapped)


# Quiz 9

# กำหนดให้ lst = [5, 2, 1, 3, 2] จงเขียนฟังก์ชั่น Reduce เพื่อหาผลลัพท์สุดท้ายของดำเนินการแบบเลขยกกำลัง 

# In[143]:


from functools import reduce
lst = [5, 2, 1, 3, 2]
result = reduce((lambda x,y: x ** y), lst)
print(result)


# กำหนดให้ lst = [1,2,3,4,5,6,7,8,9,10] จงเขียนฟังก์ชั่น Reduce เพื่อหาผลลัพท์สุดท้ายของดำเนินการแบบการคูณ

# In[144]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce((lambda x,y: x * y), lst)
print(result)

