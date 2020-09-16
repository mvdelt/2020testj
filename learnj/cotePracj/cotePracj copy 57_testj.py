

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]

# s = sum(i for row in board for i in row)
s = sum(1 for row in board for i in row if i)

print(s)

# print(hash(board))
hashed=hash(tuple(row) for row in board)
print(*[tuple(row) for row in board])
print(hashed)
# print(hash(*[tuple(row) for row in board]))
print(hash(tuple([(1,2,3,0),(3,3,4,5),(1,2,3,2)] + [-1,-1,0] + [2,3])))
print(hash(tuple([(1,2,3,0),(3,3,4,5),(1,2,3,2)] + [-1,-1,0] + [2,3])))
print(hash(tuple([(1,2,3,0),(3,3,4,5),(1,2,3,2)] + [2,3] + [-1,-1,0])))
print(hash(tuple([(1,2,3,0),(3,3,4,5),(0,2,3,2)] + [-1,-1,0] + [2,3])))
print(hash(tuple([(1,2,3,0),(3,3,4,5),(1,2,3,2)] + [-1,-1,1] + [2,3])))