class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[r][c] will store (max_score, number_of_paths) for cell (r, c)
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Starting point 'E' (top-left)
        dp[0][0] = [0, 1]
        
        # Pre-process board: replace 'E' with '0' and 'S' with '0' to align with number cells
        # Also mark 'X' with a score of -1 to flag as impassable
        
        for r in range(n):
            for c in range(n):
                # If current cell is impassable or unreachable so far, skip it
                if dp[r][c][0] == -1:
                    continue
                    
                current_score, current_paths = dp[r][c]
                
                # Possible moves: go right (r, c+1), down (r+1, c), down-right (r+1, c+1)
                # (Equivalent to left, up, up-left when moving backwards from E to S)
                moves = [(r, c + 1), (r + 1, c), (r + 1, c + 1)]
                
                for nr, nc in moves:
                    if nr < n and nc < n and board[nr][nc] != 'X':
                        # Get the point value of the next cell
                        val = 0 if board[nr][nc] in ('E', 'S') else int(board[nr][nc])
                        new_score = current_score + val
                        
                        if new_score > dp[nr][nc][0]:
                            dp[nr][nc][0] = new_score
                            dp[nr][nc][1] = current_paths % MOD
                        elif new_score == dp[nr][nc][0]:
                            dp[nr][nc][1] = (dp[nr][nc][1] + current_paths) % MOD
                            
        # End point is at (n-1, n-1) which originally marked 'S'
        result_score, result_paths = dp[n-1][n-1]
        
        # If the score is still -1, it means S was unreachable
        if result_score == -1:
            return [0, 0]
            
        return [result_score, result_paths]
