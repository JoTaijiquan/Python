#Example 1.05
#Python3.6.5

print ("Hello","World","!")                 #ปกติแล้ว แต่ละคำจะแสดงผลแยกกัน 1 space หรือ 1 เคาะ
print ("Hello","World","!",sep="")          #แสดงผลแค่ละคำโดยไม่มีตัวแยก (separator)
print ("Hello","World","!",sep="..")        #เปลี่ยน separator เป็น ..
print ("Hello","World",1,2,3,4,5,sep="-")   #เปลี่ยน separator เป็น -

'''
เปลี่ยนตัวแยก (separator) ในคำสั่ง print ()

print ("Hello","World","!")                 แสดงผล Hello World !          
print ("Hello","World","!",sep="")          แสดงผล HelloWorld!
print ("Hello","World","!",sep="..")        แสดงผล Hello..World..!
print ("Hello","World",1,2,3,4,5,sep="-")   แสดงผล Hello-World-1-2-3-4-5
'''
