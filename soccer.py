def best_teams(best):
    wrong_guesses = 0
    s = ["|"'\n',  "|"'\n',  "|""\n",  "|"'\n', "|","__"," ""__" " " "__"]

    l_left = list(best) # create a list "m""a""n""u""t""d"
    boards = ["_"]*len(best) #boards is the length of the team ex: ______
    win = False
    print("Welcome to the this simple game ")




    while wrong_guesses < len(s)) - 1: # youhave the length of s amont of guesses 
        print("\n")
        guess = input("Guess the first letter of the best team ")
        if guess in l_left:
            char_index = l_left.index(guess)
            boards[char_index] = guess
            l_left[char_index = '$']


        








    









best_teams("manutd")



