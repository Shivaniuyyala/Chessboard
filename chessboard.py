##################
"""
Author : Shivani
execute it using the command: python chess.py KNIGHT c2  // python chess.py type_of_pieces current_position
// types of pieces : KNIGHT, ROOK, BISHOP, QUEEN, KING, PAWN (not implemented code for this)

output: 
Possible moves for KNIGHT are :
d4
d0
b4
b0
e3
e1
a3
a1


"""
#####################

import sys

def findPossibleMovesForKnight(chess, p, q):
	# All possible moves of a knight 
	possible_moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
	count = 0
	res = []
	for each in possible_moves:
		x = p+each[0]
		y = q+each[1]
		if x>=0 and y>=0 and x<8 and y<8 and chess[x][y] == 0:
			count = count+1
			res.append([x,y])
	return res

def findPossibleMovesForBishop(chess, x, y):
	res = []
    	for i in range(1,8):
		if 0<=x+i<8 and 0<=y+i<8 and chess[x+i][y+i] == 0:
			res.append([x+i,y+i])
		if 0<=x-i<8 and 0<=y-i<8 and chess[x-i][y-i] == 0:
			res.append([x-i,y-i])
		if 0<=x+i<8 and 0<=y-i<8 and chess[x+i][y-i] == 0:
			res.append([x+i,y-i])
		if 0<=x-i<8 and 0<=y+i<8 and chess[x-i][y+i] == 0:
			res.append([x-i,y+i])
		
    	return res

def findPossibleMovesForRook(chess, x, y):
	res = []
    	for i in range(1,8):
		if 0<=y+i<8 and chess[x][y+i] == 0:
			res.append([x,y+i])
		if 0<=y-i<8 and chess[x][y-i] == 0: 
			res.append([x,y-i])
		if 0<=x+i<8 and chess[x+i][y] == 0:
			res.append([x+i,y])
		if 0<=x-i<8 and chess[x-i][y] == 0:
			res.append([x-i,y])
    	return res

def findPossibleMovesForKing(chess, x, y):
	res = []
	i = 1
	if 0<=y+i<8 and chess[x][y+i] == 0:
		res.append([x,y+i])
	if 0<=y-i<8 and chess[x][y-i] == 0: 
		res.append([x,y-i])
	if 0<=x+i<8 and chess[x+i][y] == 0:
		res.append([x+i,y])
	if 0<=x-i<8 and chess[x-i][y] == 0:
		res.append([x-i,y])
	if 0<=x+i<8 and 0<=y+i<8 and chess[x+i][y+i] == 0:
		res.append([x+i,y+i])
	if 0<=x-i<8 and 0<=y-i<8 and chess[x-i][y-i] == 0:
		res.append([x-i,y-i])
	if 0<=x+i<8 and 0<=y-i<8 and chess[x+i][y-i] == 0:
		res.append([x+i,y-i])
	if 0<=x-i<8 and 0<=y+i<8 and chess[x-i][y+i] == 0:
		res.append([x-i,y+i])
    	return res
		
def findPossibleMovesForQueen(chess, x, y):
	# finding horizantal and vertical direction possible moves
	res = findPossibleMovesForRook(chess, x, y)
	
	# finding possible diagonally direction moves
	res = res+findPossibleMovesForBishop(chess, x, y)
	return res

def getPiece(i):
	switcher={
			"KNIGHT" : findPossibleMovesForKnight,
			"ROOK" : findPossibleMovesForRook,
			"BISHOP" : findPossibleMovesForBishop,
			"QUEEN" : findPossibleMovesForQueen,
			"KING" : findPossibleMovesForKing
		}
	return switcher.get(i,"Invalid Piece of Chess")
	 
def main():
	chess = [[0 for i in range(8)] for i in range(8)]

	pos_dict = { 0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
	p = -1
	q = -1
	try:
		func = getPiece(sys.argv[1])
		if func == "Invalid Piece of Chess":
			print "Invalid Piece of Chess"
			return 0
			
	except:
		print "Provide valid input for the -piece option: available are KNIGHT, ROOK, BISHOP, QUEEN, KING"
		return 0

	try:
		pos = sys.argv[2]
		p = ord(pos[0])-97
		q = int(pos[1])
	except:
		print "Provide valid input for position: which should be in the range 8*8 Chess Board: for example 'a5','b6'."
		
	if not 0<=p<8 or not 0<=q<8:
		print "Position should in the range (a to h , 0 to 7)"
		return 0
	else:	
		res = func(chess, p,q)
		print "Possible moves for %s are :" % sys.argv[1]
		for each in res:
			print pos_dict[each[0]]+str(each[1])
			
if __name__=='__main__':
	main()
			
		
	
	
