def func7(arg11, arg12):
    var17 = func8(arg11, arg12)
    var22 = func9(arg11, arg12)
    var26 = func10(arg12, var22)
    var27 = (arg12 | arg12) | 603 & arg11
    var28 = arg12 ^ var26 + (arg11 + var27)
    var29 = (var26 + var27 ^ var22) + arg11
    if var26 < var17:
        var30 = (arg11 + var17) | arg12
    else:
        var30 = var27 | arg11
    var31 = var29 & var22 ^ 261 ^ var29
    var32 = var29 | var27 ^ -1516236652 & var29
    var33 = var29 & arg11 ^ arg11 + var27
    var34 = (var33 | var29) + var22 & var31
    var35 = var27 ^ (var29 - arg12)
    if var32 < arg12:
        var36 = (var31 & 899682326) - arg12 & var27
    else:
        var36 = (var35 + var29 ^ arg12) ^ var26
    var37 = ((var34 ^ var29) | var28) ^ arg11
    var38 = (var22 + var34) | var17 + arg12
    var39 = 489 & var34 - arg12 - var34
    var40 = (var22 | var32) | var29 - var17
    var41 = var17 | (var34 - (320 | var39))
    var42 = var41 | var29 ^ var39
    var43 = var42 | var17 - var22 ^ var32
    result = var26 ^ var39 - var42 | (arg11 | (arg11 | var29)) ^ -685 + arg12
    return result
def func9(arg18, arg19):
    var20 = 0
    for var21 in range(43):
        var20 += arg18 | -4
    return var20
def func8(arg13, arg14):
    var15 = 0
    for var16 in xrange(29):
        var15 += var16 | (9 ^ -5)
    return var15
def func1(arg1, arg2):
    var3 = func4()
    var7 = func5(arg1, arg2)
    var8 = (((var3 ^ var3 ^ -27883644 - (var7 | var3 & var3) - -22133506) | var7 | (arg2 | 667478961 & -25069599) ^ (var3 & arg2) & (arg1 | ((var3 + arg2) ^ var3)) - -69692232 + arg2) | var3 & 142577210) & -687
    var9 = ((-154979512 & var8 + ((1470484197 & -732 + var8) & var8 | (var3 ^ arg1))) | ((218773255 & -586) & (var8 & -607) | var8)) | (arg2 ^ var8 + -112403684 - var8)
    var10 = var7 ^ var9
    result = (var3 - ((var8 ^ var9) | ((19 ^ var3) - arg2 ^ var10 ^ ((var9 | var3) | (-81 - var8))))) - arg1
    return result
def func4():
    func2()
    result = len(range(23))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : 1
def func5(arg4, arg5):
    def func6(acc, rest):
        var6 = 9 + (acc | 8)
        if acc == 0:
            return var6
        else:
            result = func6(acc - 1, var6)
            return result
    result = func6(10, 0)
    return result
def func10(arg23, arg24):
    def func11(acc, rest):
        var25 = rest - rest
        if acc == 0:
            return var25
        else:
            result = func11(acc - 1, var25)
            return result
    result = func11(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 2'
    print 'func_number: 7'
    print 'arg_number: 11'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 44'
    for i in xrange(25000):
        x = 5
        x = func7(x, i)
        print x,
