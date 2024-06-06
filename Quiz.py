#Simple Program To Play a Quiz Game Like :(KBC)
#Nested List
Prashna = [

             ["Who coined the term \"cell\" first?", "Robert Hooke", "Lewweenhook", "Kane ", "Aristotle",1],
            #Rs 20,000
             ["Who is known as father of Biology?","Gregor Mendel", "Theophrastus", "Aristotle", "Charles Darwin",3], 
             #Rs 50,000
             ["Who coined the element hydrogen as \"hydrogen\" first?", "Lavoiser", "Chemist", "Kosaile ni diyena afai ayo", "Maile",1], 
             #Rs 1,00,000
             ["Who is the father of modern science?", "Lavoiser", "Chemist", "Albert Eienstein", "Linnaeous",3], 
             #10,00,000
             ["Who is the father of Economics?", "Lavoiser", "Chemist", "Adam Smiths", "Eienstein",3]
            #Rs 1,00,00,000
          
          ] 

#Function
def re_enter():
    while True:
        global name
        name = input("Please enter your username: ")
        if name == "":
            print("Error!! you must enter your username, please re-enter your username: ")
            continue
        else:
            break
re_enter()

print(f"\nWelcome {name} You're playing the one and only NextlvlQUIZ game of the year KBC!!!!!! \n{name} Let's See the Prize chart before enterning into the showdown!\n")

Prize = [ 20000 , 
          50000,
          100000,
          1000000,
          10000000]

#Loop
for i in Prize:
    print (f"{i}\n")

def begin():
    print("Let's Begin\n")

    x = 0

    for x in range(0,len(Prashna)):
        question = Prashna[x][0]
        print(f"\n{x+1}.) The Question for {Prize[x]} is:", question,"\n")
        print(f"1.){Prashna[x][1]}                   2.){Prashna[x][2]}")
        print(f"3.){Prashna[x][3]}                   4.){Prashna[x][4]}\n")
        prizesum = 0

        #Error Handling - Try...Except, Raise Error
        try:
            answer = input("Choose Option From (1-4)")
            
            if answer == "":
                raise Exception("\nInvalid Input Please provide input in numbers(1-4)")
            elif answer != "":
                answer = int(answer)

                if answer == Prashna[x][5]:
                    print(f"\nCongratulations You have Won {Prize[x]}.\n")
                    prizesum = prizesum + Prize[x]
                    quit =input(f"You have won {prizesum}, do you want to play or quit?\n Press Q for Quit And P for playing.")

                    #Break, Pass Statements
                    if quit =="Q":
                        break
                    elif quit == "P":
                        pass
                    else:
                        print("Invalid Input")
                        break
                    
                elif answer != Prashna[x][5]:
                    print(f"\nSorry! You have lost the Quiz.\n")

                    #Global, local variable concept
                    global option
                    option = input("Enter Yes To Play Again And No to Exit!:  ")

                    if option == "Yes":
                        begin()
                    elif option == "No":
                        print(f"As you said {option}, The Game has Ended.\n Thanks For Playing!!! ")
                        break
                    else:
                        print("Invalid Input!\n")
        except Exception as e:
            print(e)
    
    if prizesum > 0:
        print(f"Congratulations For winning the cash prize total of {prizesum}.")

begin()
#End of Program ---- A program written as a practice of python learning. Thank You!