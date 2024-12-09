import os 

folders=input("Enter the folder names in spaces between them: ").split()

for folder in folders:
    try:
          files=os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name: "+folder)
        break
    
    print("===The files in "+folder+" are: ")

    for file in files:
        print("The file name in "+folder+" is: ",file)
