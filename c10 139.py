class zjkt(Exception):
    def __init__(self,message):
        super().__init__(message)


i = input('please input number:')

n = 114514

try:
    result = n / int(i)
    print (result)
    print("{0}/{1}={2}".format(n,i,result))
except ZeroDivisionError as e:
    '''print("error{0}".format(e))'''
    raise zjkt("no zero")
except ValueError as e:    
    #print("error{0}".format(e))
    raise zjkt("non good bumber")
finally:
    print("运行结束")