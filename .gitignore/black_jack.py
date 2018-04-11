import os
import random

clear= lambda:os.system('clear')
cards=[x for x in range(2,11)]

cards.extend(['A','K','Q','J'])


class dealer(object):
    score=0
    def __init__(self,money=0):
        pass
    def show_money(self):
        print(self.money)
        pass
    def add_money(self,prize_money):
        self.money+=self.prize_money
        pass
    
    
    


class player(object):
    money=2500
    score=0
    def __init__(self,name):
        self.name=name
        
        pass
    def hit(self,val):
        self.score+=val
        pass

    

        
        

blackjack=input("whats your name")
name=player(blackjack)
deal=dealer()
print("Hi " +blackjack+"!"+ " Let's play the game")


while True:
            while True:
                try:
                    amount=int(input("what is your bet amount"))
                    if name.money<amount:
                            print("you have insufficient amount.Try lower bet.")
                            continue
                    break
                except:
                    print(" looks like what you entered is not a integer ! try again")
                    continue
            print("HERE YOU GO!")

            val1=random.randint(0,11)
            val2=random.randint(0,11)
            while val1==val2==8:
                val1=random.randint(0,11)
                val2=random.randint(0,11)
    
            val3=random.randint(0,11)
            val4=random.randint(0,11)
            while val3==val4==8:
                val3=random.randint(0,11)
                val4=random.randint(0,11)
    
            print("your first card is {}".format(cards[val1]))
            print("your second card is {}".format(cards[val2]))
            if 9<=val1<=11:
                  name.score=name.score+10
            elif val1==8:
                  name.score=name.score+11
            else:
                  name.score+=int(cards[val1])
            if 9<=val2<=11:
                  name.score=name.score+10
            elif val2==8:
                  name.score=name.score+11
            else:
                  name.score+=int(cards[val2])
            if 9<=val3<=11:
                  deal.score=deal.score+10
            elif val3==8:
                  deal.score=deal.score+11
            else:
                  deal.score+=int(cards[val3])
            if 9<=val4<=11:
                  deal.score=deal.score+10
            elif val2==8:
                  deal.score=deal.score+11
            else:
                  deal.score+=int(cards[val4]) 
            print()
            print()
            print("YOUR SCORE IS {}".format(name.score))
            print()
      
            print("dealer first card is {}".format(cards[val3]))

            if name.score==21 and deal.score!=21:
                printf("Wow! ypu are the blackjack")
                name.money+=amount
                print("your total money is {}".format(name.money))
                while True:
                    d_for_playing= input("do you want to continue playing? yes/no")        

                    if d_for_playing!="yes" or d_for_playing!="no":
                        print("enter the correct input")
                        continue
                    else:
                        break
                if d_for_playing=="yes":
                    name.score=0
                    deal.score=0
                    continue 
                else:
                    print("Bye!Bye! Blackjack")
                    break 
            else:
                while name.score < 21:
                    
                    while True:
                        h_s= input("do you want to hit or stand? hit/stand")        

                        if h_s!="hit" and h_s!="stand":
                            print("enter the correct input")
                            continue
                        if h_s=="hit" or h_s=="stand":
                            break
                        
                    if h_s=="hit":
                            val=random.randint(0,11)
                            if 9<=val<=11:
                                 name.score=name.score+10
                            elif val==8 and name.score+11<=21:
                                 name.score=name.score+11
                            elif  val==8 and name.score+11>21:
                                name.score=name.score+1
                               
                            else:
                                name.score+=int(cards[val1])
                            if name.score>21:
                                print("your total score is {}".format(name.score))
                                print("the second card of dealer is {}".format(cards[val4]))
                                print("the Dealer wins")
                            elif name.score==dealer.score:
                                print("your total score is {}".format(name.score))
                                print("the second card of dealer is {}".format(cards[val4]))
                                print("Its a push")
                            elif name.score<21:
                                print("your total score is {}".format(name.score))
                            
                    else:
                        if name.score>deal.score<21:
                            print("your total score is {}".format(name.score))
                            print("the second card of dealer is {}".format(cards[val4]))
                            while deal.score<=21 and deal.score<=name.score:
                                val=random.randint(0,11)
                                print("card picked by dealer is {}".format(cards[val]))
                                if 9<=val<=11:
                                     deal.score=deal.score+10
                                elif val==8 and deal.score+11<=21:
                                     deal.score=deal.score+11
                                elif  val==8 and deal.score+11>21:
                                    deal.score=deal.score+1
                               
                                else:
                                    deal.score+=int(cards[val1])
                            if 21>=deal.score>name.score:
                                print("dealer won")
                            if deal.score==name.score:
                                print("the game is push")
                            else:
                                print("congrajulations!you won")
                            break
                        else :
                            print("your total score is {}".format(name.score))
                            print("the second card of dealer is {}".format(cards[val4]))
                            print("dealer won the game")
                            break
            y_n=input("DO YOU WANT TO PLAY AGAIN? yes/no")
            while y_n!="yes" and y_n!="no":
                print("enter the appropriate input")
            if y_n=="yes":
                continue
            else:
                break
            
