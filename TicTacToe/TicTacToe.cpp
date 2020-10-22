#include <iostream>
using namespace std;

void drawBoard(char board[]){
	for(int i = 1; i < 4; i++){
		cout << " " << board[1+((i-1)*3)] << " | " << board[2+((i-1)*3)] << " | " << board[3*i] << endl;
		if(i < 3){
			cout << "---+---+---" << endl;
		}
	}
}

bool checkGameOver(char board[]){
	if(	//checks to see if 3 in a row
		(board[1] == board[2] && board[2] == board[3] && board[3] != ' ') || //first row
		(board[4] == board[5] && board[5] == board[6] && board[6] != ' ') || //second row
		(board[7] == board[8] && board[8] == board[9] && board[9] != ' ') || //third row
		(board[1] == board[4] && board[4] == board[7] && board[7] != ' ') || //first column
		(board[2] == board[5] && board[5] == board[8] && board[8] != ' ') || //second column
		(board[3] == board[6] && board[6] == board[9] && board[9] != ' ') || //third column
		(board[1] == board[5] && board[5] == board[9] && board[9] != ' ') || //first diag
		(board[7] == board[5] && board[5] == board[3] && board[3] != ' ') //second diag
		){
		return true;
	}
	for(int i = 1; i < 10; i++){	//checks for tie
		if(board[i] == ' '){
			return false;		//return false if there is an open square
		}
	}
	cout << "Tie! ";
	return true;		//return true if all square are blocked and no 3 in a row
}

int getComputerMove(char board[]){
	if(board[5] == ' '){ return 5; } //start middle if possible
	if(board[1] == ' ' && ((board[2] == board[3] && board[2] != ' ') || (board[4] == board[7] && board[4] != ' ') || (board[9] == board[5]))){ return 1;} //stops or finishes a 3 in a row
	if(board[2] == ' ' && ((board[1] == board[3] && board[1] != ' ') || (board[5] == board[8]))){ return 2;}
	if(board[3] == ' ' && ((board[1] == board[2] && board[1] != ' ') || (board[6] == board[9] && board[6] != ' ') || (board[7] == board[5]))){ return 3;}
	if(board[4] == ' ' && ((board[1] == board[7] && board[1] != ' ') || (board[5] == board[6]))){ return 4;}
	if(board[6] == ' ' && ((board[4] == board[5] && board[4] != ' ') || (board[3] == board[9]))){ return 6;}
	if(board[7] == ' ' && ((board[1] == board[4] && board[1] != ' ') || (board[8] == board[9] && board[9] != ' ') || (board[3] == board[5])) && board[7] == ' '){ return 7;}
	if(board[8] == ' ' && ((board[2] == board[5] && board[2] != ' ') || (board[7] == board[9]))){ return 8;}
	if(board[9] == ' ' && ((board[3] == board[6] && board[3] != ' ') || (board[7] == board[8] && board[8] != ' ') || (board[1] == board[5]))){ return 9;}
	for(int i = 1; i < 10; i++){ //find next open space
		if(board[i] == ' '){
			return i;
		}
	}
	return 9;
}

void makeCompMove(char board[]){
	int compMove = getComputerMove(board);
	board[compMove] = 'O';
	cout << "Computer selected sqaure " << compMove << endl;
	drawBoard(board);
}

int playerMove(char board[]){
	int move = 0;
	cout << "You turn.";
	while(move < 1 ||  move > 9 || board[move] != ' '){
		cout << "Input number between 0-8 to make your move." << endl;
		cin >> move;
		cin.clear();	//when cin gets bad input
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
	}
	return move;
}

int main(){
	char firstTurn;
	cout << "Lets play a game of TicTacToe. Do you want to go first or second?(f/s)" << endl;	//ask user who goes first
	while(firstTurn != 's' && firstTurn != 'f'){
		cin >> firstTurn;
	}
	char board[10];	//creates board with base value of a space character
	for(int i = 0; i < 10; i++){
		board[i] = ' ';
	}
	drawBoard(board);
	if(firstTurn == 's'){	//if computer starts first
		makeCompMove(board);
	}
	bool gameOver = false;
	while (gameOver == false){
		int move = playerMove(board);
		board[move] = 'X';
		drawBoard(board);
		gameOver = checkGameOver(board);
		if(gameOver == true){ break;}
		makeCompMove(board);
		gameOver = checkGameOver(board);
	}
	cout << "Game Over" << endl;
	return 0;
}