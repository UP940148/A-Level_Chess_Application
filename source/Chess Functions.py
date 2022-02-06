import copy
import Chess_Turtle
#I will need the ability to deep copy boards for move generation and for the minimax algorithm
#deep copying allows me to duplicate an entire board and it's contained objects so that I can analyse the effects of different moves
#this allows me to check if moves will leave a King in check and calculate the values of moves for the minimax algorithm


def ValidPos(BoardPos):
    '''This will allow me to make sure only valid positions are input
    (anywhere between "A1" to "H8")'''
    if len(BoardPos) != 2:
        return None
    if (ord(BoardPos[0]) < 105) and (ord(BoardPos[0]) > 96):
        BoardPos[0].upper()
    if (ord(BoardPos[0]) >= 73) or (ord(BoardPos[0]) <= 64):
        return None
    if (ord(BoardPos[1]) > 56) or (ord(BoardPos[1]) < 49):
        return None
    if (ord(BoardPos[1]) < 57) and (ord(BoardPos[1]) > 48):
        BoardPos[1] == int(BoardPos[1])
    return BoardPos


def PosToCoord(BoardPos):
    '''This will allow me to convert from
    a board position value to a coordinate value
    (e.g. "A4" to (1, 4))'''
    x = ord(BoardPos[0]) -64
    y = int(BoardPos[1])
    return x, y


def CoordToPos(Coord):
    '''This will allow me to convert form
    a coordinate value to a board position value
    (e.g. (1,4) to "A4")'''
    BoardPos = ""
    BoardPos += chr(Coord[0]+64)
    BoardPos += str(Coord[1])
    return BoardPos


def AddToBoard(BoardVal, XMod, YMod):
    '''This will allow me to return a Board position value
    offset from the input position by 'XMod' in the x and 'YMod' in the y'''
    Coord = PosToCoord(BoardVal)
    x = Coord[0] + XMod
    y = Coord[1] + YMod
    Coord = [x, y]
    return CoordToPos(Coord)


class Board:
    def __init__(self):
        self.Whites = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"]
        self.Blacks = ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"]
        self.WPiece = []
        self.BPiece = []
        #Creating all White Pieces and adding them to the PieceList
        self.WPiece.append(Piece("W", "Rook", "A1", self))
        self.WPiece.append(Piece("W", "Knight", "B1", self))
        self.WPiece.append(Piece("W", "Bishop", "C1", self))
        self.WPiece.append(Piece("W", "Queen", "D1", self))
        self.WPiece.append(Piece("W", "King", "E1", self))
        self.WPiece.append(Piece("W", "Bishop", "F1", self))
        self.WPiece.append(Piece("W", "Knight", "G1", self))
        self.WPiece.append(Piece("W", "Rook", "H1", self))
        self.WPiece.append(Piece("W", "Pawn", "A2", self))
        self.WPiece.append(Piece("W", "Pawn", "B2", self))
        self.WPiece.append(Piece("W", "Pawn", "C2", self))
        self.WPiece.append(Piece("W", "Pawn", "D2", self))
        self.WPiece.append(Piece("W", "Pawn", "E2", self))
        self.WPiece.append(Piece("W", "Pawn", "F2", self))
        self.WPiece.append(Piece("W", "Pawn", "G2", self))
        self.WPiece.append(Piece("W", "Pawn", "H2", self))
        self.WKing = self.WPiece[4]

        #Creating all Black Pieces and adding them to the PieceList
        self.BPiece.append(Piece("B", "Rook", "A8", self))
        self.BPiece.append(Piece("B", "Knight", "B8", self))
        self.BPiece.append(Piece("B", "Bishop", "C8", self))
        self.BPiece.append(Piece("B", "Queen", "D8", self))
        self.BPiece.append(Piece("B", "King", "E8", self))
        self.BPiece.append(Piece("B", "Bishop", "F8", self))
        self.BPiece.append(Piece("B", "Knight", "G8", self))
        self.BPiece.append(Piece("B", "Rook", "H8", self))
        self.BPiece.append(Piece("B", "Pawn", "A7", self))
        self.BPiece.append(Piece("B", "Pawn", "B7", self))
        self.BPiece.append(Piece("B", "Pawn", "C7", self))
        self.BPiece.append(Piece("B", "Pawn", "D7", self))
        self.BPiece.append(Piece("B", "Pawn", "E7", self))
        self.BPiece.append(Piece("B", "Pawn", "F7", self))
        self.BPiece.append(Piece("B", "Pawn", "G7", self))
        self.BPiece.append(Piece("B", "Pawn", "H7", self))
        self.BKing = self.BPiece[4]

    def MakeMove(self, From, To, Turtle = None):
        '''Move piece to a new board position'''

        #Delete captured pieces
        if [From, To] in self.WMoves or [From, To] in self.BMoves:
            for Piece in self.WPiece:
                if Piece.Position == To:
                    self.WPiece.remove(Piece)
                    
            for Piece in self.BPiece:
                if Piece.Position == To:
                    self.BPiece.remove(Piece)
                
            for Piece in self.WPiece:
                if Piece.Position == From:
                    Piece.Move(To)

            for Piece in self.BPiece:
                if Piece.Position == From:
                    Piece.Move(To)
            if Turtle != None:
                From = PosToCoord(From)
                To = PosToCoord(To)
                Buffer = []
                for Value in From:
                    Value -= 1
                    Buffer.append(Value)
                From = Buffer
                Buffer = []
                for Value in To:
                    Value -= 1
                    Buffer.append(Value)
                To = Buffer
                if Turtle.Get(To[0], To[1]) != None:
                    Turtle.Get(To[0], To[1]).hideturtle()
                    Turtle.Set(None, To[0], To[1])
                Chess_Turtle.MovePiece(Turtle.Get(From[0], From[1]), To[0], To[1])
                Turtle.Set(Turtle.Get(From[0], From[1]), To[0], To[1])
                Turtle.Set(None, From[0], From[1])
            return True
        else:
            return False
            print("Invalid")

    def GetMoves(self):
        '''Get moves of all pieces on the board'''
        for each in self.WPiece:
            each.GetMoves()
        for each in self.BPiece:
            each.GetMoves()

        self.ListMoves()

    def GetPieceType(self, Pos):
        '''Get a piece's type from it's board position'''
        for Piece in self.WPiece:
            if Piece.Position == Pos:
                return Piece.Type
            
        for Piece in self.BPiece:
            if Piece.Position == Pos:
                return Piece.Type

    def IsWhiteCheck(self):
        '''Checks if White's king is in check'''
        for Piece in self.BPiece:
            if self.WKing.Position in Piece.Moves:
                return True
        return False

    def IsBlackCheck(self):
        '''Checks if Black's king is in check'''
        for Piece in self.WPiece:
            if self.BKing.Position in Piece.Moves:
                return True
        return False

    def ListMoves(self):
        self.WMoves = []
        self.BMoves = []
        for Piece in self.WPiece:
            Piece.ListMoves(self.WMoves)
        for Piece in self.BPiece:
            Piece.ListMoves(self.BMoves)

        self.CheckWhiteMoves()
        self.CheckBlackMoves()

    def CheckWhiteMoves(self):
        WhiteMoves = []
        for Move in self.WMoves:
            Board = copy.deepcopy(self)
            Board.MakeMove(Move[0], Move[1])
            if Board.IsWhiteCheck() == False:
                WhiteMoves.append(Move)

        self.WMoves = WhiteMoves

    def CheckBlackMoves(self):
        BlackMoves = []
        for Move in self.BMoves:
            Board = copy.deepcopy(self)
            Board.MakeMove(Move[0], Move[1])
            if Board.IsBlackCheck() == False:
                BlackMoves.append(Move)

        self.BMoves = BlackMoves
            
    def GetValue(self):
        BlackCount = len(self.BMoves)
        WhiteCount = len(self.WMoves)
        return BlackCount-WhiteCount
    



class Piece:
    def __init__(self, Team, PieceType, Position, BoardRef):
        '''("B" or "W", "Pawn" "Rook" etc, "A1" - "H8", Reference for Board Object)'''
        self.Type = PieceType
        self.Position = Position
        self.Team = Team
        self.Board = BoardRef
    
    def Move(self, Position):
        if self.Team == "W":
            self.Board.Whites.remove(self.Position)
            self.Position = Position
            self.Board.Whites.append(self.Position)
            
        if self.Team == "B":
            self.Board.Blacks.remove(self.Position)
            self.Position = Position
            self.Board.Blacks.append(self.Position)

    def GetMoves(self):
        '''Gets all moves that this piece can make'''

        #Clear/Create the list to store all moves the piece can make
        self.Moves = []
        
        #Get the Column and Row that the piece is on as an integer value
        #as many pieces can use loops to get all possible moves
        CColumn, CRow = PosToCoord(self.Position)

####WHITES####        
        if self.Team == "W":
            if self.Type == "Pawn":

                #Pawns can move one position forward
                Move = AddToBoard(self.Position, 0, 1)
                if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                    self.Moves.append(Move)

                    #If the White Pawn is on the Second row, it is on it's first move
                    #and can therefore move 2 spaces forward
                    if CRow == 2:
                        Move = AddToBoard(self.Position, 0, 2)
                        if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                            self.Moves.append(Move)

                #Checking if any pieces can be taken by the pawn
                Move = AddToBoard(self.Position, 1, 1)
                if Move in self.Board.Blacks:
                    self.Moves.append(Move)

                Move = AddToBoard(self.Position, -1, 1)
                if Move in self.Board.Blacks:
                    self.Moves.append(Move)
        
            #Queens movements contain the same pattern as Rooks movements
            if self.Type == "Rook" or self.Type == "Queen":

                #Checking all moves upwards
                i = 1
                while i < (9 - CRow):
                    Move = AddToBoard(self.Position, i, 0)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    #If the move is an attack on a Black piece, no further moves in that direction can be made
                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        i = 8

                    #If the move collides with a White Piece, we don't add it to the list and we don't continue down that path
                    if (Move in self.Board.Whites) or (Move != ValidPos(Move)):
                        i = 8

                    i += 1

                #Checking all moves to the right
                j = 1
                while j < (9-CColumn):
                    Move = AddToBoard(self.Position, 0, j)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)
                        
                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        j = 8

                    if (Move in self.Board.Whites) or (Move != ValidPos(Move)):
                        j = 8

                    j += 1

                #Checking all moves downwards
                i = -1
                while i > (-CRow):
                    Move = AddToBoard(self.Position, i, 0)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)
                        
                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        i = -8

                    if (Move in self.Board.Whites) or (Move != ValidPos(Move)):
                        i = -8

                    i -= 1

                #Checking all moves to the left
                j = -1
                while j > (-CColumn):
                    Move = AddToBoard(self.Position, 0, j)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)
                        
                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        j = -8

                    if (Move in self.Board.Whites) or (Move != ValidPos(Move)):
                        j = -8

                    j -= 1

            #Queens movement patterns also contain the pattern of Bishop movements
            if self.Type == "Bishop" or self.Type == "Queen":

                #This is very similar to the Rook movement algorithm however this one compares 2 directions
                #as Bishops move in diagonals so I don't want to go off the board at any point
                #Top Right
                i = 1
                j = 1
                while i < (9-CRow) and j < (9-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        i = 8
                        j = 8

                    if Move in self.Board.Whites:
                        i = 8
                        j = 8

                    i += 1
                    j += 1
                
                #Bottom Right
                i = -1
                j = 1
                while i > (-CRow) and j < (9-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        i = -8
                        j = 8

                    if Move in self.Board.Whites:
                        i = -8
                        j = 8

                    i -= 1
                    j += 1
                    
                #Bottom Left
                i = -1
                j = -1
                while i > (-CRow) and j > (-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        i = -8
                        j = -8

                    if Move in self.Board.Whites:
                        i = -8
                        j = -8

                    i -= 1
                    j -= 1
                    
                #Top Left
                i = 1
                j = -1
                while i < (9-CRow) and j > (-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Blacks:
                        self.Moves.append(Move)
                        i = 8
                        j = -8

                    if Move in self.Board.Whites:
                        i = 8
                        j = -8

                    i += 1
                    j -= 1

            #Kings can move to any of the 8 squares around them
            if self.Type == "King":
                #TR
                Move = AddToBoard(self.Position, 1, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #CR        
                Move = AddToBoard(self.Position, 1, 0)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #BR        
                Move = AddToBoard(self.Position, 1, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #BM        
                Move = AddToBoard(self.Position, 0, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #BL        
                Move = AddToBoard(self.Position, -1, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #CL        
                Move = AddToBoard(self.Position, -1, 0)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #TL        
                Move = AddToBoard(self.Position, -1, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #TM        
                Move = AddToBoard(self.Position, 0, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)

            #Knights can move either 2 horizontally and 1 vertically or vice versa
            if self.Type == "Knight":
                #UL
                Move = AddToBoard(self.Position, -1, 2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #UR
                Move = AddToBoard(self.Position, 1, 2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #RU
                Move = AddToBoard(self.Position, 2, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #RD
                Move = AddToBoard(self.Position, 2, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #DR
                Move = AddToBoard(self.Position, 1, -2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #DL
                Move = AddToBoard(self.Position, -1, -2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #LD
                Move = AddToBoard(self.Position, -2, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)
                #LU
                Move = AddToBoard(self.Position, -2, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Whites:
                        self.Moves.append(Move)

####BLACKS####
        if self.Team == "B":
            if self.Type == "Pawn":

                #Pawns can move one position forward
                Move = AddToBoard(self.Position, 0, -1)
                if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                    self.Moves.append(Move)

                    #If the Black Pawn is on the Seventh Rank, it is on it's first move
                    #and can therefore move 2 spaces forward
                    if CRow == 7:
                        Move = AddToBoard(self.Position, 0, -2)
                        if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                            self.Moves.append(Move)

                #Checking if any pieces can be taken by the pawn
                Move = AddToBoard(self.Position, 1, -1)
                if Move in self.Board.Whites:
                    self.Moves.append(Move)

                Move = AddToBoard(self.Position, -1, -1)
                if Move in self.Board.Whites:
                    self.Moves.append(Move)
        
            #Queens movements contain the same pattern as Rooks movements
            if self.Type == "Rook" or self.Type == "Queen":

                #Checking all moves upwards
                i = 1
                while i < (9 - CRow):
                    Move = AddToBoard(self.Position, i, 0)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    #If the move is an attack on a White piece, no further moves in that direction can be made
                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        i = 8

                    #If the move collides with a Black Piece, we don't add it to the list and we don't continue down that path
                    if (Move in self.Board.Blacks):
                        i = 8

                    i += 1

                #Checking all moves to the right
                j = 1
                while j < (9-CColumn):
                    Move = AddToBoard(self.Position, 0, j)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)
                        
                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        j = 8

                    if (Move in self.Board.Blacks):
                        j = 8

                    j += 1

                #Checking all moves downwards
                i = -1
                while i > (-CRow):
                    Move = AddToBoard(self.Position, i, 0)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)
                        
                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        i = -8

                    if (Move in self.Board.Blacks):
                        i = -8

                    i -= 1

                #Checking all moves to the left
                j = -1
                while j > (-CColumn):
                    Move = AddToBoard(self.Position, 0, j)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)
                        
                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        j = -8

                    if (Move in self.Board.Blacks):
                        j = -8

                    j -= 1

            #Queens movement patterns also contain the pattern of Bishop movements
            if self.Type == "Bishop" or self.Type == "Queen":

                #This is very similar to the Rook movement algorithm however this one compares 2 directions
                #as Bishops move in diagonals so I don't want to go off the board at any point
                #Top Right
                i = 1
                j = 1
                while i < (9-CRow) and j < (9-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        i = 8
                        j = 8

                    if Move in self.Board.Blacks:
                        i = 8
                        j = 8

                    i += 1
                    j += 1
                
                #Bottom Right
                i = -1
                j = 1
                while i > (-CRow) and j < (9-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        i = -8
                        j = 8

                    if Move in self.Board.Blacks:
                        i = -8
                        j = 8

                    i -= 1
                    j += 1
                    
                #Bottom Left
                i = -1
                j = -1
                while i > (-CRow) and j > (-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        i = -8
                        j = -8

                    if Move in self.Board.Blacks:
                        i = -8
                        j = -8

                    i -= 1
                    j -= 1
                    
                #Top Left
                i = 1
                j = -1
                while i < (9-CRow) and j > (-CColumn):
                    Move = AddToBoard(self.Position, j, i)
                    if (Move not in self.Board.Whites) and (Move not in self.Board.Blacks):
                        self.Moves.append(Move)

                    if Move in self.Board.Whites:
                        self.Moves.append(Move)
                        i = 8
                        j = -8

                    if Move in self.Board.Blacks:
                        i = 8
                        j = -8

                    i += 1
                    j -= 1

            #Kings can move to any of the 8 squares around them
            if self.Type == "King":
                #TR
                Move = AddToBoard(self.Position, 1, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #CR        
                Move = AddToBoard(self.Position, 1, 0)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #BR        
                Move = AddToBoard(self.Position, 1, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #BM        
                Move = AddToBoard(self.Position, 0, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #BL        
                Move = AddToBoard(self.Position, -1, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #CL        
                Move = AddToBoard(self.Position, -1, 0)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #TL        
                Move = AddToBoard(self.Position, -1, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #TM        
                Move = AddToBoard(self.Position, 0, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)

            #Knights can move either 2 horizontally and 1 vertically or vice versa
            if self.Type == "Knight":
                #UL
                Move = AddToBoard(self.Position, -1, 2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #UR
                Move = AddToBoard(self.Position, 1, 2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #RU
                Move = AddToBoard(self.Position, 2, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #RD
                Move = AddToBoard(self.Position, 2, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #DR
                Move = AddToBoard(self.Position, 1, -2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #DL
                Move = AddToBoard(self.Position, -1, -2)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #LD
                Move = AddToBoard(self.Position, -2, -1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)
                #LU
                Move = AddToBoard(self.Position, -2, 1)
                if Move == ValidPos(Move):
                    if Move not in self.Board.Blacks:
                        self.Moves.append(Move)




    def ListMoves(self, List):
        for Move in self.Moves:
            if Move == ValidPos(Move):
                List.append([self.Position, Move])


        

class ArtificialAgent:
    '''The actual opposition'''
    def __init__(self, Board):
        self.Board = Board

    def MakeBestMove(self):
        '''MiniMax algorithm to figure out which move is best'''
        #It's impossible for white to ever have the ability to make 200 moves so this value will never be seen as the best
        BaseVal = -200

        for Move in self.Board.BMoves:
            TestBoard = copy.deepcopy(self.Board)
            TestBoard.MakeMove(Move[0], Move[1])
            TestBoard.GetMoves()
            if TestBoard.GetValue() > BaseVal:
                BestMove = Move
                BaseVal = TestBoard.GetValue()

        self.Board.MakeMove(BestMove[0], BestMove[1])
        print(BestMove[0], ", ", BestMove[1])


    def MMMax(self, Board, Depth, CurrentDepth, Alpha, Beta):
        Board.GetMoves()
        Utility = -200
        Current = len(Board.BMoves)
        if Current == 0:
            return Utility

        if Depth == CurrentDepth:
            return Board.GetValue()

        for Move in Board.BMoves:
            Check = copy.deepcopy(Board)
            Check.MakeMove(Move[0], Move[1])
            Temp = self.MMMin(Check, Depth, CurrentDepth+1, Alpha, Beta)
            if Temp > Utility:
                Utility = Temp
                if CurrentDepth == 1:
                    BestMove = Move
            if Temp >= Beta:
                return Utility
            if Temp > Alpha:
                Alpha = Temp
        if CurrentDepth == 1:
            return BestMove
        
        return Utility

    def MMMin(self, Board, Depth, CurrentDepth, Alpha, Beta):
        Board.GetMoves()
        Utility = 200
        Current = len(Board.BMoves)
        if Current == 0:
            return Utility

        if Depth == CurrentDepth:
            return Board.GetValue()

        for Move in Board.WMoves:
            Check = copy.deepcopy(Board)
            Check.MakeMove(Move[0], Move[1])
            Temp = self.MMMax(Check, Depth, CurrentDepth+1, Alpha, Beta)
            if Temp < Utility:
                Utility = Temp
                if CurrentDepth == 1:
                    BestMove = Move
            if Temp <= Alpha:
                return Utility
            if Temp < Beta:
                Beta = Temp
        if CurrentDepth == 1:
            return BestMove
        
        return Utility
        
    def Move(self, Turtles):
        Move = self.MMMax(self.Board, 2, 1, -200, 200)
        self.Board.MakeMove(Move[0], Move[1], Turtles)
        print(Move)







a = Board()
TurtleList = Chess_Turtle.LoadGame()
AI = ArtificialAgent(a)
a.GetMoves()

while len(a.WMoves) > 0 and len(a.BMoves) > 0:
    Result = False
    while Result == False:
        PlayerFrom = input("From:")
        PlayerTo = input("To: ")
        Result = a.MakeMove(PlayerFrom, PlayerTo, TurtleList)
    a.GetMoves()
    AI.Move(TurtleList)
    a.GetMoves()






