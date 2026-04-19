# import flask
def main():
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        return "Hello " + name + " " + str(age)
if __name__ == "__main__":
        print(main())