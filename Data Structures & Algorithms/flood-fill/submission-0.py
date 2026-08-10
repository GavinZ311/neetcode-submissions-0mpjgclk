class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        image[sr][sc] = color

        if starting_color == color:
            return image
    
        def dfs(image, sr, sc, color, starting_color):
            image[sr][sc] = color
            up_sr, down_sr, l_sc, r_sc = sr-1, sr+1, sc-1, sc+1
            if 0 <= up_sr and image[up_sr][sc] == starting_color:
                dfs(image, up_sr, sc, color, starting_color)

            if down_sr < len(image) and image[down_sr][sc] == starting_color:
                dfs(image, down_sr, sc, color, starting_color)
            
            if 0 <= l_sc and image[sr][l_sc] == starting_color:
                dfs(image, sr, l_sc, color, starting_color)
            
            if r_sc < len(image[0]) and image[sr][r_sc] == starting_color:
                dfs(image, sr, r_sc, color, starting_color)
            
            return image
        
        return dfs(image, sr, sc, color, starting_color)