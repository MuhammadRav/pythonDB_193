def changeme(mylist):   #this changes a passed list#
    mylist = [1,2,3,4];
    print ("Values inside the function: ", mylist)
    return
mylist = [10,20,30];
changeme(mylist);
print ("Values outside the function: ", mylist)


def printinfo(arg1, *vartuple):
    "this is test"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return;
printinfo(10);
printinfo(70, 60, 50);

#lambda#
sum = lambda arg1, arg2: arg1 + arg2;
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))
