import os
def system():
    os.system(cls)

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
        winner = bidder
    print(f"The winner is {bidder} with the bid amount of {bid_amount}")


bid = {}
bidding_finished = False
while not bidding_finished:
   name = input("Enter your name:")
   bid_amount = int(input("Enter your bid amount:"))
   bid[name] = bid_amount 
   for_further = input("Are there anyone else? Type 'yes' or 'no'.")
   if for_further == "no":
        bidding_finished = True
        highest_bidder(bid)
   elif for_further == "yes":
        system 
