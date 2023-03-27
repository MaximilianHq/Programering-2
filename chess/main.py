import pieces

board_spaces = list()

def gen_board():
    #create board
    for i in range(8):
        for n in range(8):
            board_spaces.append([i, n])
            
    #generate pieces
    pieces.Piece('pawn', 'w')
    board_spaces[8:16].append(pieces.Piece.pieceType())
            
    
gen_board()    
print(board_spaces)