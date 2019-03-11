#Example 2.2.4
#Python 3.6.5
#Draw * to both side.

num0 = '''
    ********    -
   *        *   -
  *          *  -
  *          *  -
  *          *  -
  *          *  -
  *          *  -
   *        *   -
    ********    -
'''

num1 = '''
       **       -
     *  *       -
   *    *       -
        *       -
        *       -
        *       -
        *       -
        *       -
     *******    -
'''
num2 = '''
    *****       -
   *      *     -
          *     -
        *       -
      *         -
     *          -
    *           -
   *            -
  ********      -
'''

if __name__=='__main__':
    #num=[]
    #for i in range(2):
     #   print ("num"+str(i))
      #  num.append("num"+str(i))
    a = "num"
    b = "0"
    
    num = {}
    num [a+b] = None
    print (num)
    
    print (num[0])
    print (num[1])
