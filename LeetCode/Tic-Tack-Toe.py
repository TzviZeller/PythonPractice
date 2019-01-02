# https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        X_list = []
        O_list = []
        empty_list = []
        count = 1
        
        for top_index, current_pos in enumerate(board):
          for index, char in enumerate(current_pos):
            if char == 'X':
              X_list.append(count)
            elif char == 'O':
              O_list.append(count)
            elif char == ' ':
              empty_list.append(count)
            else:
              return False
            count += 1
            
        if len(O_list) > len(X_list):
          return False
        elif len(X_list) > len(O_list) + 1:
          return False
    
        x_win = self.has_win(X_list)
        o_win = self.has_win(O_list)
        
        if x_win and len(X_list) == len(O_list) or o_win and len(X_list) == len(O_list) + 1:
          return False
        return True

    def has_win(self, letter_list):
      win_list = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,5,9],
        [3,5,7],
        [1,4,7],
        [2,5,8],
        [3,6,9]
      ]

      return any([True for win_combo in win_list if set(win_combo).issubset(letter_list)])
