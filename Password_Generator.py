#PASSWORD GENERATOR
#==================

#IMPORTS
import string, random, os

#DECLARE
strChars = string.ascii_letters
strNumbers = string.digits
strSpecial = string.punctuation
strCustom = ""
pass_length = 8
pass_create = 10
bChars = True
bNumbers = True
bSpecials = True
strCurrent = strChars + strNumbers + strSpecial + strCustom

#FUNCTIONS
def Wait_Key():
    try:
        input("Press Enter to continue...")
    except:
        pass

def Screen_Clear():
    #import os
    #print("\033c") #Clear terminal screen (Another way)

    if os.name == 'nt': os.system('cls')   #Windows
    if os.name == 'posix': os.system('clear')  #Linux, Mac

def String_Shuffle(strSource):
    #Another
    #return ''.join(random.sample(strSource,len(strSource)))

    str_var = list(strSource)
    random.shuffle(str_var)
    return ''.join(str_var)

def Password_Generator (strSource, intLength, intNumber):
    for create_number in range(0, intNumber):
        print (''.join(random.choice(strSource) for i in range(intLength)))

def Show_Settings():
    KeepRunning = True
    global bChars
    global bNumbers
    global bSpecials
    global strCustom
    global pass_create
    global pass_length
    global strCurrent
    bC = bChars
    bN = bNumbers
    bS = bSpecials
    sC = strCustom
    PC = pass_create
    PL = pass_length
    while KeepRunning == True:
        Screen_Clear()
        print ("============================")
        print ("=         Settings         =")
        print ("============================")
        print ("")
        print (" 1. Letters [" + str(bC) + "]")
        print (" 2. Numbers [" + str(bN) + "]")
        print (" 3. Special [" + str(bS) + "]")
        print (" 4. Custom  [" + sC + "]")
        print (" 5. Password Length  [" + str(PL) + "]")
        print (" 6. Password Generation  [" + str(PC) + "]")
        print (" 7. Ok")
        print (" 8. Cancel")
        print ("")
        print ("============================")
        Mode = input("Choose: ")
        print ("")

        if (Mode == "1"):
            bC = not bC
        elif (Mode == "2"):
            bN = not bN
        elif (Mode == "3"):
            bS = not bS
        elif (Mode == "4"):
            try:
                sC = input("Write the chars, that you want to use: ")
            except:
                print("Please type something!!!")
                Wait_Key()
        elif (Mode == "5"):
            try:
                PL = int(input("Password length: "))
            except:
                print("Please type a number!!!")
                Wait_Key()
        elif (Mode == "6"):
            try:
                PC = int(input("How many passwords to create: "))
            except:
                print("Please type a number!!!")
                Wait_Key()
        elif (Mode == "7"):
            bChars = bC
            bNumbers = bN
            bSpecials = bS
            strCustom = sC
            pass_create = PC
            pass_length = PL
            strCurrent = ""
            if bChars == True: strCurrent += strChars
            if bNumbers == True: strCurrent += strNumbers
            if bSpecials == True: strCurrent += strSpecial
            strCurrent += strCustom
            KeepRunning = False
            break
        elif (Mode == "8"):
            KeepRunning = False
            break
        else:
            print ("Please choose one of the above choices!")
            Wait_Key()

#PROGRAM
Mode = ""
while Mode != "4":
    Screen_Clear()
    print ("======================================")
    print ("=         Password Generator         =")
    print ("======================================")
    print ("=                                    =")
    print ("= 1. Generate password               =")
    print ("= 2. Settings                        =")
    print ("= 3. About                           =")
    print ("= 4. Quit                            =")
    print ("=                                    =")
    print ("======================================")
    Mode = input("Choose: ")

    if (Mode == "1"):
        Screen_Clear()
        print ("======================================")
        Password_Generator(String_Shuffle(strCurrent),pass_length,pass_create)
        print ("======================================")
        Wait_Key()
    elif (Mode == "2"):
        Show_Settings()
    elif (Mode == "3"):
        Screen_Clear()
        print ("======================================")
        print ("=    Password Generator by AlDim     =")
        print ("=           Version 0.2              =")
        print ("======================================")
        Wait_Key()
    elif (Mode == "4"):
        print("Thank you for using me :)")
        break
    else:
        print ("Please choose one of the above choices!")
        Wait_Key()
