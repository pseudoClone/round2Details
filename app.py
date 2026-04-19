# import flask
def main():
        name = input("Enter your name: ")
        agex = int(input("Enter your age: "))
        return "Hello " + name + " " + str(agex)
if __name__ == "__main__":
        print(main())