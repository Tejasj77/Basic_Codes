print("\n\tWelcome to the Digital Fortress\n")

nouse=input("\nTo enter the fort I should know your name ")


print("\nBollocks!!!!!!!\n")
print ("\n I am an advanced piece of encryption machine\n")
print ("\nThis is going to be challenging.To go ahead answer a question for me\n")
answer=input("What language I might be coded in?")
#proceed=="python"
if answer=="python":
        print ("Wow you got that right")
        print ("\nAs the name suggests it is a fortress.\nTO GET IN YOU HAVE TO GO THROUGH ME.")
        ans=input('\npress y if you accept the challenge')
        if ans=='y':
                print ("\nI am an advanced piece of software.TO GAIN ACCESS YOU HAVE TO UPSCALE YOUR LANGUAUGE UPTO MINE.LET ME SHOW YOU")
                timepass=input('Enter your name')
                length=len(timepass)
                
                for i in range(0,length):
                    encrypt=ord(timepass[i])
                    decrypt=encrypt+1
                    decode=chr(decrypt)
                    print(decode)
                print ("\nSo this is what I read.In technical terms this is what is called as a CIPHER")
                isthis=input('\nIs this your name?.Press N if not otherwise press Y')
                if isthis=='N':
                        print ("\nLet me make it easy for you")
                        print (" \nutkarsha is accepted as \nv\nu\nl\nb\ns\nt\ni\nb\n")
                        encrypt=0
                        decrypt=0
                        timepass2=input('\nYou wanna try again.See the decryption of')
                        length=len(timepass2)
                        for i in range(0,length):
                                 encrypt=ord(timepass2[i])
                                 decrypt=encrypt-1
                                 decode=chr(decrypt)
                                 print(decode)
#LEVEL 1 completed
                                 
                        encrypt=0;
                        decrypt=0;
                        print ("\nSeems like you are getting the hang of it.Let's level up shall we?")
                        print ("\nYou might have heard the name of ceaser cipher")
                        timepass3=input("Write anything that comes to your mind.I'll encrypt it for you.IF YOU CAN")
                                
                        length=len(timepass3)
                        for i in range(0,length):
                                 encrypt=ord(timepass3[i])
                                 decrypt=encrypt+3
                                 decode=chr(decrypt)
                                 print(decode)
                        timepass4=input('See the decryption of ')
                        length=len(timepass4)
                        for i in range(0,length):
                                 encrypt=ord(timepass4[i])
                                 decrypt=encrypt-3
                                 decode=chr(decrypt)
                                 print(decode)
                        
                        print ("\n This might be the hardest encryption")
                        lastcall1=[]
                        lastcall2=[]
                        lastcall=input("\nEnter anything")
                        lastcall3=input("\nEnter the cipher that you might think is correct")
                        decode1=[]
                        length=len(lastcall)
                        for i in range(0,length):
                                 a=lastcall[i]
                                 lastcall1.append(a)
                                 encrypt=ord(lastcall[i])
                                
                                 decrypt=encrypt+i
                                 x=chr(decrypt)
                                 decode1.append(x)
                        length1=len(lastcall3)
                        for i in range(0,length1):
                                 b=lastcall3[i]
                                 lastcall2.append(b)
                                 
                       
                        #print lastcall2
                       # print lastcall1
                        #print(decode1)
                        print ("\nIf both are answers match i.e you get the cipher right YOU WIN")
                        sampla=input("Are you ready")
                        a=lastcall2
                        b=decode1
                        if a==b:
                                print("\n YOU WIN")
                        else:
                                print("\n YOU LOST")
                       
                        print ("The cipher is")
                        print(decode1)
                                            
                        
                       
else:
    print ("Man,this ended quickly.You are banned from entering the fortress.Thank you")
