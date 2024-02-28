def main():
    # Taking input for name
    name = input("Enter your name: ")

    # Taking input for age
    age = input("Enter your age: ")

    cont = True
    while cont == True:
        age = input("Enter your age: ")
        if not age.isdigit():
            print("Write a number for your age instead of a word")
        else: cont = False

    # Printing name and age
    print("Your name is:", name)
    print("Your age is:", int(age))

if __name__ == "__main__":
    main()
