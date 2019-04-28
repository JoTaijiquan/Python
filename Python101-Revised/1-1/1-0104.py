'''
Create By Joompot Sriyapan
Date 5/4/2019

Name 
    Example 1.1.4
Description 
    แสดงผลข้อความหลายชุด
Note
    print ("3x4 =")     แสดงผล 3x4 = 12   
    print ("Hello"+"!") แสดงผล Hello!
    print ("Hello!"*3)  แสดงผล Hello!Hello!Hello!

    เครื่องหมาย , (separator) ใช้คั่นระหว่างข้อความในคำสั่ง print 
    ปกติเมื่อคั่นข้อความด้วย , จะเท่ากับเว้นวรรคหนึ่งช่อง
    แต่สามารถเปลี่ยนให้ separator แสดงผลเป็นอย่างอื่นได้
    
    print ("Hello","World","!")                 แสดงผล Hello World !          
    print ("Hello","World","!",sep="")          แสดงผล HelloWorld!
    print ("Hello","World","!",sep="..")        แสดงผล Hello..World..!
    print ("Hello","World",1,2,3,4,5,sep="-")   แสดงผล Hello-World-1-2-3-4-5
Display
2 12 ABC
3x4 =  12
Hello World !
HelloWorld!
Hello..World..!
Hello-World-1-2-3-4-5
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.4
#Python 3.7.3

print (1+1,3*4,"ABC")
print ("3x4 = ",3*4)
print ("Hello","World","!")                 #ปกติแล้ว แต่ละคำจะแสดงผลแยกกัน 1 space หรือ 1 เคาะ
print ("Hello","World","!",sep="")          #แสดงผลแค่ละคำโดยไม่มีตัวแยก (separator)
print ("Hello","World","!",sep="..")        #เปลี่ยน separator เป็น ..
print ("Hello","World",1,2,3,4,5,sep="-")   #เปลี่ยน separator เป็น -
