#User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        
        res = []
        if mat[0][0] == 0:
            return res
            
        directions = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
        
        visited = set([(0, 0)])
        def backtrack(row, col, path):
            if (row, col) == (len(mat) - 1, len(mat) - 1):
                res.append(path)
                return
            
            for dr, dc, d in directions:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < len(mat) and 0 <= nc < len(mat) and 
                    (nr, nc) not in visited and mat[nr][nc]
                    ):
                        visited.add((nr, nc))
                        backtrack(nr, nc, path + d)
                        visited.remove((nr, nc))
        
        
        backtrack(0, 0, "")
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends