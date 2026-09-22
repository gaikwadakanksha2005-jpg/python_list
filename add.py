list1=[10,20,20,40]
list2=[5,10,15,20]
result=[]
for i in range(len(list1)):
    result.append(list1[i]+list2[i])
    print("List1:",list1)
    print("List2:",list2)
    print("Sum:",result)