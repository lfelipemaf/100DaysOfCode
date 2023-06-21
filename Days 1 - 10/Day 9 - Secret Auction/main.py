import art
from os import system, name
print(art.logo)
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
end_auction = False
bidders = {}
while end_auction is not True:
    name = input("What's your name: ").lower()
    bid = input("What's your bid: $")
    bidders[name] = bid
    bids =  input("\nThere is any more bidders? 'y' for yes and 'n' for no.").lower()
    if bids == "n":
        end_auction = True
    clear()
highest_bid = 0
highest_bidder = ""
for i in bidders:
    if int(bidders[i]) >= int(highest_bid):
        highest_bid = bidders[i]
        highest_bidder = i
print(f"\nThe winner is {highest_bidder} with the bid of ${highest_bid}")