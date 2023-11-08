from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax


class LastCoinStanding(TwoPlayersGame):
    def __init__(self, players):
            self.players = players
            self.nplayer = 1
            self.pile = 20
            self.max_coins = 3

    def possible_moves(self):
         return ['1','2','3']

    def make_move(self, move):
        self.pile -= int(move)

    def win(self):
         return self.pile <= 0

    def is_over(self):
        return self.win()

    def scoring(self):
         return 100 if self.win() else 0
     
    def show(self):
        print "%d coins left" % self.pile

        
    def is_over(self):
        return self.win()
# Start the game
ai= Negamax(13) 
game = LastCoinStanding([Human_Player(),AI_Player(ai)])
#game = LastCoinStanding([Human_Player(),Human_Player()])

history=game.play()




















