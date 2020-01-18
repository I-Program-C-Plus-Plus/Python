import glob
import os
import getpass
import sys

def main():
    os.system("color 1f")
    os.chdir("C:\\Users")
    os.chdir(getpass.getuser())
    print(os.getcwd(),'\n')
    while True:
        try:
            type = (str(input("Find a file by \"type\" or by \"name\": ")))

            def typeEntered():
                global type
                amount_of_files = 0
                directory = (str(input("\nEnter directory to search: ")))
                if(directory == "skip"):
                    None
                else:
                    os.chdir(directory)
                print('\n',os.getcwd(),'\n')
                typeOfFile = (str(input("\nEnter the type of file you want to search by: ")))
                for i in glob.glob("*.{}".format(typeOfFile)):
                    amount_of_files += 1
                    if(amount_of_files < 1):
                        print("No files with type of {} in directory {}".format(typeOfFile,directory))
                    else:
                        print('\n',i,'\n')
                print("\nAmount of Files with type {} in directory {}: ".format(typeOfFile,directory),amount_of_files,'\n')
                amount_of_files = 0

            def nameEntered():
                global type
                amount_of_files = 0
                directory = (str(input("\nEnter directory to search: ")))
                if(directory == "skip"):
                    None
                else:
                    os.chdir(directory)
                print('\n',os.getcwd(),'\n')
                nameOfFile = (str(input("\nEnter the name of file you want to search for: ")))
                for i in glob.glob("{}.*".format(nameOfFile)):
                    amount_of_files += 1
                    if(amount_of_files < 1):
                        print("No files named {} in directory {}".format(nameOfFile,directory))
                    else:
                        print('\n',i,'\n')
                print("\nAmount of files with name {} in directory {}: ".format(nameOfFile,directory),amount_of_files,'\n')
                amount_of_files = 0

            if(type == "type"):
                typeEntered()

            elif(type == "name"):
                nameEntered()

            elif(type == "EXIT"):
                sys.exit(0)

            elif(type == "clear"):
                os.system("cls")

            else:
                print("Uh oh! \nUnrecognized command -> {}\n".format(type))

        except Exception as e:
            print(str(e))



if __name__ == '__main__':
    main()
