#include <stdio.h>

int solve();

char sudoku[9][9];
int isPossible(int i, int j, char k);

int main(){

    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            scanf("%c ", &sudoku[i][j]);
        }
    }
    solve();
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            printf("%c ", sudoku[i][j]);
        }
        printf("\n");
    }
}

int isPossible(int i, int j, char k){
    for(int x = 0; x < 9; x++){
        if(sudoku[x][j] == k || sudoku[i][x] == k){
            return 0;
        }
    }
    for(int x = i - (i%3); x < i - (i%3) + 3; x++){
        for(int y = j - (j%3); y < j - (j%3) + 3; y++){
            if(sudoku[x][y] == k){
                return 0;
            }
        }
    }
    return 1;
}

int solve(){
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(sudoku[i][j] == '.'){
                for(char k = '1'; k <= '9'; k++){
                    if(isPossible(i, j, k) == 1){
                        sudoku[i][j] = k;
                        if(solve() == 1){
                            return 1;
                        }
                        else{
                            sudoku[i][j] = '.';
                        }
                    }
                }
                return 0;
            }
        }
    }
    return 1;
}