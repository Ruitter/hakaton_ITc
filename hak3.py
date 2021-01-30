print ("Посмотреть задачу №4??? y/n??")
y = input()
if y == 'y' or y =='Y' :
	sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
	print(sequence_0)
	for i in range(len(sequence_0)):
	    for j in range(len(sequence_0)):
	        if i != j and sequence_0[i] == sequence_0[j]:
	            break
	           
	    else:
	    	print('Эти значения уникальны:' + str(sequence_0[i]))
	sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
	print(sequence_1)
	for i in range(len(sequence_1)):
	    for j in range(len(sequence_1)):
	        if i != j and sequence_1[i] == sequence_1[j]:
	            break
	    else:
	        print('Эти значения уникальны:' + str(sequence_1[i]))
	sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
	print(sequence_2)
	for i in range(len(sequence_2)):
	    for j in range(len(sequence_2)):
	        if i != j and sequence_2[i] == sequence_2[j]:
	            break
	    else:
	        print('Эти значения уникальны:' + str(sequence_2[i]))
	sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
	print(sequence_3)
	for i in range(len(sequence_3)):
	    for j in range(len(sequence_3)):
	        if i != j and sequence_3[i] == sequence_3[j]:
	            break
	    else:
	        print('Эти значения уникальны:' + str(sequence_3[i]))
else :
	pass

print ("Посмотреть задачу №3??? y/n??")
y = input()
if y == 'y' or y =='Y' :
	print ('Введите сторону квадрата')
	y = int(input())
	print(f'S = {y**2}')
	print(f'P = {4*y}')
else :
	pass

print ("Посмотреть задачу №2??? y/n??")
y = input()
if y == 'y' or y =='Y' :
	a= int (input ("Введите число А: "))
	b= int (input ("Введите число B: "))
	c= int (input ("Введите число C: "))
	a1= a+b
	b1= c-a
	c1=a+b+c
	print ("Новое значение А = ", a1)
	print ("Новое значение В = ", b1)
	print ("Новое значение С = ", c1)
else :
	pass

print ("Посмотреть задачу №6??? y/n??")
y = input()
if y == 'y' or y =='Y' :
	num = int (input ("Введите четырехзначное число: "))
	a = num //1000
	b= (num//100)%10
	c= (num//10)%10
	d = num%10
	if a > b and b > c and c > d:
	    print ("Да")
	else:
	    print ("Нет")
else :
	pass



