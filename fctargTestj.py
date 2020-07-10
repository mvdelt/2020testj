# A function that shows the results of running competitions consisting of 2 to 4 runners.
def save_ranking(first, second='sec',*, third=None, fourth=None):
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)    

# # Pass the 2 positional arguments
# save_ranking('ming', 'alice')
# # Pass the 2 positional arguments and 1 keyword argument
# save_ranking('alice', 'ming', third='mike')
# # Pass the 2 positional arguments and 2 keyword arguments (But, one of them was passed as like positional argument)
# save_ranking('alice', 'ming', 'mike', fourth='jim')

save_ranking('111','real2nd',third='3rd',fourth='fourth~~')