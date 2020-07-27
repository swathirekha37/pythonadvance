import random

compnum=random.randint(1,10)



def game():
    count=0

    while count<5:
        try:
            userguess=int(input('guess the number: '))
        except ValueError:
            print('enter only integers')
        else:
            if userguess == compnum:
                print('congratulations you won the game. The number is {}'.format(compnum))
                break
            
            elif userguess != compnum:
                if userguess < compnum:
                    print("your guess is less than compnum.")
                    count=count+1
                
                elif userguess > compnum:
                    print("your guess is greater than compnum")
                    count=count+1
                
    else:   
        print('oops! You are out of chances')

    que=input('do you want to play again?(y/n')    
    if que=='y':
        game()
    

game()            
