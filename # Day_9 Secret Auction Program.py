# Secret Auction Program

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record :
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The Winner is {winner} with a bid of {highest_bid}")        



dic = {}
bidding_finish = False
while not bidding_finish:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dic[name] = bid
    other = input("Are ther any bidders? Type 'yes' or 'no'.")
    if other == 'no':
        highest_bidder(dic)
        bidding_finish = True
    elif other == 'yes' :
        highest_bidder(dic)
    else:
        print("Wrong Input!")        
    