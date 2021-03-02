import shutil
import os
from pathlib import Path


def main():
    txtBaseFilePath = []  # Stores base folder text files adrress
    txtFile = []  # Stores base folder text file names
    txtDestFilePath = []  # Stores dest folder text files adrress
    Source_path = "D:\sai"
    source = Path('D:\sai')
    for root, dirs, files in os.walk(Source_path):
        for file in files:
            if file.endswith(".txt"):  # Selecting the type of file
                txtFile.append(file)  # Storing all the text file names

    pattren = "*txt"
    for j in source.glob(pattren):
        print(j)
        txtBaseFilePath.append(j)

    for i in range(0, len(txtFile)):
        print(i, txtFile[i])  # Printing selected files with serial number
    select = int(input("Select the number of files user want to copy "))
    selectedfiles = []  # Stores file numbers which needs to be copied
    for i in range(0, select):
        selectedfiles.append(int(input("Enter file number ")))  # Storing file serial numbers
    for i in range(0, len(selectedfiles)):
        txtDestFilePath.append(input("Enter the dest path name "))  # Providing destination path
        if Path(txtDestFilePath[i]).is_dir():
            print()
        else:
            Path(txtDestFilePath[i]).mkdir(parents=True, exist_ok=False)
    for i in range(0, len(selectedfiles)):
        shutil.copy(txtBaseFilePath[selectedfiles[i]], txtDestFilePath[i])  # copying process from source to dest
    print("Copying is Done")


if __name__ == "__main__":
    main()
'''
txtfile = [.txt(0), .txt(1)......]
txtBaseFilePath = [pathoftxtfile(0), pathoftxtfile(0).....]
selectedfiles = [0(0), 1(1) ......]
txtDestFilePath = [pathbyuser(0), pathbyuser(1)...]


'''