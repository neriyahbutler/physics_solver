p1_equation = open("p1equations.txt","r")
p2_equation = open("p2equations.txt","r")
var_lst = ["v", "v0", "a", "t", "F", "nF", "x", "x0","p","m","V","P","P0","g","h","Fb","A0","A","W","v2"]

def boot_up():

    print("===============================================================================================================================================================")
    print ("Welcome to my program!".center(120," "))
    print("===============================================================================================================================================================\n")

def take_choice():
    while 1==1:
        choice = input("Which course would you like to choose, Physics 1 or Physics 2\n")
        if choice == "Physics 1" or choice == "Physics 2": break
        else:   print("Invalid input, please enter one of the valid choices.")
    return choice

def iterate_equations(choice): #This code receives the input
    if choice == "Physics 1":
        line = p1_equation.readline() #Reads through the file that contains the equations for Physics 1
        strng = ""
        lst = []
        for char in line: #Adds all the characters for the equation into a string variable until it comes across a comma, which symbolizes the end of the equation
            if char != ",": strng += char
            else:
                eq_stng = strng.split("=") #Seperates the variable you solve for with the equation you use to solve for it
                lst.append(eq_stng)
                strng = ""
        solve_var_lst = []
        for x in range(len(lst)): solve_var_lst.append(lst[x][0])
        #Returns each of the sublists for each equation in one whole list along with another list containing the variables you solve for
    else:
        line_p2 = p2_equation.readline()
        strng = ""
        lst = []
        for char in line_p2:
            if char != ",": strng += char
            else:
                eq_stng = strng.split("=")
                lst.append(eq_stng)
                strng = ""
            solve_var_lst = []
            for x in range(len(lst)): solve_var_lst.append(lst[x][0])
    return lst, solve_var_lst

def solve_variable(choice):
    lst, solve_v_lst = iterate_equations(choice)
    new = []
    dict = {}
    checked = []
    while True:
        variable_choice = input("What variable do you want to solve for?\n")
        if variable_choice not in solve_v_lst:#(variable_choice>="a" and variable_choice<="z"):
            print("Invalid input has been recieved, please try again.")
        else:
            #print("Variable is in the list")
            for y in range(len(solve_v_lst)):
                if variable_choice == solve_v_lst[y]:
                    new = lst[y]
                    #print("This is the variable, 'lst', " + str(lst))
                    print("Program being used is:",new[1])
            break
    strng2 = ''
    prev = ''
    num_l = ['1','2','3','4','5','6','7','8','9'] #This checks to see if there are numbers or not that are picked up in the loop. If they are picked up, the int is skipped so the code doesn't ask for the input of a regular number, like "2"
    for z in (new[1]):
        if z != "+" and z != "-" and z != "*" and z != "/" and z != "(" and z != ")" and z not in num_l:
            strng2 += z
            prev = strng2
            if len(new[1]) == (new[1].index(strng2)+1) and strng2 in var_lst and strng2 not in checked:
                inpt = float(input(
                    "Enter variable number for " + strng2 + ": "))  # PROBLEM the code isn't taking "v0"s and other initial values. I need to figure out a way to fix this. Perhaps I can make an empty string that just adds characters until the funciton runs into a variable that isn't allowed or something...
                dict[strng2] = inpt
                checked.append(prev)
                strng2 = ''
        else:
            #print(strng2)
            if strng2 in var_lst and strng2 not in checked: #Goes through the variables in the equation and sets a value for it
                inpt = float(input("Enter variable number for " + strng2 + ": "))#PROBLEM the code isn't taking "v0"s and other initial values. I need to figure out a way to fix this. Perhaps I can make an empty string that just adds characters until the funciton runs into a variable that isn't allowed or something...
                dict[strng2] = inpt
                checked.append(prev)
                strng2 = ''
            else:
                strng2 = ""
    return dict, new

def get_answer(dict, lst):
    eq_stng = ''
    curr_var = ''
    num_l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in lst[1]:
        if char != "+" and char != "-" and char != "*" and char != "/" and char != "(" and char != ")" and char not in num_l:
            curr_var += char
            #print(curr_var)
            if len(lst[1]) == (lst[1].index(curr_var) + 1):
                eq_stng += str(dict[curr_var])
        else:
            if curr_var in dict:
                eq_stng += str(dict[curr_var])
                curr_var = ''
            eq_stng += char
    solved_eq = eval(eq_stng)
    print(float(solved_eq))

boot_up()
x = take_choice()
y, z = solve_variable(x)
get_answer(y, z)