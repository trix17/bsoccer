def best_teams(best):
    wrong_guesses = 0
    s = ["|"'\n',  "|"'\n',  "|""\n",  "|"'\n', "|","  ___ ___ ___"]

    l_left = list(best) # create a list "m""a""n""u""t""d"
    
    boards = ["_"]*len(best) #boards is the length of the team ex: ______
    win = False
    print("Welcome to the this simple game ")




    while wrong_guesses < len(s) - 1: # youhave the length of s amont of guesses 
        print("\n")
        guess = input("Guess a letter of the best team ")
        if guess in l_left:
            char_index = l_left.index(guess)
            boards[char_index] = guess
            l_left[char_index] = '$'


        else:
            wrong_guesses += 1

        print(''.join(boards)) #he join() method takes all items in an iterable and joins them into one string
        print('\n'.join(s[0:wrong_guesses+1]))


        if '_' not in boards:
            print("You win, Game Over")
            print("".join(boards))

            win = True 
            break 
    
    if not win:
        
        print("\n")
        print('\n'.join(s))
        
        print("Sorry , you lost, the word was {}".format(best))
        

best_teams("manutd")
        




