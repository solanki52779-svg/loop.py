for i in range(5):
    print(i)
    
#loop control statment

#1.break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
#2.continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
 
#3.print number from 1 to 10 using for loop 
for i in range(1, 11):
    print(i)  
    
#4.print even number from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i,end='')
for i in range (2,21,2):
        print(i,end='')
        
#5.print odd number is 1 to 15
for i in range(1, 16 ,2):
        print(i)


#6.print each character of using string 
text = "janvi"
for ch in text:
    print(ch)


#7.print all item in this list 
my_list = [10, 20, 30, 40, 50]

for i in range(len(my_list)):
    print(my_list[i])
    
    
#8.print number is reverse order from 10 to 1 
for i in range(10, 0, -1):
    print(i)
    
for i in range(1, 6):
    print(i * 2)