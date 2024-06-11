class Board:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def place_move(self, row, col, symbol):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol:
                return True  # Row win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == symbol:
                return True  # Column win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True  # Diagonal win
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True  # Diagonal win
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, 'X')
        self.player2 = Player(player2_name, 'O')
        self.current_player = self.player1

    def start(self):
        is_game_over = False
        moves = 0

        while not is_game_over:
            self.board.display_board()
            print(f"{self.current_player.name}'s turn")
            row, col = map(int, input("Enter row and column (0-2): ").split())

            if self.board.place_move(row, col, self.current_player.symbol):
                moves += 1
                if self.board.check_win(self.current_player.symbol):
                    print(f"{self.current_player.name} wins!")
                    is_game_over = True
                elif moves == 9:
                    print("It's a draw!")
                    is_game_over = True
                else:
                    # Switch players
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = Game("Player 1", "Player 2")
    game.start()
