# import flask
def main():
        name = input("Enter your name: ")
        agey = int(input("Enter your age: "))
        return "Hello " + name + " " + str(agey)
if __name__ == "__main__":
        print(main())