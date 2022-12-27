# We all have played  snake , water , gun game in our childhood. if you haven't, google the rules of  this game and write a python program capable of playing thiss game with the user.

import random
print(f'''
{"*"*48}
This is Stone, Paper , Scissors Game by Shubham.
{"*"*48}

''')
Pc=random.randint(1,3)
print("********* Start your game, all the best *********** \n")

def game(PC,You):
    if (PC=="Stone" and You=="Paper") or (PC=="Paper" and You=="Scissor") or ( PC=="Scissor" and You=="Stone"):
        print("Result:- ")
        print('''
        *         *  * * * * *   *      *
         *   *   *       *       *  *   *
          *  *  *        *       *    * * 
           *   *     * * * * *   *      *
        ''')
    elif (PC=="Stone" and You=="Scissor") or (PC=="Paper" and You=="Stone") or (PC=="Scissor" and You=="Paper"):
        print("Result:- ")
        print('''
        *          *       * * * * *  * * * * *
        *        *    *    *          * 
        *      *        *  * * * * *  * * * * * 
        *         *   *            *  * 
        * * * *     *      * * * * *  * * * * * 
         ''')
    else:
        print("Result:- ")
        print('''
        *       *      *      *       *  * * * * *
        * *     *    *   *    * *     *  * 
        *   *   *  *       *  *   *   *  * * * * *
        *     * *    *   *    *     * *  *
        *       *      *      *       *  * * * * * 
         ''')
    
for i in range(0,6):
    You=int(input("Choose $Stone(1) $Paper(2) $Scissor(3) $exit(0): ") )
    if(You==0):
        print("Game exited")
        break
    if Pc==1:
        Pc="Stone"
    elif Pc==2:
        Pc="Paper"
    elif Pc==3:
        Pc="Scissor"

    if You==1:
        You="Stone"
    elif You==2:
        You="Paper"
    elif You==3:
        You="Scissor" 


    print(f'''   ------Choices-------
$Computer:{Pc}  $You:{You} ''')  
    game(Pc,You)