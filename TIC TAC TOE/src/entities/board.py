class Board:
    
    def __init__(self) -> None:
        self.board = [['_']* 3 for _ in range(3)]  # 3 * 3 board
        
        
    def print_board(self):
        print(self.board)
        
        
    def mark_board(self,box: str , symbol: str):
        if len(box) != 2:
            raise Exception('Please enter row and col')
        i, j = int(box[0]) , int(box[i])
        if self.board[i][j] != '_':
            raise Exception('Choose Different box , this is already Marked')
        self.board[i][j] = symbol