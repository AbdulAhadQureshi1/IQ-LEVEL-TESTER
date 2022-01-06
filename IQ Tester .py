import random

score = 0
again = "Y"

def results(n):
    print("Your Score: \t", n)
    if n >= 3:
        print("Your IQ Level: \t Genius!")
    elif n == 3:
        print("Your IQ Level: \t Above Average IQ")
    elif 2 <= n < 3:
        print("Your IQ Level: \t Average")
    elif n < 2:
        print("Your IQ Level: \t Below Average")
        
def validate (ans):
    global score
    guess = input("Your Answer: \t").upper()
    if guess == "break": return True
    if guess == 'A' or guess == 'C' or guess != 'D' or guess == 'B':
        if guess == ans:
            score += 1
    else:
        print(">>>>Error! Make sure to give input \"A B C D\" or \"break\". Your mark for this question is deducted! Make sure not to repeat this mistake!<<<<")
#==================================================================MAIN PROGRAM=================================================================
while again == 'Y':
    print("            ============================================================IQ LEVEL ESTIMATION PROGRAM=================================================================")
    print("      ===================This program will ask you different question and tell your estimated IQ level based on your answers to the questions!============================")
    print("=================>>>>>>> Type \"break\" to end the program and get your results. Else program will automatically end once questions are finished! <<<<<<<<<=====================")
    q = random.sample(range(10),5)
    score = 0
    q_num = 0
    for i in q:
        q_num += 1
        if i == 0: #64
            print("\n Question # ",q_num, end="\t")
            print('''
            Complete the series: 1, 1, 4, 8, 9, 27, 16, ?
        *OPTIONS*    
            A. 32       B. 64       C. 81       D. 256
            ''')
            if validate ("B"): break
        elif i == 1: #D
            print("\n Question # ",q_num, end="\t")
            print('''
            Find the answer that best completes the analogy:
                Book is to Reading as Fork is to:
        *OPTIONS*:
            A. drawing      B. writing      C. stirring     D. eating
            ''')
            if validate ("D"): break
        elif i == 2: #C
            print("\n Question # ",q_num, end="\t")
            print('''
            Find two words, one from each group, that are the closest in meaning:
            -Group A
                talkative, job, ecstatic
            -Group B
                angry, wind, loquacious
        *OPTIONS*:
            A. talkative and wind           B. job and angry
            C. talkative and loquacious     D. ecstatic and angry
            ''')
            if validate ("C"): break
        elif i == 3: #C
            print("\n Question # ",q_num, end="\t")
            print('''
            Which of the following can be arranged into a 5-letter English word?
            1. H R G S T    2. R I L S A    3. T O O M T    4. W Q R G S
        *OPTIONS*:
            A. 1 and 2      B. 1 and 4      C. 2 and 3      D. 2 and 4
            ''')
            if validate ("C"): break
        elif i == 4: #5
            print("\n Question # ",q_num, end="\t")
            print('''
            What number best completes the analogy:
                            8:4 as 10:
        *OPTIONS*:
            A. 3        B. 7        C. 24        D. 5
            ''')
            if validate ("D"): break
        elif i == 5:  #Blood
            print("\n Question # ",q_num, end="\t")
            print('''
            Green is to grass as red is to?
        *OPTIONS*:
            A. Blood        B. Rose     C. Carpet       D. None
            ''')
            if validate ("A"): break
        elif i == 6: #C
            print("\n Question # ",q_num, end="\t")
            print('''
            A,B,C,D,E are all facing north. If A is in front of B, B is west to C,D is south of C and E is on left of D. Which letter is northeast to the letter left to D?
        *OPTIONS*:
            A. A        B. B        C. C        D. D
            ''')
            if validate ("C"): break
        elif i == 7: #B
            print("\n Question # ",q_num, end="\t")
            print('''
            In a certain case GIGANTIC is written as GIGTANCI. How is MIRACLES written in that code?
        *OPTIONS*:
            A. MIRLCAES     B. MIRLACSE     C. RIMCALSE     D. RIMLCAES
            ''')
            if validate ("B"): break
        elif i == 8: #Friday
            print("\n Question # ",q_num, end="\t")
            print('''
            If it would be Thursday two days after tomorrow, what was two days before yesterday?
        *OPTIONS*:
            A. Monday       B. Friday       C. Saturday         D. Sunday
            ''')
            if validate ("B"): break
        elif i == 9: #South-west
            print("\n Question # ",q_num, end="\t")
            print('''
            A man is facing west. He turns 45 degree in the clockwise direction and then another 180 degree in the same direction and then 270 degree in the anticlockwise direction. Find which direction he is facing now ?
        *OPTIONS*:
            A. South-West       B. South       C. West      D. East-South
            ''')
            if validate ("A"): break
    print("\n==================================================================YOUR RESULTS ARE READY==============================================================\n")
    while True:
        result = input("Enter 'Y' to get your result or 'N' to finsih the test without results:\t").upper()
        if result == 'Y':
            results(score)
            break
        elif result =='N':
            print("You chose to get no result!")
            break
        else:
            print("Make sure to input 'Y' or 'N'.")
    print("\n=================================================================DO YOU WANT TO TRY AGAIN?============================================================\n")
    again = input("Do you want to Try Again? (Y/N):   ")
