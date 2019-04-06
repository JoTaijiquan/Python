'''
Create By Joompot Sriyapan
Date 5/4/2019

Name 
    Example 1.1.5
Description 
    separator
Note
    เครื่องหมาย , (separator) ใช้คั่นระหว่างข้อความในคำสั่ง print 
    ปกติเมื่อคั่นข้อความด้วย , จะเท่ากับเว้นวรรคหนึ่งช่อง
    แต่สามารถเปลี่ยนให้ separator แสดงผลเป็นอย่างอื่นได้
    
    print ("Hello","World","!")                 แสดงผล Hello World !          
    print ("Hello","World","!",sep="")          แสดงผล HelloWorld!
    print ("Hello","World","!",sep="..")        แสดงผล Hello..World..!
    print ("Hello","World",1,2,3,4,5,sep="-")   แสดงผล Hello-World-1-2-3-4-5
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.5
#Python 3.7.3

print ("Hello","World","!")                 #ปกติแล้ว แต่ละคำจะแสดงผลแยกกัน 1 space หรือ 1 เคาะ
print ("Hello","World","!",sep="")          #แสดงผลแค่ละคำโดยไม่มีตัวแยก (separator)
print ("Hello","World","!",sep="..")        #เปลี่ยน separator เป็น ..
print ("Hello","World",1,2,3,4,5,sep="-")   #เปลี่ยน separator เป็น -

