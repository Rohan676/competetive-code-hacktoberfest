# finding palindrome of a number i.e, reverse of a number


def palindrome(n):
    num=0
    while(n>0):
        rem=n%10
        num=(10*num)+rem
        n//=10
    return num


number=int(input("Enter a number whose palindrome is required :- "))
reverse=palindrome(number)
print("The palindrome of {0} is {1} .".format(number,reverse))
