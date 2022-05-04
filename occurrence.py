
def occurrence():
    num_1 = input("enter the list of numbers, separate with comas: ")
    num_3 = num_1.split(",")
    num_2 = list(num_3)
    existing_num = []
    new_num = []
    i = 0
    occur_num = 0
    for i in num_2:
        i = int(i)
        if i in new_num:
            existing_num.append(i)
            occur_num += 1
        else:
            new_num.append(i)
        if i in new_num and i in existing_num:
            del new_num[new_num.index(i)]
            existing_num.append(i)
            occur_num += 1
        else:
            pass
             
    existing_num.sort()
    new_num.sort()
    j = 0
    dic = {}
    counted_num = []
    for j in existing_num:
        num = existing_num.count(j)
        
        if j in counted_num:
            pass
        else:
            counted_num.append(j)
            dic[j] = num
    for j in new_num:
        dic[j] = 1
        
    print("{integar:number of occurrence}",dic)            
occurrence()
        
    
        