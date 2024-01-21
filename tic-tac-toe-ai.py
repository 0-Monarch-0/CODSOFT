a,b,c,d,e,f,g,h,i="_","_","_","_","_","_","_","_","_"
print(f"{a}"+"|"+f'{b}'+"|"+f"{c}\n"+f"{d}"+"|"+f'{e}'+"|"+f"{f}\n"+f"{g}"+"|"+f'{h}'+"|"+f"{i}\n")
chance = ""
global count


def ai(chance):

    global a,b,c,d,e,f,g,h,i,count

    if(count==0):
        e = chance
        count+=1

    if(count == 2):
        if(a=="O"):
            d=chance
            count+=1
        elif(b=="O"):
            i=chance
            count+=1
        elif(c=="O"):
            h=chance
            count+=1
        elif(d=="O"): 
            a=chance
            count+=1
        elif(f=="O"):
            c=chance
            count+=1
        elif(g=="O"):
            d=chance
            count+=1
        elif(h=="O"):
            g = chance
            count+=1
        elif(i=="O"):
            b=chance
            count+=1 

    if(count == 4):
        if(a=="O" and f=="O" and b=="_" and c=="_" and g=="_" and h=="_" and i=="_" and count == 4):
             b = chance 
             count+=1
        if(a=="O" and f=="_" and (b!="_" and  c!="_" and  g!="_" and  h!="_" and  i!="_") and count == 4):
             f = chance 
             count+=1

        if(b=="O" and a=="O"and d=="_" and f=="_" and g=="_" and h=="_" and c=="_" and  count == 4):
             c=chance 
             count+=1
        if(b=="O" and a=="_"and (d!="_" and  f!="_" and  g!="_" and  h!="_" and  c!="_") and  count == 4):
             a = chance 
             count+=1

        if(c=="O" and b=="O" and a=="_" and d=="_" and f=="_" and g=="_" and i=="_" and count == 4):
             a = chance 
             count+=1
        if(c=="O" and b=="_" and (a!="_" and  d!="_" and  f!="_" and  g!="_" and  i!="_") and count == 4):
             b=chance 
             count+=1

        if(d=="O" and i=="O" and b=="_" and c=="_" and f=="_" and g=="_" and h=="_" and count == 4):
            b=chance 
            count+=1
        if(d=="O" and i=="_" and (b!="_" and  c!="_" and  f!="_" and  g!="_" and  h!="_") and count == 4):
             i=chance 
             count+=1

        if(f=="O" and g=="O" and a=="_" and b=="_" and  d=="_" and h=="_" and i=="_" and count == 4):
            a=chance 
            count+=1
        if(f=="O" and g=="_" and (a!="_" and  b!="_" and   d!="_" and  h!="_" and  i!="_") and count == 4):
             g=chance 
             count+=1

        if(g=="O" and f=="O" and a=="_" and b=="_" and c=="_" and h=="_" and i=="_" and count == 4):
             b = chance 
             count+=1
        if(g=="O" and f=="_" and (a!="_" and  b!="_" and  c!="_" and  h!="_" and  i!="_") and count == 4):
             f=chance 
             count+=1

        if(h=="O" and c=="O" and a=="_" and b=="_" and d=="_" and f=="_" and i=="_" and count == 4):
             a = chance 
             count+=1
        if(h=="O" and c=="_" and (a!="_" and  b!="_" and  d!="_" and  f!="_" and  i!="_") and count == 4):
             c = chance 
             count+=1

        if(i=="O" and h=="O" and a=="_" and c=="_" and d=="_" and f=="_" and g=="_" and count == 4):
             g = chance 
             count+=1
        if(i=="O" and h=="_" and(a!="_" and  c!="_" and  d!="_" and  f!="_" and  g!="_") and count == 4):
             h=chance 
             count+=1

    if(count == 6):
        if(a=="O" and f=="O" and h=="O" and c=="_" and g=="_" and i=="_" and count == 6):
             c = chance
             count+=1
        if(a=="O" and f=="O" and h=="_" and (c!="_" and g!="_" and i!="_") and count == 6):
             h = chance
             count+=1

        if(b=="O" and a=="O" and g=="O" and d=="_" and f=="_" and h=="_" and  count == 6):
             f=chance
             count+=1
        if(b=="O" and a=="O" and g=="_" and (h!="_" and  f!="_" and  d!="_") and count == 6):
             g = chance 
             count+=1

        if(c=="O" and b=="O" and i=="O" and g=="_" and f=="_" and d=="_" and count == 6):
             f = chance
             count+=1
        if(c=="O" and b=="O" and i=="_" and (g!="_" and  f!="_" and  d!="_") and count == 6):
             i=chance
             count+=1

        if(d=="O" and i=="O" and g=="O" and b=="_" and h=="_" and f=="_" and count == 6):
             b=chance
             count+=1
        if(d=="O" and i=="O" and g=="_" and (b!="_" and  f!="_" and  h!="_") and count == 6):
             g=chance
             count+=1

        if(f=="O" and g=="O" and i =="O" and b=="_" and d=="_" and h=="_" and count == 6):
             b=chance
             count+=1
        if(f=="O" and g=="O" and i =="_" and (b!="_" and  h!="_" and  d!="_") and count == 6):
             i=chance
             count+=1

        if(g=="O" and f=="O" and h=="O" and a=="_" and c=="_" and i=="_" and count == 6):
             i = chance
             count+=1
        if(g=="O" and f=="O" and h=="_" and (a!="_" and  c!="_" and  i!="_") and count == 6):
             h=chance
             count+=1

        if(h=="O" and c=="O" and i=="O" and b=="_" and f=="_" and d=="_" and count == 6):
             d = chance
             count+=1
        if(h=="O" and c=="O" and i=="_" and (b!="_" and  f!="_" and  d!="_") and count == 6):
             i = chance
             count+=1

        if(i=="O" and h=="O" and c=="O" and a=="_" and f=="_" and d=="_" and count == 6):
             f = chance
             count+=1
        if(i=="O" and h=="O" and c=="_" and (a!="_" and  f!="_" and  d!="_") and count == 6):
             c=chance
             count+=1

    if (count==8):
        if(a=="O" and f=="O" and h=="O" and g=="O" and i=="_" and count ==8):
            i = chance
            count+=1
        if(a=="O" and f=="O" and h=="O" and g=="_" and i!="_" and count ==8):
            g = chance
            count+=1

        if(b=="O" and a=="O" and g=="O" and f=="_" and h=="_" and d=="_" and count == 6):
             f=chance
             count+=1
        if(b=="O" and a=="O" and f=="O" and d=="_" and g=="_" and h=="_" and count == 6):
             g = chance 
             count+=1

        if(c=="O" and b=="O" and i=="O" and d=="O" and g=="_" and count ==8):
            g = chance
            count+=1
        if(c=="O" and b=="O" and i=="O" and d=="_" and g!="_" and count ==8):
            d=chance
            count+=1

        if(d=="O" and i=="O" and g=="O" and b=="_" and h=="_" and f=="_" and count == 6):
             b=chance
             count+=1
        if(d=="O" and i=="O" and b=="O" and g=="_"  and h=="_" and f=="_" and count == 6):
             g=chance
             count+=1 

        if(f=="O" and g=="O" and i =="O" and b=="_" and d=="_" and h=="_" and count == 6):
             b=chance
             count+=1
        if(f=="O" and g=="O" and b=="O" and i =="O" and d=="_" and h=="_" and count == 6):
             i=chance
             count+=1

        if(g=="O" and f=="O" and h=="O" and a=="O" and c=="_" and count ==8):
            c = chance
            count+=1
        if(g=="O" and f=="O" and h=="O" and a=="O" and c!="_" and count ==8):
            a=chance
            count+=1

        if(h=="O" and c=="O" and i=="O" and b=="_" and f=="_" and d=="_" and count == 6):
             d = chance
             count+=1
        if(h=="O" and c=="O" and d=="O" and i=="_" and f=="_" and b=="_" and count == 6):
             i = chance
             count+=1

        if(i=="O" and h=="O" and c=="O" and d=="O" and a=="_" and count ==8):
            a = chance
            count+=1
        if(i=="O" and h=="O" and c=="O" and d=="O" and a!="_" and count ==8):
            d=chance
            count+=1        
    print(f"{a}"+"|"+f'{b}'+"|"+f"{c}\n"+f"{d}"+"|"+f'{e}'+"|"+f"{f}\n"+f"{g}"+"|"+f'{h}'+"|"+f"{i}\n")


def check():

    global a,b,c,d,e,f,g,h,i
    if (a==b and b==c and (a and b and c !="_")):
        print(a+" Wins")
        return True
    elif (d==e and e==f and (d and e and f !="_")):
        print(d+" Wins")
        return True
    elif (g==h and h==i and (g and h and i !="_")):
        print(g+" Wins")
        return True
    elif (a==d and d==g and (a and d and g !="_")):
        print(a+" Wins")
        return True
    elif (b==e and e==h and (e and b and h !="_")):
        print(b+" Wins")
        return True
    elif (c==f and f==i and (c and f and i !="_")):
        print(c+" Wins")
        return True
    elif (a==e and e==i and (a and e and i !="_")):
        print(a+" Wins")
        return True
    elif (c==e and e==g and (c and e and g !="_")):
        print(c+" Wins")
        return True
    else:
        return False
    

def table(row,column,chance):
    global a,b,c,d,e,f,g,h,i,count
    if (row == 1 and column == 1 and a == "_"):
        a = chance
    elif(row ==1 and column == 2 and b == "_"):
        b = chance
    elif(row ==1 and column == 3 and c == "_"):
        c = chance
    elif(row ==2 and column == 1 and d == "_"):
        d = chance
    elif(row ==2 and column == 2 and e == "_"):
        e = chance
    elif(row ==2 and column == 3 and f == "_"):
        f = chance
    elif(row ==3 and column == 1 and g == "_"):
        g = chance
    elif(row ==3 and column == 2 and h == "_"):
        h = chance
    elif(row ==3 and column == 3 and i == "_"):
        i = chance
    else:
        print("already taken!!!")
        count -= 1
    print(f"{a}"+"|"+f'{b}'+"|"+f"{c}\n"+f"{d}"+"|"+f'{e}'+"|"+f"{f}\n"+f"{g}"+"|"+f'{h}'+"|"+f"{i}\n") 



print("Think this as the 3x3 matrix.")
count = 0
while(True):
    if (count%2 == 1):
        print("Turn:O")
        user_input_row=int(input("enter row:"))
        user_input_column=int(input("entre the column:"))
        count+=1
        table(user_input_row,user_input_column,"O")
        if(check()):
            break
        if count == 9:
            print("tie")
            break
    elif(count%2 == 0):
        ai("X")
        if(check()):
            break
        if count == 9:
            print("tie")
            break
    else:
        print("Game Over")




