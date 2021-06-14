# Diagonal Traverse

# Time Complexity: O(m*n); traversing through all the elements of the matrix.
# Space Complexity: O(1); no extra space was used.
# Did this code successfully run on Leetcode: all test cases passed.
# Any problem you faced while coding this: no.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        # find size of the matrix
        m = len(mat)-1 # rows
        n = len(mat[0])-1 # cols
        output = []
        # starting indices of the loop
        r = 0
        c = 0
        i = 0
        # starting direction
        direc = 1
        
        while(i < (m+1)*(n+1)):
            
            output.append(mat[r][c])
            
            if direc == 1:
    
                # boundary cases
                if c == n:
                    direc = -1
                    r=r+1
                    
                elif r == 0:
                    direc = -1
                    c=c+1
                
                # forward case
                else:
                    
                    r=r-1
                    c=c+1
            
            else:
                
                # boundary cases
                if r == m:
                    direc = 1
                    c=c+1
                    
                elif c == 0:
                    direc = 1
                    r=r+1
                
                # downward case
                else:
                    r=r+1
                    c=c-1
            i=i+1
        return output
                