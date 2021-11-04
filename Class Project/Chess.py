# Open file to get the playing board
# check to see if playing baord is legal- 9 Knights, 5x4 board, knights are defined as k
# turn board into usuable data 
# start in lower left corner and send position into generator that computes next possible position 
# check if move is legal
# if legal move to next move untill all moves are analyzed
# once all moves analayzed then move to next piece removing that piece from list
# repeat until empty list

# file 
#  . . . . k
#  k . . . .
#  . k . k .
#  k . k . k


finished = False
while finished == False:
    try:
        file = open("Class Project\input.txt")
        data = [list(line) for line in file]
        # [[".", "k"][".", "k"]]
    except IOError as error:
        print(error)
    finally:
        file.close()

class NineKnights:
    def __init__(self):
        self._data = data
        self._legalBoard = True

    def checkBoard(self, data):
        # Checking to see if board is correct dimensions
        while self._legalBoard == True:
            if len(data) == 4:
                for x in range(len(data)):
                    if len(data[x]) == 5:
                        self._legalBoard = True
                        
                    else:
                        self._legalBoard = False
            

        return self._legalBoard


    def legalMoveGenerator(self):
        return
    
game = NineKnights()
game.checkBoard(data)


