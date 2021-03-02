import shutil
import os


def main():
    txtBaseFilePath = []  # Stores base folder text files address
    txtFile = []  # Stores base folder text file names
    txtDestFilePath = []  # Stores destination folder text files address
    Source_path = "D:/sai"
    for root, dirs, files in os.walk(Source_path):
        for file in files:
            if file.endswith(".txt"):  # Selecting the type of file
                print(file)  # Printing all files(considering type)
                txtFile.append(file)  # Storing all the text file names
                print(os.path.join(root, file))  # Prints path of the selected files
                txtBaseFilePath.append(os.path.join(root, file))  # Storing selected base path file address
    for i in range(0, len(txtFile)):
        print(i, txtFile[i])  # Printing selected files with serial number
    select = int(input("Select the number of files user want to copy "))
    selectedfiles = []  # Stores file numbers which needs to be copied
    for i in range(0, select):
        selectedfiles.append(int(input("Enter file number ")))  # Storing file serial numbers
    for i in range(0, len(selectedfiles)):
        txtDestFilePath.append(raw_input("Enter the destination path name "))  # Providing destination path
        if not os.path.exists(txtDestFilePath[i]):
            os.makedirs(txtDestFilePath[i])  # creating destination directory if not created
            print(txtDestFilePath)
    for i in range(0, len(selectedfiles)):
        shutil.copy(txtBaseFilePath[selectedfiles[i]], txtDestFilePath[i])  # copying process from source to dest
    print("Copying is Done")


if __name__ == "__main__":
    main()
