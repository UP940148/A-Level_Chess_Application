import Maths_Library as MyMaths
import Chess_Turtle as Graphics
import copy

'''Start working on move validation. Create a list of all moves that each piece can make, make them submit it back to a main list within the Board Instance'''

_BLACK = 1
_WHITE = 0
NUMS = ["1", "2", "3", "4", "5", "6", "7", "8"]
CHARS = ["A", "B", "C", "D", "E", "F", "G", "H"]

def VectToRef(VectA: MyMaths.Vector):
    #Parameter Checking
    #I plan to use lots of Error checking in my code so that if a bug occurs, I can easily find out what it was and where it occurred
    if not isinstance(VectA, MyMaths.Vector):
        print("Bad Value 'VectA':", VectA)
        print("Function can only take Vector Parameter")
        raise TypeError
    if VectA(2) != 0:
        print("Bad Value 'VectA':", VectA)
        print("3-Dimensional Vector passed into 2-Dimensional function")
        raise TypeError
    for i in range(2):
        if not isinstance(VectA(i), int):
            print("Bad Value 'VectA':", VectA)
            print("Function can only accept Vectors with integer components")
            raise ValueError
    i = VectA(0)
    j = VectA(1)
    i = chr(ord(str(i)) + 17)
    j = str(j+1)

    return [i, j]

def RefToVect(BoardRef: str):
    if not isinstance(BoardRef, str):
        print("Bad Value 'BoardRef':", BoardRef)
        print("Board Reference must be a list of 2 values")
        raise TypeError
    if len(BoardRef) != 2:
        print("Bad Value 'BoardRef':", BoardRef)
        print("Board Reference must be a list of 2 values")
        raise ValueError
    if BoardRef[0] not in CHARS or BoardRef[1] not in NUMS:
        print("Bad Value 'BoardRef':", BoardRef)
        print("Board Reference must be a capital letter (A-H) followed by a number (1-8)")
        raise ValueError
    i = BoardRef[0]
    j = BoardRef[1]
    i = ord(i) -65
    j = ord(j) -49

    return MyMaths.Vector(i, j)

def IsValidSpace(Move):
    EndPos = Move
    if EndPos(0) < 0 or EndPos(0) > 7 or EndPos(1) < 0 or EndPos(1) > 7:
        return False
    return True

class Board:
    def __init__(self):
        self.WPiece, self.BPiece, self.Whites, self.Blacks, self.WKing, self.BKing = InitialisePieces(self)
        #I created a reference to the Kings so that I can easily check for instances of Check later in the code
        self.GetWMoves()
        self.GetBMoves()
        #I collect all moves when the board is initialised to make it easier to check a move's eligibility#

    def __call__(self):
        ##I made the board callable so that I can just return a deepcopy of it with ease##
        return copy.deepcopy(self)
    
    def GetWMoves(self):
        WMoves = []
        for Piece in self.WPiece:
            Pos, Moves = Piece.GetMoves(self.Whites, self.Blacks)
            for Move in Moves:
                WMoves.append([Pos, Move])
        self.WMoves = [Move for Move in WMoves if IsValidSpace(Move[1]) == True]
            
    def GetBMoves(self):
        BMoves = []
        for Piece in self.BPiece:
            Pos, Moves = Piece.GetMoves(self.Whites, self.Blacks)
            for Move in Moves:
                BMoves.append([Pos, Move])
        self.BMoves = [Move for Move in BMoves if IsValidSpace(Move[1]) == True]

    def IsWhiteCheck(self):
        if self.WKing in self.BMoves:
            return True
        return False

    def IsBlackCheck(self):
        if self.BKing in self.WMoves:
            return True
        return False

    def RemoveWhiteCheck(self):
        ##The Easiest way to find if a piece is in check is by duplicating the board, playing the move, then checking the state##
        GoodMoves = []
        for Move in self.WMoves:
            Clone = self()
            Clone.MakeMove(Move[0], Move[1])
            Clone.GetBMoves()
            if Clone.IsWhiteCheck() != True:
                GoodMoves.append(Move)
        self.WMoves = GoodMoves

    def RemoveBlackCheck(self):
        GoodMoves = []
        for Move in self.BMoves:
            Clone = self()
            Clone.MakeMove(Move[0], Move[1])
            Clone.GetWMoves()
            if Clone.IsBlackCheck() != True:
                GoodMoves.append(Move)
        self.BMoves = GoodMoves

    def GetVal(self):
        return len(self.BMoves) - len(self.WMoves)
                
    def MakeMove(self, Start: MyMaths.Vector, End: MyMaths.Vector):
        #This function will take move details and convert that to game logic
        #First it will error check the parameters, convert the positions into a vector with specific start point
        #Then it will change the Piece position value to the new position, and move the Piece on the Turtle Board
        if not isinstance(Start, MyMaths.Vector):
            print("Bad Value 'Start':", Start)
            print("Position must be in Vector format")
            raise TypeError
        if not isinstance(End, MyMaths.Vector):
            print("Bad Value 'End':", End)
            print("Position must be in Vector form")
            raise TypeError

        IsValid = False

        if Start in self.Whites:
            for Move in self.WMoves:
                if Move[0] == Start and Move[1] == End:
                    IsValid = True
                    for Pos in self.Whites:
                        if Pos == Start:
                            Pos.Store = End()
                    break
                
        elif Start in self.Blacks:
            for Move in self.BMoves:
                if Move[0] == Start and Move[1] == End:
                    IsValid = True
                    for Pos in self.Blacks:
                        if Pos == Start:
                            Pos.Store = End()
                    break
                
        if IsValid == False:
            return False

        return True

        
                
        
    
        

class Piece:
    def __init__(self, MyBoard: Board, Type: str, Team: int, Position: MyMaths.Vector, MoveVectors: list, AttackVectors: list):
        '''Makes sure all parameters are valid and then creates a piece'''
        #I plan to use lots of Error checking in my code so that if a bug occurs, I can easily find out what it was and where it occurred
        if not isinstance(MyBoard, Board):
            print("Bad Value 'MyBoard':", MyBoard)
            print("Board must use 'Board' class as datatype")
            raise TypeError
        if not isinstance(Type, str):
            print("Bad Value 'Type':", Type)
            print("Piece type must be a string")
            raise TypeError
        if not isinstance(Team, int) or (Team != 1 and Team !=0):
            print("Bad Value 'Team':", Team)
            print("Team must be an Integer. Either 0 or 1")
            raise TypeError
        if not isinstance(Position, MyMaths.Vector):
            print("Bad Value 'Position':", Position)
            print("Position must be in vector form")
            raise TypeError
        if not isinstance(MoveVectors, list):
            print("Bad Value 'MoveVectors':", MoveVectors)
            print("Move Vectors must be presented as a list")
            raise TypeError
        if not isinstance(AttackVectors, list):
            print("Bad Value 'AttackVectors':", AttackVectors)
            print("Attack Vectors must be presented as a list")
            raise TypeError
        self.Board = MyBoard
        self.Type = Type
        self.Team = Team
        self.Position = Position
        self.MoveVectors = MoveVectors
        self.AttackVectors = AttackVectors

    def __eq__(self, other):
        if not isinstance(other, MyMaths.Vector):
            return False
        if self.Position != other:
            return False
        return True

    def __call__(self):
        return self.Type

    def GetMoves(self, Whites, Blacks):
        '''This will collect all moves that this piece can make and return them in a list'''
        if not isinstance(Whites, list):
            print("Bad Value 'Whites':", Whites)
            print("Piece Locations must be in list form")
            raise TypeError
        if not isinstance(Blacks, list):
            print("Bad Value 'Blacks':", Blacks)
            print("Piece Locations must be in list form")
            raise TypeError
        ##'MyMoves' is to store all moves that this piece determines it can make##
        ##'ShouldBreak' is going to be used for the Rook, Bishop, and Queen. It will allow-##
        ##-me to track whether the last move was on a piece or not and will break-##
        ##-in next loop cycle##
        MyMoves = []
        ShouldBreak = False
        if self.Type == "Pawn":
            if self.Team == _WHITE:
                ##Attack##
                for Vect in self.AttackVectors:
                    CurrentMove = self.Position + Vect
                    if CurrentMove in Blacks:
                        MyMoves.append(CurrentMove)
                ##Move##
                CurrentMove = self.Position + self.MoveVectors[0]
                if CurrentMove not in Whites:
                    if CurrentMove not in Blacks:
                        MyMoves.append(CurrentMove)
                        if self.Position(1) == 1:
                            CurrentMove = self.Position + 2 * self.MoveVectors[0]
                            if CurrentMove not in Whites:
                                if CurrentMove not in Blacks:
                                    MyMoves.append(CurrentMove)

            if self.Team == _BLACK:
                ##Attack##
                for Vect in self.AttackVectors:
                    CurrentMove = self.Position - Vect
                    if CurrentMove in Whites:
                        MyMoves.append(CurrentMove)
                ##Move##
                CurrentMove = self.Position - self.MoveVectors[0]
                if CurrentMove not in Whites:
                    if CurrentMove not in Blacks:
                        MyMoves.append(CurrentMove)
                        if self.Position(1) == 6:
                            CurrentMove = self.Position - 2 * self.MoveVectors[0]
                            if CurrentMove not in Whites:
                                if CurrentMove not in Blacks:
                                    MyMoves.append(CurrentMove)

        elif self.Type == "King" or self.Type == "Knight":
            ##-Knights and Kings have the same logic as both have attack vectors-##
            ##-identical to their move vectors, and both can only move a magnitude-##
            ##-of one of their vector/s##
            if self.Team == _WHITE:
                for Vect in self.MoveVectors:
                    CurrentMove = self.Position + Vect
                    if CurrentMove not in Whites:
                        MyMoves.append(CurrentMove)
                    CurrentMove = self.Position - Vect
                    if CurrentMove not in Whites:
                        MyMoves.append(CurrentMove)
                        
            if self.Team == _BLACK:
                for Vect in self.MoveVectors:
                    CurrentMove = self.Position + Vect
                    if CurrentMove not in Blacks:
                        MyMoves.append(CurrentMove)
                    CurrentMove = self.Position - Vect
                    if CurrentMove not in Blacks:
                        MyMoves.append(CurrentMove)
                        
        else:
            if self.Team == _WHITE:
                for Vect in self.MoveVectors:
                    ##I use 7 because it's the smallest value that will always ensure that-##
                    ##-the whole board is covered in all directions##
                    for i in range(1, 7):
                        CurrentMove = self.Position + i*Vect
                        if CurrentMove in Whites:
                            ##A##
                            ##We can't take or pass over our own pieces##
                            break
                        elif ShouldBreak == True:
                            ##B##
                            ##If our last move was on an opposing piece, we can make no further move this way##
                            ShouldBreak = False
                            break
                        elif CurrentMove not in Blacks:
                            ##C##
                            ##This must be a blank tile and we can't have gone over any pieces else the-##
                            ##-loop would have broken##
                            MyMoves.append(CurrentMove)
                        elif CurrentMove in Blacks:
                            ##D##
                            ##Add move to list because it will take a piece, but then break the loop next time-##
                            ##-before adding another move##
                            MyMoves.append(CurrentMove)
                            ShouldBreak = True
                            
                    ##This for loop is used for the opposites of the moves calculated above##        
                    for i in range(1, 7):
                        CurrentMove = self.Position - i*Vect
                        if CurrentMove in Whites:
                            ##A##
                            break
                        elif ShouldBreak == True:
                            ##B##
                            ShouldBreak = False
                            break
                        elif CurrentMove not in Blacks:
                            ##C##
                            MyMoves.append(CurrentMove)
                        elif CurrentMove in Blacks:
                            ##D##
                            MyMoves.append(CurrentMove)
                            ShouldBreak = True
            ##The move for blacks is the same as for whites, just searching opposite lists##
            if self.Team == _BLACK:
                for Vect in self.MoveVectors:
                    for i in range(1, 7):
                        CurrentMove = self.Position + i*Vect
                        if CurrentMove in Blacks:
                            ##A##
                            break
                        elif ShouldBreak == True:
                            ##B##
                            ShouldBreak = False
                            break
                        elif CurrentMove not in Whites:
                            ##C##
                            MyMoves.append(CurrentMove)
                        elif CurrentMove in Whites:
                            ##D##
                            MyMoves.append(CurrentMove)
                            ShouldBreak = True

                    ##Again, this for loop calculates the opposite moves##
                    for i in range(1, 7):
                        CurrentMove = self.Position - i*Vect
                        if CurrentMove in Blacks:
                            ##A##
                            break
                        elif ShouldBreak == True:
                            ##B##
                            ShouldBreak = False
                            break
                        elif CurrentMove not in Whites:
                            ##C##
                            MyMoves.append(CurrentMove)
                        elif CurrentMove in Whites:
                            ##D##
                            MyMoves.append(CurrentMove)
                            ShouldBreak = True
            
        return self.Position, MyMoves 


class ArtificialAgent:
    def __init__(self, Board):
        self.Board = Board

    def MMBlack(self, Board, Depth, CurrentDepth, Alpha, Beta):
        Board.GetBMoves()
        Board.RemoveBlackCheck()
        Utility = -10000
        Current = len(Board.BMoves)

        ##If Black Can make no more moves, this node is terminal##
        if Current == 0:
            return Utility

        ##If we've reached our max depth, we return the heuristic value of this move##
        if Depth == CurrentDepth:
            return Board.GetVal()

        for Move in Board.BMoves:
            ##I create a copy of the board to test moves on for the algorithm##
            Check = Board()
            Check.MakeMove(Move[0], Move[1])
            Temp = self.MMWhite(Check, Depth, CurrentDepth + 1, Alpha, Beta)
            ##If the Found value is greater than the Utility, Max will prefer this path##
            if Temp >= Utility:
                Utility = Temp
                ##This means we will always have at least one move that we can make##
                ##I only change this on the top level because we don't need to worry about##
                ##remembering future moves until we get to them##
                if CurrentDepth == 1:
                    BestMove = Move
                ##If Temp is larger than Beta, it means that Min will prefer a different path, this is part-##
                ##of the 'Alpha-Beta' pruning algorithm## 
                if Temp >= Beta:
                    return Utility
                ##If Temp is larger than Alpha, it means we have found a new best alternative for Max##
                if Temp >= Alpha:
                    Alpha = Temp
            ##If we have finished our search, return the best move we have found##
            if CurrentDepth == 1:
                return BestMove

            ##If we haven't finished our search, pass the Utility value back up the algorithm##
            return Utility

    def MMWhite(self, Board, Depth, CurrentDepth, Alpha, Beta):
        Board.GetWMoves()
        Board.RemoveWhiteCheck()
        Utility = 10000
        Current = len(Board.WMoves)

        ##If no moves can be made, node is terminal##
        if Current == 0:
            return Utility

        ##If we've reached max depth, return heuristic##
        if Depth == CurrentDepth:
            return Board.GetVal()

        for Move in Board.WMoves:
            Check = Board()
            Check.MakeMove(Move[0], Move[1])
            Temp = self.MMBlack(Check, Depth, CurrentDepth + 1, Alpha, Beta)

            ##If found value is better than utility, we have a new best value##
            if Temp <= Utility:
                Utility = Temp
                ##If we're at the top level, we have found a best move##
                if CurrentDepth == 1:
                    BestMove = Move
            ##If Temp is less than Alpha, it means that Max will prefer another route##        
            if Temp <= Alpha:
                return Utility
            
            ##If Temp is less than Beta, we've found a best alternative for Min##
            if Temp < Beta:
                Beta = Temp
        ##If we've reached the end of our search, return best Move found##
        if CurrentDepth == 1:
            return BestMove

        return Utility

    def Move(self, MyGUI):
        Move = self.MMBlack(self.Board, 2, 1, -10000, 10000)
        self.Board.MakeMove(Move[0], Move[1])
        MyGUI.MakeMove(Move[0], Move[1])
        
        
            
            
            
        

class GUI:
    def __init__(self):
        self.Turtles = Graphics.LoadGame()
    def MakeMove(self, From, To):
        if not isinstance(From, MyMaths.Vector):
            print("Bad Value 'From':", From)
            print("Positions must be in Vector Form")
            return TypeError
        if not isinstance(To, MyMaths.Vector):
            print("Bad Value 'To':", To)
            print("Positions must be in Vector Form")
            return TypeError
        
        LFrom = From()
        LTo = To()
        print(LFrom[0], LFrom[1])
        Graphics.MovePiece(self.Turtles.Get(LFrom[0], LFrom[1]), LTo[0], LTo[1])
        if self.Turtles.Get(LTo[0], LTo[1]) != None:
            self.Turtles.Get(LTo[0], LTo[1]).hideturtle()
        self.Turtles.Set(self.Turtles.Get(LFrom[0], LFrom[1]), LTo[0], LTo[1])
        self.Turtles.Set(None, LFrom[0], LFrom[1])
        

def InitialisePieces(Board):
    '''Initialise all board pieces with their starting position'''
    Vectors = SetVectors()
    #Create the list of all occupied spaces for each team so that I can easily use them in the creation of pieces.
    #This way, I only need to change the values in this list and it will change the value in the piece's variable as well.
    Whites = [MyMaths.Vector(0, 0), MyMaths.Vector(1, 0), MyMaths.Vector(2, 0), MyMaths.Vector(3, 0), MyMaths.Vector(4, 0), MyMaths.Vector(5, 0), MyMaths.Vector(6, 0), MyMaths.Vector(7, 0), MyMaths.Vector(0, 1), MyMaths.Vector(1, 1), MyMaths.Vector(2, 1), MyMaths.Vector(3, 1), MyMaths.Vector(4, 1), MyMaths.Vector(5, 1), MyMaths.Vector(6, 1), MyMaths.Vector(7, 1)]
    Blacks = [MyMaths.Vector(0, 6), MyMaths.Vector(1, 6), MyMaths.Vector(2, 6), MyMaths.Vector(3, 6), MyMaths.Vector(4, 6), MyMaths.Vector(5, 6), MyMaths.Vector(6, 6), MyMaths.Vector(7, 6), MyMaths.Vector(0, 7), MyMaths.Vector(1, 7), MyMaths.Vector(2, 7), MyMaths.Vector(3, 7), MyMaths.Vector(4, 7), MyMaths.Vector(5, 7), MyMaths.Vector(6, 7), MyMaths.Vector(7, 7)]
    WPiece = []
    BPiece = []
    for i in range(8):
        WPiece.append(Piece(Board, "Pawn", _WHITE, Whites[8+i], Vectors[0], Vectors[1]))
        BPiece.append(Piece(Board, "Pawn", _BLACK, Blacks[i], Vectors[0], Vectors[1]))
        
    ##White Pieces##
    WPiece.append(Piece(Board, "Rook", _WHITE, Whites[0], Vectors[2], Vectors[2]))
    WPiece.append(Piece(Board, "Rook", _WHITE, Whites[7], Vectors[2], Vectors[2]))
    WPiece.append(Piece(Board, "Knight", _WHITE, Whites[1], Vectors[3], Vectors[3]))
    WPiece.append(Piece(Board, "Knight", _WHITE, Whites[6], Vectors[3], Vectors[3]))
    WPiece.append(Piece(Board, "Bishop", _WHITE, Whites[2], Vectors[4], Vectors[4]))
    WPiece.append(Piece(Board, "Bishop", _WHITE, Whites[5], Vectors[4], Vectors[4]))
    WPiece.append(Piece(Board, "King", _WHITE, Whites[4], Vectors[5], Vectors[5]))
    WPiece.append(Piece(Board, "Queen", _WHITE, Whites[3], Vectors[6], Vectors[6]))
    
    ##Black Pieces##
    BPiece.append(Piece(Board, "Rook", _BLACK, Blacks[0], Vectors[2], Vectors[2]))
    BPiece.append(Piece(Board, "Rook", _BLACK, Blacks[7], Vectors[2], Vectors[2]))
    BPiece.append(Piece(Board, "Knight", _BLACK, Blacks[1], Vectors[3], Vectors[3]))
    BPiece.append(Piece(Board, "Knight", _BLACK, Blacks[6], Vectors[3], Vectors[3]))
    BPiece.append(Piece(Board, "Bishop", _BLACK, Blacks[2], Vectors[4], Vectors[4]))
    BPiece.append(Piece(Board, "Bishop", _BLACK, Blacks[5], Vectors[4], Vectors[4]))
    BPiece.append(Piece(Board, "King", _BLACK, Blacks[4], Vectors[5], Vectors[5]))
    BPiece.append(Piece(Board, "Queen", _BLACK, Blacks[3], Vectors[6], Vectors[6]))
    
    return WPiece, BPiece, Whites, Blacks, WPiece[14], BPiece[14]

def SetVectors():
    '''Create the vectors that the pieces can move across and assign them to lists'''
    #I don't need every possible move represented as it's own vector because vectors are bi-directional
    #I've re-used lots of vectors by making copies in the other lists, this is because these vectors should never be altered-
    #- by the program and therefore can be used all throughout as many pieces can move in the same directions as others
    PawnVector = [MyMaths.Vector(0, 1)]
    PawnAttackVectors = [MyMaths.Vector(-1, 1), MyMaths.Vector(1, 1)]
    RookVectors = [PawnVector[0], MyMaths.Vector(1, 0)]
    KnightVectors = [MyMaths.Vector(-2, 1), MyMaths.Vector(-1, 2), MyMaths.Vector(1, 2), MyMaths.Vector(2, 1)]
    BishopVectors = [PawnAttackVectors[0], PawnAttackVectors[1]]
    KingVectors = [PawnAttackVectors[0], PawnVector[0], PawnAttackVectors[1], RookVectors[1]]
    QueenVectors = KingVectors
    #^^I can safely make the King and Queen movement vectors the same because the king will be
    #restricted to a scalar multiple of 1 for movements
    
    return [PawnVector, PawnAttackVectors, RookVectors, KnightVectors, BishopVectors, KingVectors, QueenVectors]

def GetMoveVector(From: MyMaths.Vector, To: MyMaths.Vector):
    '''Gets a vector which represents the move being made on the board'''
    if not isinstance(From, MyMaths.Vector):
        print("Bad Value 'From':", From)
        print("Postions must be in vector form")
        raise TypeError
    if not isinstance(To, MyMaths.Vector):
        print("Bad Value 'To':", To)
        print("Postions must be in vector form")
        raise TypeError
    
    return MyMaths.GetVector(From, To)

def GetPlayerMove():
    FromInput = RefToVect(input("From: "))
    ToInput = RefToVect(input("To: "))
    if IsValidSpace(FromInput):
        if IsValidSpace(ToInput):
            return FromInput, ToInput, True
    return FromInput, ToInput, False


Game = Board()
GameGUI = GUI()
AI = ArtificialAgent(Game)
i = 0
while i == 0:
    Game.GetWMoves()
    Game.RemoveWhiteCheck()
    Valid = False
    while Valid == False:
        StartPos, EndPos, Valid = GetPlayerMove()
    Game.MakeMove(StartPos, EndPos)
    GameGUI.MakeMove(StartPos, EndPos)
    AI.Move(GameGUI)
    
    
    
            


