import itertools 
import random
import time
import os
import numpy

def acknowledgement_display():	
	for i in reversed(range(3)) :
		time.sleep(1)
		print("\n We will begin in "+str(i+1)+" seconds ..... \n")

class Card :
	def __init__(self, suit, face) :
		self.suit = suit
		self.face = face

	def __str__(self):    
		return self.face+' of '+self.suit


class Deck :
	def __init__(self, cards_list=[]) :
		self.cards = cards_list

	def print_deck(self) :
		if len(self.cards) > 0 :
			for card in reversed(self.cards) :
				print(card)

	def pop(self):
		card=self.cards.pop()
		return card#,Deck(self.cards)

	def get_length(self) :
		return len(self.cards)

	def add_card(self,card):
		self.cards.append(card)
		return Deck(self.cards)

	def is_empty(self) :
		return len(self.cards) < 1 


class Player :
	def __init__(self, name, cards) :
		self.name = name
		self.deck = Deck(cards)

	def print_info(self) :
		print("\nNAME :- "+str(self.name))
		print("\n Deck is as follows")
		self.deck.print_deck()

	def take_turn(self, visible_deck) :

		if not self.deck.is_empty() :
			card = self.deck.pop()
			print("\n"+ self.name + "'s card is :-\n")
			print(card)
			visible_deck = visible_deck.add_card(card)
			print("\n Visible Stack :- ")
			visible_deck.print_deck()

		return self.deck, visible_deck

	def take_stack(self, visible_deck) :
		print("\n Cards Matched , Stack will be shifted now......")
		print("\n STACK WILL BE SHIFTED TO "+str(self.name)+'\n')
		time.sleep(4)
		return Deck(self.deck.cards + visible_deck.cards), Deck([])


def screenshow(players,visible_deck) :
	for player in players :
		print player.name,

class Game :
	players = []
	visible_deck = Deck([])
	scores = []
	deck_lengths = []

	def initiate(self) :

		while True:	
			name = str(raw_input("\n Enter the name of the player :- \n"))
			self.players.append(Player(name, cards = []))
			if len(self.players) < 2:
				continue
			else :
				inp = str(raw_input("\n To add more players please enter 1 \n"))
				if inp != '1' :
					break

		suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
		values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
		all_cards = []
		for suit in suits :
			for value in values :
				card = Card(suit, value)
				all_cards.append(card)
		random.shuffle(all_cards)	

		index = 0
		for card in all_cards :
			self.players[index % len(self.players)].deck.add_card(card)
			index += 1

		for player in self.players :
			self.deck_lengths.append(len(player.deck.cards))
			player.print_info()

		acknowledgement_display()
	
	def printscore(self,totalscore) :
		print "GAME NO. , ",
		for player in self.players :
			print player.name,
			print "   ",
		print("\n   ")	
		for i in range(len(totalscore)):
			print "  "+str(i+1),
			print "         ",
			for indiv_score in totalscore[i] :
				print indiv_score,
				print "     ",


	def is_game_on(self) :
		for i in range(len(self.players)) :
			self.deck_lengths[i] = self.players[i].deck.get_length()
		print("\nThe deck deck_lengths are :- ",self.deck_lengths)	

		return (len(self.players)-self.deck_lengths.count(0)) > 1 

	def check_stack(self) :
		if len(self.visible_deck.cards) > 1 and self.visible_deck.cards[len(self.visible_deck.cards)-1].face == self.visible_deck.cards[len(self.visible_deck.cards)-2].face :
			return True
		return False		

	def begin(self) :		
		while self.is_game_on() :
			index=0
			while index < len(self.players) :
				(self.players[index].deck, self.visible_deck) = self.players[index].take_turn(self.visible_deck)
				if self.check_stack() :
					(self.players[index].deck, self.visible_deck) = self.players[index].take_stack(self.visible_deck)
				else :
					index = index + 1

		if (len(self.players)-self.deck_lengths.count(0)) == 0 :
			print("\n The match is draw between all the players\n")
		else :
			print("\n "+self.players[self.deck_lengths.index(max(self.deck_lengths))].name+" has won the match \n\n")
			self.scores=[0]*len(self.players)
			self.scores[self.deck_lengths.index(max(self.deck_lengths))]=1


def main():

	totalscore=[]
	p2p = Game()
	p2p.initiate()
	p2p.begin()
	totalscore.append(p2p.scores)
	p2p.printscore(totalscore)

if __name__== "__main__":
	main()	
