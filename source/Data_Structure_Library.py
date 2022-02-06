class Array:
        def __init__(self, x, y=0, z=0):
                self.Grid = [[[None for k in range(z+1)] for j in range(y+1)] for i in range(x+1)]

        def Get(self, x, y=0, z=0):
                return self.Grid[x][y][z]

        def Set(self, Value, x, y=0, z=0):
                self.Grid[x][y][z] = Value

class Queue:
        '''Standard Queue'''
        def __init__(self, Size):
                self.Size = Size
                self.Store = [None] * self.Size

        def EnQueue(self, Item):
                if self.IsFull != True:
                        self.Store.append(Item)
                else:
                        return "Surpassed Size"
                

        def DeQueue():
                if self.IsEmpty != True:
                        return self.Store.pop(0)
                else:
                        return None

        def IsFull(self):
                Total = 0
                for Item in self.Store:
                        if Item != None:
                                Total += 1
                if Total == self.Size:
                        return True
                else:
                        return False

        def IsEmpty(self):
                Total = 0
                for Item in self.Store:
                        if Item != None:
                                Total += 1
                if Total == 0:
                        return True
                else:
                        return False
                
class CQueue:
        '''Circular Queue'''
        def __init__(self, Size):
                self.Size = Size
                self.Front = 0
                self.Rear = 0

                self.Store = [None] * self.Size
                
        def EnQueue(self, Item):
                if self.IsFull() != True:
                        self.Store[self.Rear] = Item
                
                        self.Rear += 1
                        self.Rear %= self.Size
                else:
                        return "Surpassed Size"
                
        def DeQueue(self):
                if self.IsEmpty() != True:
                        Item = self.Store[self.Front]
                        self.Store[self.Front] = None
                        
                        self.Front += 1
                        self.Front %= self.Size
                        return Item
                else:
                        return None
        
        def IsFull(self):
                Total = 0
                for Item in self.Store:
                        if Item != None:
                                Total += 1
                if Total == self.Size:
                        return True
                else:
                        return False
                
        def IsEmpty(self):
                Total = 0
                for Item in self.Store:
                        if Item != None:
                                Total += 1
                if Total == 0:
                        return True
                else:
                        return False
                

class PQueue:
        '''Priority Queue'''
        def __init__(self, Size):
                self.Size = Size
                self.Rear = 0
                
                self.Store = [None]*self.Size
                self.Priority = [0]*self.Size

        def EnQueue(self, Item, Priority):
                self.Store[self.Rear] = Item
                self.Priority[self.Rear] = Priority
                self.Rear += 1
                self.Sort()

        def DeQueue(self):
                pass

        def Sort(self):
                Swaps = True
        
                while Swaps == True:
                        Swaps = False
                
                        for i in range(len(self.Store) - 1):
                                if self.Priority[i + 1] != None:
                                        if self.Priority[i] < self.Priority[i + 1]:
                                                Held = self.Store[i]
                                                self.Store[i] = self.Store[i + 1]
                                                self.Store[i + 1] = Held
                                        
                                                Held = self.Priority[i]
                                                self.Priority[i] = self.Priority[i + 1]
                                                self.Priority[i + 1] = Held
                                        
                                                Swaps = True

class Stack:
        def __init__(self):
                self.Store = []

        def AddItem(self, Item):
                self.Store.append(Item)

        def RemoveItem(self):
                if self.GetSize != 0:
                        return self.Store.pop(-1)
                else:
                        return None

        def GetSize(self):
                return len(self.Store)


class Grid:
        def __init__(self, XSize, YSize, Value = None):
                self.XSize = XSize
                self.YSize = YSize
                self.Store = [[Value for i in range(self.XSize)] for j in range(self.YSize)]

        def Set(self, X, Y, Value):
                self.Store[Y][X] = Value

        def Get(self, X, Y):
                return self.Store[Y][X]

        def SetRegion(self, X1, Y1, X2, Y2, Value):
                for i in range(X1, X2+1):
                        for j in range(Y1, Y2+1):
                                self.Set(i, j, Value)

        def Clear(self):
                self.SetRegion(0, 0, self.XSize, self.YSize, None)

        def Fill(self, Value):
                self.SetRegion(0, 0, self.XSize, self.YSize, Value)

        def DeBugShow(self):
                for i in range(self.XSize):
                        Out = ""
                        for j in range(self.YSize):
                                Out += str(self.Get(i, j)) + ", "
                        print(Out)
        

class BTree:
        def __init__(self, Root):
                self.Left = None
                self.Right = None
                self.Me = Root

        def AddNode(self, Value):
                '''Checks the Value and places it correctly in the tree'''
                if Value < self.Me:
                        if self.Left != None:
                                self.Left.AddNode(Value)
                        else:
                                self.Left = BTree(Value)
                else:
                        if self.Right != None:
                                self.Right.AddNode(Value)
                        else:
                                self.Right = BTree(Value)

        def GetInOrder(self):
                '''Returns a list of the node values in numerical order'''
                Result = []
                
                if self.Left != None:
                                for Each in self.Left.GetInOrder():
                                        Result.append(Each)
                                
                Result.append(self.Me)

                if self.Right != None:
                                for Each in self.Right.GetInOrder():
                                        Result.append(Each)

                return Result

        def GetPreOrder(self):
                '''I don't know how to explain this order other than 'Root -> Left -> Right'''
                Result = []
                                
                Result.append(self.Me)
                
                if self.Left != None:
                                for Each in self.Left.GetInOrder():
                                        Result.append(Each)

                if self.Right != None:
                                for Each in self.Right.GetInOrder():
                                        Result.append(Each)

                return Result

        def GetPostOrder(self):
                '''I don't know how to explain this order other than 'Left -> Right -> Root'''
                Result = []
                
                if self.Left != None:
                                for Each in self.Left.GetInOrder():
                                        Result.append(Each)

                if self.Right != None:
                                for Each in self.Right.GetInOrder():
                                        Result.append(Each)
                                
                Result.append(self.Me)

                return Result

