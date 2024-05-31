import random

someWords = '''apple banana mango strawberry
orange grape pineapple aprioot lemon coconut watermelon 
cherry berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print("Guess the word! HINT: word is a name of fruit")

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0

    try:
        while(chances != 0):
            print()
            chances -= 1
            try:
                guess = str(input("enter a letter to guess: "))
            except:
                print("enter only a letter!")
                continue
            
            #the validation is happenig
            if not guess.isalpha() :
                print('enter only a letter')
                continue
            elif len(guess) > 1:
                print('enter only a single letter')
                continue
            elif guess in letterGuessed:
                print("You have already guess that letter")
                continue

            #if the letter is guessed corecly
            if guess in word:
                letterGuessed += guess
            
            #print the word
            for char in word:
                if char in letterGuessed:
                    print(char, end =' ')
                    correct += 1
                
                else:
                    print('_', end=' ')
            
            #if user has guessed all the letters
            if(set(letterGuessed) == set(word)):
                print()
                print("Congratulation  you won!!")
                break
        
        if chances==0:
            print()
            print("Sorry You Lose!!!")
            print("The word was {}".format(word))
    
    except:
        print()
        print("Bye, try again")
        exit()
            



