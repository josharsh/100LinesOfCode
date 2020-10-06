class GOL{
  
  int w = 10;
  int columns, rows;
  
  int[][] board;
  
  GOL(){
    columns = width/w;
    rows = height/w;
    board = new int[columns][rows];
    init();
  }
  
  void init(){
    for(int i = 0; i < columns - 1; i++){
      for(int j = 0; j < rows - 1; j++){
        board[i][j] = int(random(2));
      }
    }
  }
  
  void generate(){
    int[][] next = new int[columns][rows];
    
    for(int x = 1; x < columns - 1; x++){
      for(int y = 1; y < rows - 1; y++){
        
        int neighbors = 0;
        for(int i = -1; i <= 1; i++){
          for(int j = -1; j <= 1; j++){
            neighbors += board[x + i][y + j];
          }
        }
        
        neighbors -= board[x][y];
        
        if ((board[x][y] == 1) && (neighbors < 2)) next[x][y] = 0;
        else if ((board[x][y] == 1) && (neighbors > 3)) next[x][y] = 0;
        else if ((board[x][y] == 0) && (neighbors == 3)) next[x][y] = 1;
        else next[x][y] = board[x][y];        
      }
    }
    
    board = next;
  }
  
  void render(){
    for(int i = 0; i < columns; i++){
      for(int j = 0; j < rows; j++){
        if(board[i][j] == 1){
          fill(0);
        } else {
          fill(255);
        }
        int x = i * w;
        int y = j * w;
        rect(x, y, w, w);
      }
    }
  }
}
