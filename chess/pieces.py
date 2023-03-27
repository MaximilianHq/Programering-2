class Board:
    def __init__(self):
        self.position 
        self.piece
        
class Piece:
    
    def __init__(self, type, color):
        self.piece = {
            'type' : type,
            'color' : color
        }
        self.valid_movements = list()
        
    def pieceType(self) -> str:
        return self.piece[[type]]
        
class Pawn(Piece):
    
    def __init__(self):
        self.valid_movements.append((0,1))
        
class Rook(Piece):
    
    def __init__(self):
        self.valid_movements.append((0,8),(0,-8),(8,0),(-8,0))
        
class Knight(Piece):
    
    def __init__(self):
        self.valid_movements.append((-3,1),(-3,-1),(3,1),(3,-1),(1,-3),(-1,-3),(1,3),(-1,3))
        
class Bishop(Piece):
    
    def __init__(self):
        self.valid_movements.append((8,8),(-8,-8),(8,-8),(-8,8))
        
class Queen(Piece):
    
    def __init__(self):
        self.valid_movements.append((0,8),(0,-8),(8,0),(-8,0),(8,8),(-8,-8),(8,-8),(-8,8))
        
class King(Piece):
    
    def __init__(self):
        self.valid_movements.append((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1))