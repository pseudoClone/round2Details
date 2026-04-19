import flask
def main():
        name = input("Enter your name: ")
        return "Hello " + name
if __name__ == "__main__":
        print(main())