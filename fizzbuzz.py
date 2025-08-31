# lets make a fizzbuzz program, for numbers divisible by 3 print fizz, for numbers divisible by 5 print buzz, for numbers divisible by both 3 and 5 print fizzbuzz, for all other numbers print the number itself

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

def main():
    
    n = int(input("Enter a number: "))
    fizzbuzz(n)
    print("Done")

main()