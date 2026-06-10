def txt_file_handle():
    x=int(input("enter your choice 1 to enter the program:"))
    while x==1:
            print("select 1 to read your file","\n"
              ",select 2 to write your file,","\n"
              "select 3 to append your fil","\n"
              "select 4 to display your number of line,","\n"
              "select 5 to display your searched word,","\n"
              "select 6 to exit the program")
            choice=int(input("enter your choice"))
            F = input("enter your file name:")
            if choice==1:
                try:
                    file=open(F,"r")
                    lines = file.readlines()
                    print(lines)
                except FileNotFoundError:
                    print("file not exist")
                    print("please make a file")
            elif choice==2:
                try:
                    text=input("Enter text to write: ")
                    file=open(F,"w")
                    file.write(text)
                    print("file saved successfully")
                except :
                    print("error")
            elif choice==3:
                try:
                    file=open(F,"a")
                    text=input("Enter text to write: ")
                    file.write(text)
                    print("file appended successfully")
                except FileNotFoundError:
                    print("file not exist")
                    print("please make a file")
            elif choice==4:
                try:
                    with open(F, "r") as file:
                        line_count=0
                        for l in file:
                            line_count+= 1
                        print("Number of lines:", line_count)
                except FileNotFoundError:
                    print("file not exist")
                    print("please make a file")
            elif choice==5:
                try:
                    word_to_search = input("enter your searched word:")
                    count = 0
                    with open(F, "r") as file:
                        for line in file:
                            words = line.lower().split()
                            count += words.count(word_to_search.lower())
                    print(f"The word '{word_to_search}' appears {count} times in the file.")
                except FileNotFoundError:
                    print("file not exist")
                    print("please make a file")
            elif choice==6:
                 print("Thank you for using this program")
                 break
            else:
                print("please choose the correct option")
                continue

print("file handeling")
txt_file_handle()
