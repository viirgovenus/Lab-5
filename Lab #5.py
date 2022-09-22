
import random

def play_again() -> bool: #asks users if they'd like to play again
    while True:
        play = input("Do you want to play again?\n")
        play = play.upper()
        if play == "Y" or "YES":
            return True
        elif play == "N" or "NO":
            return False
        print("Please enter a valid value")

def get_wager(bank : int) -> int: #asks users how many chips they want to wager
    while True:
        wager = int(input("How many chips do you want to wager?"))
        if wager > bank:
            print("The value for your wager must not be greater than the value in your bank. Please choose another number.")
        elif wager < 0:
            print("The value for your wager must be greater than zero. Please choose another value.")
        else:
            return wager

def get_slot_results() -> tuple: #returns 3 random reels
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = random.randint(1, 10)
    return (num_1, num_2, num_3)

def get_matches(reelA, reelB, reelC): #returns how many of the reels match
    if reelA == reelB and reelA == reelC:
        return 3
    elif reelA == reelB or reelA == reelC or reelB == reelC:
        return 2
    return 0
        
def get_bank(): #asks users how many chips they'd like to start with
    while True:
        chips = int(input("How many chips would you like to start with?\n"))
        if chips > 0 and chips < 101:
            return chips
        elif chips < 1:
            print("Please pick a value greater than 0.")
        else:
            print("Please pick a value lower than 101.")   

def get_payout(wage, matches): #returns payout for user based on how many matches and the wager
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1
    
    

if __name__ == "__main__":

    playing = True #starts games
    while playing:
        bank = get_bank() #beginning number of chips
        initial_bank = bank #tells beginning number of chips
        count = 0 #count starts at zero always
        new_bank = 0 #new amount always starts at zero
        high_score = bank
        while bank > 0: #main game function
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > new_bank:
                high_score = bank
            new_bank = bank

            print("Your spin", reel1, reel2, reel3) #tells spin results
            print("You matched", matches, "reels") #tells matches
            print("You won/lost", payout) #tells if won or lost
            print("Current bank", bank) #tells current bank
            print()
            count +=1

        print("You lost all {} spins in {} spins".format(initial_bank, count)) #tells results of game
        print("The most chips you had was {}".format(high_score)) #tells high score
        playing = play_again() #resets game
        

        
        
            

        
    
    
            
            
        
        
        
        
