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