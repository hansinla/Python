# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
player_in_play = False
dealer_in_play = False
outcome = ""
score1 = ""
score2 = ""
wins = 0
plays = 0
debug = False			#assign True to debug
TABLE_SIZE_X = 600
TABLE_SIZE_Y = 600

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE, rot_list[RANKS.index(self.rank)])
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.card_list = []
        
    def __str__(self):
        # return a string representation of a hand
        s = ""
        for card in self.card_list:
            s = s + str(card) + " "
        return "Hand contains " + s
            
    def add_card(self, card):
        # add a card object to a hand
        self.card_list.append(card)
    
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.score = 0
        ace_in_deck = False
        for card in self.card_list:
            if card.get_rank() == 'A':
                ace_in_deck = True
            self.score += VALUES[card.get_rank()]
        if ace_in_deck and self.score + 10 <= 21:
            self.score += 10
        return self.score
        
        
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_list = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_list.append(Card(suit,rank))

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck_list)

    
    def deal_card(self):
        # deal a card object from the deck
        return self.deck_list.pop()
    
    def __str__(self):
        s = ""
        for card in self.deck_list:
            s = s + str(card) + " "
        return "Deck contains " + s

#define event handlers for buttons
def deal():
    global plays, wins, outcome, score1, score2, player_in_play, dealer_in_play, dealer_hand, player_hand, playing_deck, rot_list
    if player_in_play:
        plays += 1
    outcome = ""
    score1 = ""
    score2 = ""
    rot_list = []
    for i in range (52):
        rot_list.append((random.random()-0.5)/2)
    
    # initialize dealer hand and player hand
    dealer_hand = Hand()
    player_hand = Hand()
    # create a deck and shuffle it
    playing_deck = Deck()
    playing_deck.shuffle()
    # deal two cards to player and dealer
    for i in range (2):
        dealer_hand.add_card(playing_deck.deal_card())
        player_hand.add_card(playing_deck.deal_card())
    # player is in play    
    player_in_play = True
    dealer_in_play = False
         
    game_state(dealer_hand, player_hand, playing_deck) #debug code
   
    if player_hand.get_value() == 21:
        outcome = "Player wins."
        wins += 1
        plays += 1
        score1 = str(dealer_hand.get_value())
        score2 = str(player_hand.get_value())
        player_in_play = False
        dealer_in_play = True

    
def game_state(dealer_hand, player_hand, playing_deck): # debug helper code
    if debug:
        print ""
        print "Dealer " + str(dealer_hand) + "value " + str(dealer_hand.get_value())
        print "Player " + str(player_hand) + "value " + str(player_hand.get_value())
        print playing_deck
        print player_in_play, dealer_in_play
    

def hit():
    global plays, wins, outcome, score1, score2, player_in_play, dealer_in_play
    # if the hand is in play, hit the player
    if player_in_play:
        player_hand.add_card(playing_deck.deal_card())
        
        game_state(dealer_hand, player_hand, playing_deck) #debug code
        
        if player_hand.get_value() == 21:
            if dealer_hand.get_value() < 21:
                outcome = "Player wins."
                wins += 1
                plays += 1
                score1 = str(dealer_hand.get_value())
                score2 = str(player_hand.get_value())
                player_in_play = False
                dealer_in_play = True
            else:
                outcome = "Dealer wins."
                plays += 1
                score1 = str(dealer_hand.get_value())
                score2 = str(player_hand.get_value())
            player_in_play = False
            dealer_in_play = True
        
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted. Dealer wins."
            plays += 1
            score1 = str(dealer_hand.get_value())
            score2 = str(player_hand.get_value())
            player_in_play = False
            dealer_in_play = True
 
       
def stand():
    global plays, wins, outcome, score1, score2, player_in_play, dealer_in_play
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    player_in_play = False
    dealer_in_play = True
    
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(playing_deck.deal_card())
    # assign a message to outcome, update in_play and score
    game_state(dealer_hand, player_hand, playing_deck) #debug code
    
    if  (dealer_hand.get_value() >=  player_hand.get_value()) and dealer_hand.get_value() <= 21:
        outcome = "Dealer wins."
        plays += 1
        score1 = str(dealer_hand.get_value())
        score2 = str(player_hand.get_value())
    elif dealer_hand.get_value() > 21:
        outcome = "Dealer busted. Player wins."
        wins += 1
        plays += 1
        score1 = str(dealer_hand.get_value())
        score2 = str(player_hand.get_value())
    else:
        outcome = "Player wins."
        wins += 1
        plays += 1
        score1 = str(dealer_hand.get_value())
        score2 = str(player_hand.get_value())
   
def toggle_debug(): # toggle debug code on/off
    global debug
    debug = not debug

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", (text_pos1, 60), 60, "Gray", "sans-serif")
    canvas.draw_text("Dealer", (10, 240), 36, "Gray", "sans-serif")
    canvas.draw_text("Player", (10, 440), 36, "Gray", "sans-serif")
    canvas.draw_text(outcome, (580 - frame.get_canvas_textwidth(outcome, 24, "sans-serif"), 240), 24, "White", "sans-serif")
    canvas.draw_text(score1, (500 - frame.get_canvas_textwidth(score1, 36, "sans-serif"), 330), 36, "White", "sans-serif")
    canvas.draw_text(score2, (500 - frame.get_canvas_textwidth(score2, 36, "sans-serif"), 520), 36, "White", "sans-serif")
    if plays > 0:
        canvas.draw_text("wins: "+ str(wins) + " out of " + str(plays) + " games", (180, 595), 24, "White", "sans-serif")
    if player_in_play:
        canvas.draw_text("Hit or Stand?", (300, 440), 24, "White", "sans-serif")
    else:
        if not dealer_in_play:
            canvas.draw_text("New Deal?", (300, 440), 24, "White", "sans-serif")
        else:
            if not outcome == "":
                canvas.draw_text("New Deal?", (300, 440), 24, "White", "sans-serif")
    
    if dealer_in_play or player_in_play: # make sure a deck exists
        # draw the deck
        for index in range(0,len(playing_deck.deck_list)):
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [60 + index * 8, 140], [75,100], rot_list[index]/2)
        
        index = 0
        for card in player_hand.card_list:
            card.draw(canvas, [30 + index * CARD_SIZE[0], 460])
            index += 1
            
        if dealer_in_play:
            index = 0
            for card in dealer_hand.card_list:
                card.draw(canvas, [30 + index * CARD_SIZE[0], 272])
                index += 1
        else:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [55, 320], [75,100], rot_list[0])
            for index in range(1,len(dealer_hand.card_list)):
                card = dealer_hand.card_list[index]
                card.draw(canvas, [30 + index * CARD_SIZE[0], 272])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
label1 = frame.add_label("")
frame.add_button("Hit",  hit, 200)
label2 = frame.add_label("")
frame.add_button("Stand", stand, 200)
label3 = frame.add_label("")
#frame.add_button("Toggle Debug On/Off", toggle_debug, 200) #uncomment to debug
frame.set_draw_handler(draw)
text_pos1 =  TABLE_SIZE_X/2 - 0.5 * frame.get_canvas_textwidth("Blackjack", 60, "sans-serif")

# get things rolling
frame.start()
