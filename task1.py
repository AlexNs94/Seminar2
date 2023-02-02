print('Введите кол во арбузов: ')
num = int(input())

print('Введите вес арбуза:  ')
cur_ar = int(input())
min_ar = max_ar = cur_ar
input_numbers = str(cur_ar)
for i in range(2,num +1):
    cur_ar = int(input())
    input_numbers += " " + str(cur_ar)
    if min_ar > cur_ar:
       min_ar = cur_ar
    elif max_ar < cur_ar:
        max_ar = cur_ar

print ("Input :", num ,"->",input_numbers)
print ("Output :", min_ar,max_ar )