#this code does the first 3 hackerrank python challenges 
# first challenge print hello world to terminal
print('challenge 1 -  Hello World!')



# this second challenge is called if-else 
# takes input from python as an integer called n, let's assume n = 34
    #if __name__ == '__main__':
        #n = int(input().strip())
n = 34
if n % 2 == 1 :
    print('challenge 2 - Weird')
if n % 2 != 1 and (2<=n<=5 or n>20):
    print('challenge 2 - Not Weird')
if n % 2 != 1 and 6<=n<=20 :
    print('challenge 2 - Weird')





# this third challenge is called Arithmetic Operators
# takes 2 input from python as an integers called a&b
    #if __name__ == '__main__':
    #   a = int(input())
    #    b = int(input())
a = 3
b = 5
print(f'challenge 3 : {a+b, a-b, a*b}')





# this fourth challenge is called division 
# takes 2 input from python as an integers called a&b, prints out dision integer and float
    #if __name__ == '__main__':
    #a = int(input())
    #b = int(input())
a = 33
b = 5
print(f'challenge 4 : division integer : {int(a/b)}') 
print(f'challenge 4 : division float : {a/b}') 





# this fifth challenge is called loop
# takes an input from python as an integers called n, prints out the squares of numbrts 1-n
    #if __name__ == '__main__':
    #n = int(input())
n = 2
x = 0 
while x < n :
    print(f'challenge 5 : {x*x}')
    x += 1




# this sixth challenge is called Write a function
# runs a function to determine if the year in question is a leap year
# year = int(input())
year = 1994

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 :
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    
    print(f'challenge 6 : {leap}')
    return leap
    
is_leap(year)




# this seventh challenge is called print function
# takes an integer n and prints out the values of 1-n without spacing 
# if __name__ == '__main__':
#    n = int(input())
n = 4    
myTuple = []
for x in range(n): myTuple.append(x+1)
art = "".join(str(myTuple).split(','))
cod = "".join(art.split(" "))
color = cod[1:-1]
print(f'challenge 7 : {color}')
