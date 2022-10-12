class Player:
    
    #create and use variables inside of function
    def __init__(self):
        #players points
        self.points = 0
        #player names
        self.name = input("Ange ditt namn: ")
        self.choice = ""

    validChoices=["sten", "sax", "påse"]

    #let players chose a move
    def choose(self):
        valid=False
        #if move is not valid repeat the question
        while valid==False:
            self.choice = input(f"{self.name}, välj sten, sax eller påse: ")
            if self.choice in Player.validChoices:
                valid=True
            else:
                print(self.choice + ", is not a valid option\n")

    #transform move into integer
    def to_numerical_choice(self):
        switcher = {"sten": 0, "sax": 1, "påse": 2}
        return switcher[self.choice]

    #give player point
    def incrementPoint(self):
        self.points += 1

    #print the winner
    def print_winner(self):
        print("\n"+self.name, "vann rundan!")

class GameRound:

    round=0
    
    #create and use variables inside of function
    def __init__(self, p1, p2):
        
        #keeps track of round
        GameRound.round += 1

        print("\nSpelomgång", GameRound.round, "\n")
        #En 2-dimensionell array
        self.rules = [[0, 1, -1],[-1, 0, 1],[1, -1, 0]]
        #players choose move
        p1.choose()
        p2.choose()
        #compare moves and declare a winner
        result = self.compare_choices(p1, p2)

        if(result>0): 
            p1.incrementPoint()
            p1.print_winner()

        elif(result<0):
            p2.incrementPoint()
            p2.print_winner()

        else:
            print("Rundan slutade lika")

    def score_board(self, p1, p2):
        print("\nPoäng:\n"+ p1.name, p1.points, " : ", p2.name, p2.points, "\n________________________\n")
        
    #compare player points ans return the game winner
    def w(self, p1, p2):
        if p1.points > p2.points:
            return p1
        elif p1.points < p2.points:
            return p2
        #if the game is unsettled, p1 becomes no one
        else:
            p1.name="obestämd"
            p1.points="_"
            return p1
    
    #compare moves and declare the round winner
    def compare_choices(self, p1, p2):
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]

class Game:

    #create and use variables inside of function
    def __init__(self):
        print("Sten, sax, påse")
        #let players choose their names
        print("\nSpelare 1")
        self.player1 = Player()
        print("\nSpelare 2")
        self.player2 = Player()
        self.endgame = False

    def start(self):
        while(self.endgame != True):      
            game_round = GameRound(self.player1, self.player2)
            
            #decide how long the match will continue
            valid=False
            while valid==False:
                cont = input("Vill ni fortsätta (j/n)?")
                if(cont=="n"):
                    self.endgame=True
                    valid=True
                elif(cont=="j"):
                    valid=True
                else:
                    print(cont + ", is not a valid option\n")
                    
        print("Spelet är över.\n")
        
        game_round.score_board(self.player1, self.player2)
        #show scoreboard
        winner = game_round.w(self.player1, self.player2)
        print(f"\nVinnaren är {winner.name} med {winner.points} poäng!\n")
            
game=Game()

#start the game
game.start()