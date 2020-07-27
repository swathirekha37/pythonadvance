import random

words=['apple','mango','grapes','oranges','cherries','eggs','mushrooms']

word=random.choice(words)
print("the length og the word is  {}".format(len(word)))
correct=0
fail=0
guessed=dict.fromkeys(word,0)
flag=0

for i in range(0,7):
    letter=str(input("enter the guessing letter : "))
    if letter in word:
        print("{} is present".format(letter))
        correct=correct+1
        guessed[letter]=guessed[letter]+1
        i=i
        if letter in guessed:
            flag=flag+1

        print("i value is {} and correct value is {} and the flag vaue is {} ".format(i,correct,flag))
        if len(word)==correct+flag:
            print("congratulations you win the game and the word is {}".format(word))
            break
    else:
        fail=fail+1
        print("{} is not present ".format(letter))
        if len(word)==fail:
            print("sorry you lose the game and the word is {}".format(word))       
            break
    print(" ".join([letter if guessed[letter] else '-' for letter in word]))
    #print(" ".join([ch if guessed[ch] else '- ' for ch in word]))
else:
    print("sorry you lose the game and the word is {}".format(word))       


