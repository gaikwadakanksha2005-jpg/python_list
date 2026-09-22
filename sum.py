num=[12,23,7,10,15]
even=[]
odd=[]
for i in num:
    if i % 2== 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
print("Odd:",odd)        