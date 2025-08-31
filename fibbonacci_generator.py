# program to generate fibonacci series for n number of terms

def fibonacci(n):
    
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)

    for i in range(n):
        nth = n1 + n2
        print(nth)
        n1 = n2
        n2 = nth

def main():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, ":")
        print(0)
    else:
        print("Fibonacci sequence:")
        fibonacci(n-2)  # Subtracting 2 because first two terms are already printed

main()

