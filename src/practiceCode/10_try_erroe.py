try:
    # risky code here
    x = int(input("Enter a number: "))
    y = 10 / x
except Exception as e:
    print(f"An unknown error occurred: {e}")