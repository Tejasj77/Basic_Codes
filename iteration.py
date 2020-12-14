

#if the letter is i or o in the string then capitalize that letter only
# 2 ways to capitaize the letter 


name = str(input("Enter the string "))
new_name = ""
sec_new_name = ""
a=len(name)
for letter in name:
    if letter == "i":
        new_name += letter.upper()
    elif letter == "o":
        new_name += letter.upper()
    else:
        new_name +=letter
        
print(new_name)
        
    
for i in range(0,a):
    if new_name[i] == "i":
        sec_new_name += new_name[i].upper()
    elif new_name[i] == "o":
        sec_new_name += new_name[i].upper()
    else:
        sec_new_name += new_name[i]

print(sec_new_name)
