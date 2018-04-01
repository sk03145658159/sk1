for aa in range(1,36):
    bb=35-aa#鸡的数量
    if(aa*4+bb*2==94):
        print("兔%d,鸡%d" %(aa,bb))
