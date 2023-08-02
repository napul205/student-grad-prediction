n = 8;
x = [2, 1, -1, -2, -2, -1, 1, 2];
y = [1, 2, 2, 1, -1, -2, -2, -1];


def isSafe(new_x, new_y, board):
    if (new_x >= 0 and new_y >= 0 and new_x < n and new_y < n and board[new_x][new_y] == -1):
        return True
    return False


def solve(n):
    board = [[-1 for i in range(n)] for i in range(n)]
    board[0][0] = 0
    pos = 1
    if (not solveKTUtil(n, board, 0, 0, x, y, pos)):
        print("Solution does not exist")
    else:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()


def solveKTUtil(n, board, curr_x, curr_y, x, y, pos):
    if (pos == n ** 2):
        return True

    for i in range(n):

        new_x = curr_x + x[i]
        new_y = curr_y + y[i]
        if (new_x >= 0 and new_y >= 0 and new_x < n and new_y < n and board[new_x][new_y] == -1):
            board[new_x][new_y] = pos
            if (solveKTUtil(n, board, new_x, new_y, x, y, pos + 1)):
                return True

            board[new_x][new_y] = -1
    return False


if __name__ == "__main__":
    solve(n)