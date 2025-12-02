
class TicTacToe:

    def __init__(self):
        self.turn = True
        self.character_list = [ ["*"]*3 for i in range(4)]
        print("Welcome to tic-tac-toe")
        print("Which mode you like to play: AI OR 1v1")
        choice = int(input("Press 1 for 1v1 and 2 for AI:"))

        if(choice == 1):
            pass

        else:
            pass
        
        
    
    def print_board(self):
        print(f"""
                ___________________
                |  {self.character_list[0][0]}  |  {self.character_list[0][1]}  |  {self.character_list[0][2]}  |   
                |  {self.character_list[1][0]}  |  {self.character_list[1][1]}  |  {self.character_list[1][2]}  |   
                |  {self.character_list[2][0]}  |  {self.character_list[2][1]}  |  {self.character_list[2][2]}  |
                ___________________
            """)
        
        


    def input_to_board(self):
        if(self.turn):
            x_pos_row = int(input("Player X enter the row for your X: "))
            x_pos_col = int(input("Player X enter the column for your X: "))
            if(self.character_list[x_pos_row - 1][x_pos_col - 1] == "X" or self.character_list[x_pos_row - 1][x_pos_col - 1] == "O"):
                print(f"THERES ALREADY A {self.character_list[x_pos_row][x_pos_col]} THERE!!")

            else:
                self.character_list[x_pos_row - 1][x_pos_col - 1] = "X"
                self.print_board()
                self.turn = False


        else:
            o_pos_row = int(input("Player O enter the row for your O: "))
            o_pos_col = int(input("Player O enter the column for your O: "))


            if(self.character_list[o_pos_row - 1][o_pos_col - 1] == "O" or self.character_list[o_pos_row - 1][o_pos_col - 1] == "X"):
                print(f"THERES ALREADY A {self.character_list[o_pos_row][o_pos_col]} THERE!!")

            else:
                self.character_list[o_pos_row - 1][o_pos_col - 1] = "O"
                self.print_board()
                self.turn = True
        


    def method_caller(self):
        self.print_board()
        self.input_to_board()
        self.input_to_board()
        self.input_to_board()
        self.input_to_board()



ttt = TicTacToe()   

ttt.method_caller()
