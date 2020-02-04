#include <iostream>
using namespace std;
int main() {
	char board[8][8];
	int cnt = 0;
	for (int i = 0; i < 8; i++) {
		for(int j = 0;j<8;j++)
			cin >> board[j][i];
	}
	for (int i = 0; i < 8; i++) {//8มู
		for (int j = (i%2==0?0:1); j < 8; j+=2) {
			if (board[i][j] == 'F') {
				cnt++;
			}
		}
	}
	cout << cnt;
	return 0;
}