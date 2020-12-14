
#The problem statement is to identify a version of "(Query no. 25)" in the excel sheet and return the number to the user


import xlwings as xlw

f1 = xlw.Book('Book1.xlsx')
s1 = f1.sheets['Sheet1']
work = []
work1 = ""
col_A = s1.range('A1:A10').value

query = ['Query','query','QUERY']
number = ['Number','NUMBER','no.','number']

#Eliminating all the empty cells in the excel sheet
for i in range(len(col_A)):
    if col_A[i] != None:
        work.append(col_A[i])

#Function to identify whether a character in a string is integer or a character
def is_a_number(char):
    try:
        char = int(char)
        return True
    except:
        return False

#function to convert work list into a string
def function(work):
    str = ""
    for i in work:
        str += i
    return str
print(function(work))
a= function(work)

#We used this logic to check the braces and delete them as we only require the number inside
#using the split function we convert the string again into a iist(we use string first to identify the braces)
if '(' in a:
    b = a.replace('(','')
    if ')' in b:
         c = b.replace(')','')
         c = c.split()
         print(c)

# To chech whether "Query" exists then return the number by incrementing the index
for element in c:
    if element in query:
        print("Query found")
        for element1 in c:
            if element1 in number:
                if is_a_number(element1)== False:
                        print("You were fucking right")
                ant = c.index(element1)                             #returning the index
                ant = ant + 1                                       #incrementing index by 1 to return the index
                                                                     #having the integer.
                print("The query no. is " +c[ant])

# To traverse through the string to check whether a character is integer or string.
for j in c:
    if is_a_number(j) == False:
        print("Not a number" +j)
    else:
        print("It is a number" +j)


