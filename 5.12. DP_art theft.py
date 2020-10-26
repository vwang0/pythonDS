"""
Suppose you are a computer scientist/art thief who has broken into a major art gallery. All you have with you to haul out your stolen art is your knapsack which only holds W pounds of art, but for every piece of art you know its value and its weight. Write a dynamic programming function to help you maximize your profit. Here is a sample problem for you to use to get started: Suppose your knapsack can hold a total weight of 20. You have 5 items as follows:

item     weight      value
  1        2           3
  2        3           4
  3        4           8
  4        5           8
  5        9          10
"""
tr = [None, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]

max_weight = 20
m = {(i, w):0 for i in range(len(tr)) for w in range(max_weight+1)}

for i in range(1, len(tr)):
    for w in range(1, max_weight+1):
        if tr[i]['w'] > w:
            m[(i, w)] = m[(i-1, w)]
        else:
            m[(i, w)] = max(m[(i-1, w)], m[(i-1, w-tr[i]['w'])] + tr[i]['v'])
print(m[(len(tr)-1, max_weight)])
