#print("Hello Again!")

#a = 1
#b = 2
#c = a + b
#print(c)

#d = "Hello Hello!"
#print(d)

num_list = [1, 2, 3, 4]
#print(num_list[1])

# for num in num_list:
# 	print(num)
#select code, command / will add hashtag

#cumbersome way to write for loop
#print(num_list[0])
#print(num_list[1])
#print(num_list[2])
#print(num_list[3])

name_list=["John", "Mary", "Tom"]

#this will give you an error because you cannot add a string and a number
#for name in name_list:
	#for num in num_list:
		#print(name + num)

# for name in name_list:
# 	for num in num_list:
# 		print(name + str(num))

#there are two ways to do the following:
another_list=[]
for num in num_list:
	another_list.append((num+3)*2)
print(another_list)

#here is the second way, it is BETTER if you can understand it
another_list_2= [(num+3)*2 for num in num_list]
print(another_list_2)

#If statement
for num in another_list:
	if (num > 11):
		print("Big number:" + str(num))
	elif (num < 9):
		print("Small Number:" + str(num))

def my_function():
	print("Hello World!")
	print("Hello World again!")
	print("Hello World using a function!")

my_function()

def augmented_numbers(num1, num2):
	return (num1+num2) ** 2

print (augmented_numbers(1, 2) + 2)

for i in range(2000):
	print(i+1)











