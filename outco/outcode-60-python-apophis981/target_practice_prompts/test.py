    else:
                self.game_board.place_piece(r, c, self.player)
                break

    def print_current_players_turn(self):
        print(f"Player {self.player}'s turn")

    def decrement_rounds(self):
        self.rounds -= 1

    def declare_winner(self, player):
        print(f"Player {player} wins!")

    def declare_tie(self):
        print("Nobody wins!")

    def print_current_move(self, row, col):
        print(f"Placing a {self.player} at {row} {col")

    def print_invalid_move(self, row, col):
        print(f"Invalid move {row} {col}, both row and col have to be between 0 and {len(self.game_board.board)}")

    def switch_player(self):
        self.player = 'X' if self.player == 'O' else 'O'




class Board:
    def __init__(self, dim):
        self.board = [dim*['-'] for _ in range(dim)]
        self.size = dim * dim

    def print_board(self):
        # YOUR WORK HERE
        print("\n".join(" ".join(row) for row in self.board))

    def can_place_piece(self, row, col):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return False

        if self.board[row][col] != '-':
            return False

        return True
        # YOUR WORK HERE

    def place_piece(self, row, col, player):
        self.board[row][col] = player

    def check_win_condition(self, player):
        if self.check_diagonals(player):
            return True

        if self.check_rows(player):
            return True

        if self.check_columns(player):
            return True

        return False

    def check_diagonals(self, player):
        from_left = True
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                from_left = False

        from_right = True
        for i in range(len(self.board)):
            if self.board[i][-(i+1)] != player:
                from_right = False

        return from_left or from_right

    def check_rows(self, player):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if j == len(self.board) - 1 and self.board[i][j] == player:
                    return True
                if self.board[i][j] is not player:
                    break
        return False




    def check_columns(self, player):
        # YOUR WORK HERE
        for c in range(len(self.board[0])):
            if self.board[0][c] == '-':
                continue

            for r in range(len(self.board)):
                if self.board[r][c] != self.board[0][c]:
                    break
            else:
                return True

        return False


# Uncomment to test
ttt = TicTacToe()
ttt.play(3)
