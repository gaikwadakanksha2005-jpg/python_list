list1=[10,20,30,40,50]
list2=[20,25,10,14,40]
common=[]
for num in list1:
    if num in list2:
        common.append(num)
        print("Common number:",common)
