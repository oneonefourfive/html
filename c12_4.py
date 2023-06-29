f = open('test.txt','w+')
f.write('world')

f = open('test.txt','r+')
f.write('Hello')

f = open('test.txt','a')
f.write(' ')


f = open('test.txt','a+')
f.write('world')


f = open('test.txt','r+')
print(f.read())
f_name = 'file.txt'
with open(f_name,"w+",encoding='gbk') as f:
    lines = f.readlines()
    copy_f_name = 'dest_file.txt'
    with open(copy_f_name,'w',encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('sucess')