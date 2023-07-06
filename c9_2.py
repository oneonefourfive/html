
def init__(name,age,sex = '雌性'):
    print("{0}{1}{2}".format(name,age,sex))
    if len(name)>5:
        print(len(name))
        print("sb")
    else:
        print("ok")
init__('球球',2)
init__('haha',2,'boy')
init__(name = 'tuo bu',age = 3, sex = 'walmart bag')
