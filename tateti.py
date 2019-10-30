
class TaTeTi():

    def __init__(self, board = [" "," "," "," "," "," "," "," "," "]):

        self.board = board 

    def full(self):

        return " " not in self.board

    def win(self):

        if self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[3] != " ":

           return True

        elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[4] != " ":

            return True

        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[8] != " ":

            return True

        elif self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[8] != " ":

            return True

        

        elif self.board[3] == self.board[4] and self.board[3] == self.board[5] and self.board[5] != " ":

            return True

        

        elif self.board[0] == self.board[1] and self.board[0] == self.board[2] and self.board[2] != " ":

            return True

        

        elif self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[8] != " ":

            return True

        elif self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[6] != " ":

            return True

        else:

            return False



    def validate(self,position):
        
        if self.board[position-1] != " ":
            return False
        else:
            return True

    def assign(self, position, piece):

        if self.board[position - 1] == " ":
            self.board[position - 1] = piece
        else:
            raise Exception

    def draw_board(self):
        
        board = self.board
        
        for i in range (9):
            if board[i] == " ":
                board [i] = str(i+1)

        return "\n " +  board[0]+" | " +  board[1]+" | "+  board[2] +" \n---+---+---\n "+ board[3] + " | " + board[4]+ " | " + board[5]+" \n---+---+---\n "+ board[6] + " | " + board[7] + " | " + board[8] + " \n"








       