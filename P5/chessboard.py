class ChessBoard:
    """
    This class gets the position of each players ' pieces from a chessboard and prints each players' pieces with the corresponding row and column information 
    """
    def __init__ (self, boardFile):
        self.__boardFile = boardFile
        self.pieces = {"White":{"K":[],"Q":[],"R":[],"B":[],"N":[],"P":[]},
                  "Black":{"K":[],"Q":[],"R":[],"B":[],"N":[],"P":[]}}
        self.__pattern = "+---+---+---+---+---+---+---+---+"

    def obtain_positions(self):
        f = open(self.__boardFile,"r")
        lines = f.readlines()
        numberRow = 9
        for line in lines[:-1]:
            aux = line.strip()
            if aux == self.__pattern:
                numberRow -=1
            else: 
                row = aux.split("|")[1:-1]
                for val,column in enumerate(row):
                    if column[1].isupper():
                        self.__add_piece_white_player(column[1],val,numberRow)
                    elif column[1].islower():
                        self.__add_piece_black_player(column[1],val,numberRow)
        f.close()

        self.order_positions("White",False)
        self.order_positions("Black",True)

    def __add_piece_white_player(self, piece, column, row):
        self.pieces["White"][piece].append([chr(column+97),str(row)])

    def __add_piece_black_player(self, piece, column, row):
        self.pieces["Black"][piece.upper()].append([chr(column+97),str(row)])

    def order_positions(self, player, invert):
        for plr,positions in self.pieces[player].items():
            if len(positions)>1:
                self.pieces[player][plr] = sorted(self.pieces[player][plr],key=lambda x: x[1],reverse=invert)

                # pieces[player][plr] = sorted(pieces[player][plr],key=lambda x: x[0])

    def print_positions(self):
        for player,piece in self.pieces.items():
            print(f"{player}:",end=" ")
            strAux = []
            for lett, pos in piece.items():
                p = lett if lett != "P" else ""
                for iteration in pos:
                    strAux.append(p+iteration[0]+iteration[1])
            print(",".join(strAux))
    
print("================================================================")
chess_board1 = ChessBoard("input.txt")
chess_board1.obtain_positions()
chess_board1.print_positions()
print("================================================================")
chess_board2 = ChessBoard("input2.txt")
chess_board2.obtain_positions()
chess_board2.print_positions()
print("================================================================")
chess_board2 = ChessBoard("input3.txt")
chess_board2.obtain_positions()
chess_board2.print_positions()
print("================================================================")
