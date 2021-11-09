# Open file to get the playing board
# check to see if playing baord is legal- 9 Knights, 5x4 board, knights are defined as k
# turn board into usuable data 
# start in lower left corner and send position into generator that computes next possible position 
# check if move is legal
# if legal move to next move untill all moves are analyzed
# once all moves analayzed then move to next piece removing that piece from list
# repeat until empty list
#                                                      Possible Moves
# file           0 1 2 3 4          (2, 2) --> (x+-2, y+-1) union (x+-1, y+-2)
#  . . . . k   [[k . . . .], 0                 
#  k . . . .    [. . . . .], 1
#  . k . k .    [. . . . .]  2 
#  k . k . k    [. . . . .]  3
#  k . k . k    [. . . . .]] 4

class NineKnights:
    def __init__(self, file):
        self._data = self.getData(file)
        self._legalBoard = True

    def getData(self, file):
        finished = False
        while finished == False:
            try:
                fileToOpen = open(file)
                data = [list(line.rstrip()) for line in fileToOpen]
                # [[".", "k"...][".", "k"...]...]
                finished = True
            except IOError as error:
                print(error)
            finally:
                fileToOpen.close()
        return data

    def checkBoard(self):
        # Checking to see if board is correct dimensions
        knightsNum = 0
        if len(self._data) == 5:
            for x in range(len(self._data)):
                if len(self._data[x]) == 5:
                    self._legalBoard = True
                    knightsNum += self._data[x].count("k") # get num of knights on board and make sure knights are represented by k
                else:
                    self._legalBoard = False
        else:
            self._legalBoard = False
        if knightsNum != 9:
            self._legalBoard = False
        return self._legalBoard

    def knightPossibleMovement(self, coords):
        # kinda jank wish i could make this a loop :(
        possibleMoves = [[coords[0]-2, coords[1]-1], [coords[0]+2, coords[1]-1], [coords[0]-2, coords[1]+1], [coords[0]+2, coords[1]+1], [coords[0]+1, coords[1]+2], [coords[0]-1, coords[1]+2], [coords[0]+1, coords[1]-2], [coords[0]-1, coords[1]-2]]
        return possibleMoves

    def legalMoveGenerator(self):  
        #[["","","","",""], [], [], [], []]
        for x in range(len(self._data)): # this is going to give us the nested list
            for y in range(len(self._data[x])):
                if self._data[x][y] == "k":
                    coords = [x, y] # coords of the night in the (x, y)
                    possibleMoves = self.knightPossibleMovement(coords) # get a nested list of every place the night at coords can move
                    for move in possibleMoves: # check first coords in possible moves, if that is a "k" yeild False
                        
                        if move[0] >= 0 and move[1] >= 0:
                            if move[0] < 4 and move[1] < 4:
                                if self._data[move[0]][move[1]] == "k": 
                                    print("Piece at", move, "can be attacked by knight at", coords)
                                    yield False # meaning move is illegal and no more values will be checked bc game puzzle is invalid
                                else:
                                    print("Piece at", coords, "makes a valid move to", move)
                                    yield True
                                                                

                    
game = NineKnights("ClassProject\input.txt")
legalBoard = game.checkBoard()
if legalBoard:
    legalMove = game.legalMoveGenerator()
    for x in legalMove:
        # x will be yielded as False or True (Optimzation so we stop when we run into invalid knight placement)
        if x == False:
            print("[!] Invalid Knight Placement [!]")
            break
else:
    print("[!] Invalid Board [!]")
    print("- knights need to be represented by k and blank squares are represented by .")
    print("- needs to be a 5x5 board")


