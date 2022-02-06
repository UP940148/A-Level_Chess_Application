import math
import copy
class Matrix:
    '''A Matrix of size NxM'''
    def __init__(self, Rows, Columns):
        self.RowCount = Rows
        self.ColumnCount = Columns
        self.Contents = [[0 for i in range(Columns)] for j in range(Rows)]

    def __add__(MatA, MatB):
        '''Add 2 Matrices (of the same size)'''
        if (MatA.RowCount == MatB.RowCount) and (MatA.ColumnCount == MatB.ColumnCount):
            MatC = Matrix(MatA.RowCount, MatA.ColumnCount)
            for i in range(MatA.RowCount):
                for j in range(MatA.ColumnCount):
                    Val = MatA.GetVal(i, j) + MatB.GetVal(i, j)
                    MatC.SetVal(i, j, Val)
            return MatC

    def __sub__(MatA, MatB):
        '''Subract a Matrix from another Matrix (of the same size)'''
        if (MatA.RowCount == MatB.RowCount) and (MatA.ColumnCount == MatB.ColumnCount):
            MatC = Matrix(MatA.RowCount, MatA.ColumnCount)
            for i in range(MatA.RowCount):
                for j in range(MatA.ColumnCount):
                    Val = MatA.GetVal(i, j) - MatB.GetVal(i, j)
                    MatC.SetVal(i, j, Val)
            return MatC

    def __mul__(MatA, MatB):
        if type(MatB) == Matrix:
            if MatA.ColumnCount != MatB.RowCount:
                return None
            else:
                MatC = Matrix(MatA.RowCount, MatB.ColumnCount)

                for ARow in range(MatA.RowCount):
                    for BColumn in range(MatB.ColumnCount):
                        for BRow in range(MatB.RowCount):
                            #A really ugly way of incrementing the value in the Answer Matrix#
                            MatC.SetVal(ARow, BColumn, MatC.GetVal(ARow, BColumn) + MatA.GetVal(ARow, BRow) * MatB.GetVal(BRow, BColumn))

                return MatC
                    
                    

    def Fill(self):
        '''Set Values via the Console'''
        for i in range(self.RowCount):
            for j in range(self.ColumnCount):
                self.Contents[i][j] = float(input("(" + str(i) + ", " + str(j) + "): "))

    def GetDet(self):
        '''Returns the Determinant of any Square Matrix'''
        if self.RowCount == self.ColumnCount:
            
            if self.RowCount == 1:
                Det = self.Contents[0][0]
                return Det
            
            Det = 0
            #Create Matrix of Minors    
            for Column in range(self.ColumnCount):
                    
                MatA = Matrix(self.RowCount -1, self.ColumnCount -1)
                
                H = 0
                for i in range(self.RowCount):
                    if i != 0:
                        W = 0
                        for j in range(self.ColumnCount):
                            if j  != Column:
                                MatA.SetVal(H, W, self.GetVal(i, j))
                                
                                
                                W += 1

                        H += 1
                if float(self.GetVal(0, Column)) != 0:
                    if Column % 2 == 0:
                        Det += (float(self.GetVal(0, Column))*float(MatA.GetDet()))
                    else:
                        Det -= (float(self.GetVal(0, Column))*float(MatA.GetDet()))
                else:
                    Det += 0

                del MatA
                    
            

            return Det

    def GetVal(self, Row, Column):
        return self.Contents[Row][Column]

    def SetVal(self, Row, Column, Value):
        self.Contents[Row][Column] = Value

    def DisplaySelf(self):
        for Row in self.Contents:
            print(Row)

    def Exponent(self, Exp):
        Exp = int(Exp)
        if Exp < 2 or (self.RowCount != self.ColumnCount):
            return None
        else:
            Result = self
            for i in range(Exp-1):
                Result = MultiplyMat(Result, self)
                
            return Result

    def SetRandom(self):
        import random
        for i in range(self.RowCount):
            for j in range(self.ColumnCount):
                self.SetVal(i, j, random.randint(-5, 5))
        del random

    def SetIdentity(self):
        if self.RowCount == self.ColumnCount:
            for i in range(self.RowCount):
                for j in range(self.ColumnCount):
                    if i == j:
                        self.SetVal(i, j, 1)
                    else:
                        self.SetVal(i, j, 0)
        else:
            return "Only Square Matrix Can Be Identity"
                


'''Matrix Maths'''

def MultiplyMat(MatA, MatB):
    if MatA.ColumnCount != MatB.RowCount:
        return None
    else:
        MatC = Matrix(MatA.RowCount, MatB.ColumnCount)

        for ARow in range(MatA.RowCount):
                for BColumn in range(MatB.ColumnCount):
                    for BRow in range(MatB.RowCount):
                        #A really ugly way of incrementing the value in the Answer Matrix#
                        MatC.SetVal(ARow, BColumn, MatC.GetVal(ARow, BColumn) + MatA.GetVal(ARow, BRow) * MatB.GetVal(BRow, BColumn))

        return MatC
                    
        

class Vector:
    def __init__(self, i, j, k = 0):
        self.Store = [i, j, k]
        self.Mod = math.sqrt((i**2) + (j**2) + (k**2))

    def __add__(self, b):
        c = Vector(self(0), self(1), self(2))
        for i in range(3):
            c.Store[i] += b.GetVal(i)
        return c

    def __sub__(self, b):
        c = Vector(self(0), self(1), self(2))
        for i in range(3):
            c.Store[i] -= b.GetVal(i)
        return c

    def __mul__(Vect, Scalar):
        i = Vect.GetVal(0) * Scalar
        j = Vect.GetVal(1) * Scalar
        k = Vect.GetVal(2) * Scalar
        Result = Vector(i, j, k)
        return Result

    def __rmul__(Vect, Mult):
        if type(Mult) ==(int or float):
            return Vect * Mult
        
        if type(Mult) == Matrix:
            if Mult.GetColumns == 3:
                MatV = Matrix(3, 1)
                MatV.SetVal(0, 0, Vect.GetVal(0))
                MatV.SetVal(1, 0, Vect.GetVal(1))
                MatV.SetVal(2, 0, Vect.GetVal(2))
                return Mult * MatV
                
            if Mult.GetColumns == 2:
                MatV = Matrix(2, 1)
                MatV.SetVal(0, 0, Vect.GetVal(0))
                MatV.SetVal(1, 0, Vect.GetVal(1))
                return Mult * MatV

    def __eq__(self, Other):
        if not isinstance(Other, Vector):
            return False
        if self.GetVal(0) != Other.GetVal(0):
            return False
        if self.GetVal(1) != Other.GetVal(1):
            return False
        if self.GetVal(2) != Other.GetVal(2):
            return False
        return True

    def __call__(self, x = -1):
        '''Returns value in Store[x],
        if no value entered or x = -1, returns Store as list'''
        if x == -1:
            return self.Store
        for i in range(3):
            if x == i:
                return self.Store[i]

    def __neg__(self):
        return Vector(-self.GetVal(0), -self.GetVal(1), -self.GetVal(2))
        
    def GetMod(self):
        return self.Mod
        
    def GetSelf(self):
        return self.Store

    def GetVal(self, Pos):
        return self.Store[Pos]

    def IsEqual(self, Vector):
        for i in range(0, 2):
            if Vector.Store[i] != self.Store[i]:
                return False


'''Vector Maths'''

def Dot(VectA, VectB):
    a = VectA.GetSelf()
    b = VectB.GetSelf()
    Total = 0
    for i in range(3):
        Total += a[i]*b[i]
    return Total

def Scalar(VectA, VectB):
    '''Will find the Angle in Radians between two Vectors'''
    #Definition: a.b = |a||b|Cos(Theta)#
    DotProd = Dot(VectA, VectB)
    ModA = VectA.GetMod()
    ModB = VectB.GetMod()
    return math.acos(DotProd/(ModA*ModB))

    
def Cross(VectA, VectB):
    MatI = Matrix(2, 2)
    MatI.SetVal(0, 0, VectA.GetVal(1))
    MatI.SetVal(0, 1, VectA.GetVal(2))
    MatI.SetVal(1, 0, VectB.GetVal(1))
    MatI.SetVal(1, 1, VectB.GetVal(2))

    MatJ = Matrix(2, 2)
    MatJ.SetVal(0, 0, VectA.GetVal(0))
    MatJ.SetVal(0, 1, VectA.GetVal(2))
    MatJ.SetVal(1, 0, VectB.GetVal(0))
    MatJ.SetVal(1, 1, VectB.GetVal(2))

    MatK = Matrix(2, 2)
    MatK.SetVal(0, 0, VectA.GetVal(0))
    MatK.SetVal(0, 1, VectA.GetVal(1))
    MatK.SetVal(1, 0, VectB.GetVal(0))
    MatK.SetVal(1, 1, VectB.GetVal(1))

    I = MatI.GetDet()
    J = -MatJ.GetDet()
    K = MatK.GetDet()

    VectC = Vector(I, J, K)

    return VectC

def IsCollinear(a, b):
    #If any of these 3 cases are true, the vectors are not collinear
    #Checking this now means we don't risk dividing by zero in the next step
    if (a.Store[2] == 0 and b.Store[2] !=0) or (a.Store[2] != 0 and b.Store[2] == 0):
        return False
    if (a.Store[1] == 0 and b.Store[1] !=0) or (a.Store[1] != 0 and b.Store[1] == 0):
        return False
    if (a.Store[0] == 0 and b.Store[0] !=0) or (a.Store[0] != 0 and b.Store[0] == 0):
        return False

    Scalar = a.Store[0] / b.Store[0]
    for i in range(1,2):
        if a.Store[i] / Scalar != b.Store[i]:
            return False
    return True

def GetVector(PosA, PosB):
    i = PosB.Store[0] - PosA.Store[0]
    j = PosB.Store[1] - PosA.Store[1]
    k = PosB.Store[2] - PosA.Store[2]
    return Vector(i, j, k)
    

class Line:
    def __init__(self, Position, Direction):
        self.Pos = Position
        self.Dir = Direction

    def DoesMeet(self, Point):
        Range = Point.Store[0] - self.Pos.Store[0]
        Check = self.Pos + Range * self.Dir
        if Check.Store == Point.Store:
            return True
        return False

def GetSmallest(Value1, Value2):
    '''Returns the smallest of two numbers'''
    if not isinstance(Value1, int) and not isinstance(Value1, float):
        print("Bad Value 'Value1':", Value1)
        print("Can only compare numbers")
        raise TypeError
    if not isinstance(Value2, int) and not isinstance(Value2, float):
        print("Bad Value 'Value2':", Value2)
        print("Can only compare numbers")
        raise TypeError
    if Value1 <= Value2:
        return Value1
    else:
        return Value2

def GetLargest(Value1, Value2):
    '''Returns the largest of two numbers'''
    if not isinstance(Value1, int) and not isinstance(Value1, float):
        print("Bad Value 'Value1':", Value1)
        print("Can only compare numbers")
        raise TypeError
    if not isinstance(Value2, int) and not isinstance(Value2, float):
        print("Bad Value 'Value2':", Value2)
        print("Can only compare numbers")
        raise TypeError
    if Value1 >= Value2:
        return Value1
    else:
        return Value2





                 
