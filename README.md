# sk1
'''
start=1;
rows=10;
for row in range(start,rows):
    str1=""
    space=""
    for col in range(1,row+1):
        if (row==3 and col==2) or (row==4 and col==2):
            space="  "
        else:
            space=" "
        str1+=(str(row)+"*"+str(col)+"="+str(row*col)+space)#转换成字符串
    print(str1);

'''
