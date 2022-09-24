import os
bidder_info = {}
# bidder_list = []


# def add_bidder(new_bidder, new_bid):
#     bidder_info["name"] = new_bidder
#     bidder_info["bid"] = new_bid

#     bidder_list.append(bidder_info)


# add_bidder(new_bidder=user_name, new_bid=user_bid)

def bidder_record(bidder_info):
    highest_bid = 0
    winner = ""
    for (bidder) in bidder_info:
        bidding_record = bidder_info[bidder]
        if bidding_record > highest_bid:
            highest_bid = bidding_record
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid_end = False
while not bid_end:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bidder_info[user_name] = user_bid
    decide = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if decide == "yes":
        bid_end = False

        os.system('cls')
    if decide == "no":
        bid_end = True
        bidder_record(bidder_info)
