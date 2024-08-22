def maxPoints(points) -> int:
    rows , cols = len(points) , len(points[0])
    
    
    # @cache
    def find_max(i,j,cur_sum,prev_col):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 0
        
        
        if i == rows-1:
            return cur_sum + (points[i][j] - abs(prev_col - j))
        
        
        # dont take
        dont_take = find_max(i+1,j,cur_sum,prev_col)
        ans = dont_take
        
        for col in range(j,cols):   
            
            # take it
            cur_sum += points[i][col]
            cur_sum -= abs(prev_col - col)

            take_it = find_max(i+1,col,cur_sum,col)
            
            ans = max(ans,take_it)
            
            cur_sum -= points[i][j]
            cur_sum += abs(prev_col- col)
            
        return ans
        
    ans = float('-inf')
    for col in range(cols):
        val = find_max(0,0,points[0][col],col)
        ans = max(val,ans)
    return ans 


points = [[1,2,3],[1,5,1],[3,1,1]]
print("maxPoints(points)",maxPoints(points))
            