# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters

street_name = "MGRoad"
print(street_name)
print(street_name[0])
print(street_name[2])
print(street_name[4])


# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else

team_name = str(input('Enter the team name'));

if(team_name[1] == 'i' or team_name[1] == 'o' or team_name[1] == 'u'):
    print("YOU WERE DAMN RIGHT")
else :
    print("YOU WERE DAMN WRONG")

student_name = "Tejas"
print(student_name[-1])

student_name = str(input("Enter the name to be analysed"))
end_letter = student_name[-1]

print(student_name, " ends with " , "'" + end_letter + "'")


#length of string

street_name = str(input("Enter the name"))
a = len(street_name)

print("Size of string " , a)
count = 0
for i in range(0,len(street_name)):
    if(street_name[i] == 'f'):
        count+=1
    
    
print(count)
print('f exists ',count,'times')    
if(count==0):
    print("Did not find")


