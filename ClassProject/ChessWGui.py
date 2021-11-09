from typing import Sequence
import pygame as p
from pygame import color

class NineKnights:
    def __init__(self):
        # . is a blank square k is a knight
        self.WIDTH = 500
        self.HEIGHT = 500
        self.DIMENSION = 5 # 5 BY 5 
        self.SQ_SIZE = self.HEIGHT // self.DIMENSION
        self.IMAGE = {}
        # [(0,0),(1,0),(2,2)]
        self._moveLog = []

        self._board = [
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
        ]

    def loadPieces(self):
        self.IMAGE["k"] = p.transform.scale(p.image.load("ClassProject/bN.png"),(self.SQ_SIZE, self.SQ_SIZE))


    def drawBoard(self, screen):
        colors = [p.Color("white"), p.Color("gray")]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                color = colors[((r+c)%2)]
                p.draw.rect(screen, color, p.Rect(c*self.SQ_SIZE, r*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def drawPieces(self, screen, board):
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                piece = self._board[r][c]
                if piece != ".":
                    screen.blit(self.IMAGE[piece], p.Rect(c*self.SQ_SIZE, r*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def knightPossibleMovement(self, coords):
        # kinda jank wish i could make this a loop :(
        possibleMoves = [[coords[0]-2, coords[1]-1], [coords[0]+2, coords[1]-1], [coords[0]-2, coords[1]+1], [coords[0]+2, coords[1]+1], [coords[0]+1, coords[1]+2], [coords[0]-1, coords[1]+2], [coords[0]+1, coords[1]-2], [coords[0]-1, coords[1]-2]]
        return possibleMoves

    def legalMoveGenerator(self):  
            #[["","","","",""], [], [], [], []]
            
        coords = [self._moveLog[len(self._moveLog)-1][0], self._moveLog[len(self._moveLog)-1][1]] # coords of the night in the (x, y)
        possibleMoves = self.knightPossibleMovement(coords) # get a nested list of every place the night at coords can move
        for move in possibleMoves: # check first coords in possible moves, if that is a "k" yeild False
            
            if move[0] >= 0 and move[1] >= 0:
                if move[0] < 4 and move[1] < 4:
                    if self._board[move[0]][move[1]] == "k": 
                        print("Piece at", move, "can be attacked by knight at", coords)
                        yield False # meaning move is illegal and no more values will be checked bc game puzzle is invalid
                    else:
                        print("Piece at", coords, "makes a valid move to", move)
                        yield True

    def main(self):
        p.init()
        screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = p.time.Clock()
        screen.fill(p.Color("white"))
        game = NineKnights()
        self.loadPieces()
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    col = location[0]//self.SQ_SIZE
                    row = location[1]//self.SQ_SIZE
                    self._board[row][col] = "k"
                    self._moveLog.append((row,col))
                    print(self._moveLog)
                    if len(self._moveLog) > 9:
                        print("Too many knights placed")
                        running = False
                        break
                    legalMove = self.legalMoveGenerator()
                    for x in legalMove:
                        # x will be yielded as False or True (Optimzation so we stop when we run into invalid knight placement)
                        if x == False:
                            print("[!] Invalid Knight Placement [!]")
                            running = False
                            break
                        if len(self._moveLog) == 9:
                            print("Congrats You Win!")
                            running = False 
                            break
                    
            self.drawBoard(screen)
            self.drawPieces(screen, self._board)
            
            p.display.flip()

if __name__ == "__main__":
    game = NineKnights()
    game.main()
