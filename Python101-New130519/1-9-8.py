#Python 3.9.5
#Example 1-9-8
 
class Animal:
    'กำหนดค่าตั้งต้นสำหรับพารามิเตอร์ของคลาส'

    def __init__(self,common_name='Cat'):
        self.common_name = common_name
    def say(self):
        print ("I am",self.common_name)

if __name__ == "__main__":
    tom = Animal()
    tom.say()
    tweety = Animal("Bird")
    tweety.say()
