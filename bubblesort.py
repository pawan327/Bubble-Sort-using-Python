def bubble_sort(list):

##Swaping the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx]= list[idx+1]
                list[idx+1] = temp 


list=[45,1,54,65,34,2,66,101,434,54,5555,45,5,34,3,6,534]
bubble_sort(list)
print(list)





