import math
def br_of_divisors(n):   #samo smeni def na sum ;) 
    sum1=0
    br=0
    for i in range (1,n+1):
        if n%i==0:
         sum1=sum1+i
         br=br+1
    return br  #return sum1

                                #x=int(input())
#print(sum_of_divisors(x))

#a="abcde"   a[-1] = e !!!
#celiq na obratno  a[::-1]
              #      4aka purviq :  4aka vtoriq : stupka
# a[1:2] ---> b



def is_prime(n):
    x=0
    if (n<=1):
        return False
    else:
        for i in range (2,n):
            if (n%i==0):
                x=x+1
        if(x>0):
            return False
        else :
            return True

def prime_number_of_divisors(n):
    y=br_of_divisors(n)
    if (is_prime(y)==True):
        print("True")#return True
    else:
        print("false")#return False
    

#prime_number_of_divisors(x)

def contains_digit(number, digit):
        if digit in number:
            print("true")
        else:
            print("false")
        
#x=input()
#digit=input()
#contains_digit(x, digit)

def contains_digits(number, digits):
    for index in range (0,len(digits)):
        if str(digits[index]) not in number:
            return False
    return True
    
#number=str(402123)
#digits =[0,3,4]
#print(contains_digits(number,digits))



#math.ceil(x)       // dictonary struct bez podredba


def is_number_balanced(n):
    y=int(n)
    x=math.ceil(y/2)
    print(x)
    sum1=0
    sum2=0
    for index in range (0,x):
        sum1+=int(n[index])
    for index in range (x,len(n)):
        sum2+=int(n[index])
    if (sum1==sum2):
        return True
    else:
        return False

    
x=input()
print(is_number_balanced(x))





'''def balanced(numbers):
    for pivot in range(len(numbers)):
        left_total = sum(numbers[:pivot])
        right_total = sum(numbers[pivot:])
        if left_total == right_total:
            return pivot
    return None
    '''


    
