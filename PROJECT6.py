a=1
def Valut_Lite() :
    print("="*4,end="")
    print("Valut Lite",end="")
    print("="*4)
    print(f"{1}. View Credentials")
    print(f"{2}.Add Credential")
    print(f"{3}.Update Credentials")
    print(f"{4}.Exit")
    Choice=int(input("Enter Choice(1-4): "))
    globals()[f"CHOICE{Choice}"]()
    return



def CHOICE1()  :
    print("Saved Credentials:")
    with open("File,txt","r") as f:
        data=f.readlines()
        for lines in data :
            parts=lines.strip().split("@")
            parts[-1]="****"
            print("@".join(parts))
    Valut_Lite()
    return

def CHOICE2() :
    global a
    print("Add Credential")
    Web=input("Website: ").strip()
    User=input("Username: ").strip()
    Pass=input("Passwprd: ")
    d ="{User}@{Web}@{Pass}\n"
    with open("File,txt","a") as f:
        f.write(f"{a}.{d}")
    print('Add credential Successfully')
    a+=1
    Valut_Lite()
    return

def CHOICE3() :
    with open("File.txt", "r") as f:
        lines = f.readlines()
    print("Saved Credentials:")
    for line in lines:
        parts = line.strip().split("@")
        parts[-1] = "****"
        print("@".join(parts))
    select = input("\nEnter Number To Update Password: ")
    new_pass = input("Enter New Password: ").strip()
    for index, line in enumerate(lines):
        if line.startswith(select + "."):
            parts = line.strip().split("@")
            parts[-1] = new_pass          # 🔑 ONLY password update
            lines[index] = "@".join(parts) + "\n"
    with open("File.txt", "w") as f:
        f.writelines(lines)

    print("Password Updated Successfully")
    Valut_Lite()
    return

def CHOICE4() :
    print('Exiting Valut Lite')
    exit()
    return


def initial() :
    global a
    print("Creating First Account")
    Web=input("Website: ").strip()
    User=input("Username: ").strip()
    Pass=input("Password: ") 
    d=f"{User}@{Web}@{Pass}\n"
    with open("File,txt","a") as f:
        f.write(f"{a}.{d}")
    a+=1
    print("Credential Save Successfully:\n")
    return  

initial()
Valut_Lite()
    
