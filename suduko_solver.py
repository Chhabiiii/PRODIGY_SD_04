import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

root = tk.Tk()
root.title("Sudoku Solver")

entries = []

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            if val == '':
                row.append(0)
            else:
                try:
                    row.append(int(val))
                except:
                    row.append(0)
        board.append(row)
    return board

def set_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve():
    board = get_board()
    if solve_sudoku(board):
        set_board(board)
        messagebox.showinfo("Sudoku Solver", "Solved Successfully!")
    else:
        messagebox.showerror("Sudoku Solver", "No solution exists.")

def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(frame, width=3, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j, padx=2, pady=2)
        row_entries.append(entry)
    entries.append(row_entries)

btn_solve = tk.Button(root, text="Solve", command=solve, width=10, bg="green", fg="white")
btn_solve.pack(pady=10)

btn_clear = tk.Button(root, text="Clear", command=clear_board, width=10, bg="red", fg="white")
btn_clear.pack()

root.mainloop()