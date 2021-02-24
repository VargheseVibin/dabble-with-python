bid_dict = {}
done="no"

while (done=="no"):
    name=input("Hello Bidder!! Please Enter your name:")
    bid=int(input("Please enter your bid:$"))

    bid_dict[name]=bid
    done=input("Are you done? [Yes/No]:").lower()

highest_bidder="John Doe"
highest_bid=0
for name in bid_dict:
    if bid_dict[name]>=highest_bid:
        highest_bid=bid_dict[name]
        highest_bidder=name

print(f"{highest_bidder} has won the auction with a bid of ${highest_bid}")

