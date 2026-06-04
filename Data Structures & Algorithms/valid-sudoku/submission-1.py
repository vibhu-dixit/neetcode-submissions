class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            clean_row = [val for val in l if val != '.']
            if len(clean_row) != len(set(clean_row)):
                return False
        for col_tuple in zip(*board):
            clean_col = [val for val in col_tuple if val != '.']
            if len(clean_col) != len(set(clean_col)):
                return False
        box_lists = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + (j // 3)
                box_lists[box_index].append(board[i][j])
        for box in box_lists:
            clean_box = [val for val in box if val != '.']
            if len(clean_box) != len(set(clean_box)):
                return False
        return True    