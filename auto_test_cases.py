import unittest
import sys
from chessboard import *

class TestChessboard(unittest.TestCase):
	chess = [[0 for i in range(8)] for i in range(8)]
	def test_findPossibleMovesForKnight(self):
		res = findPossibleMovesForKnight(TestChessboard.chess, 0, 2)
		self.assertEqual(res, [[1, 4], [1, 0], [2, 3], [2, 1]])

	def test_findPossibleMovesForBishop(self):
		res = findPossibleMovesForBishop(TestChessboard.chess, 0, 2)
		self.assertEqual(res, [[1, 3], [1, 1], [2, 4], [2, 0], [3, 5], [4, 6], [5, 7]])

	def test_findPossibleMovesForRook(self):
		res = findPossibleMovesForRook(TestChessboard.chess, 0, 2)
		self.assertEqual(res, [[0, 3], [0, 1], [1, 2], [0, 4], [0, 0], [2, 2], [0, 5], [3, 2], [0, 6], [4, 2], [0, 7], [5, 2], [6, 2], [7, 2]])

	def test_findPossibleMovesForKing(self):
		res = findPossibleMovesForKing(TestChessboard.chess, 0, 2)
		self.assertEqual(res, [[0, 3], [0, 1], [1, 2], [1, 3], [1, 1]])

	def test_findPossibleMovesForQueen(self):
		res = findPossibleMovesForQueen(TestChessboard.chess, 0, 2)
		self.assertEqual(res, [[0, 3], [0, 1], [1, 2], [0, 4], [0, 0], [2, 2], [0, 5], [3, 2], [0, 6], [4, 2], [0, 7], [5, 2], [6, 2], [7, 2], [1, 3], [1, 1], [2, 4], [2, 0], [3, 5], [4, 6], [5, 7]])

	def test_main(self):
		sys.argv = ['', 'xxx', 'a2']
		res = main()
		self.assertEqual(res, "Invalid Piece of Chess")
		sys.argv = ['xxx']
		res = main()
		self.assertEqual(res, "Incorrect number of command line arguments")
		sys.argv = ['', 'KNIGHT', 'a9']
		res = main()
		self.assertEqual(res, 'Position should in the range (a to h , 0 to 7)')
		sys.argv = ['', "KNIGHT", 'a2']
		res = main()
		self.assertEqual(res, "Possible moves for KNIGHT are ['b4', 'b0', 'c3', 'c1']")


if __name__ == '__main__':
    unittest.main()
