#include <iostream>
using namespace std;
char map[2188][2188]; //N의 최대크기

void recursive(int y, int x, int n) {
	if (n == 1) {//제일 끝자락
		map[y][x] = '*';
		return;
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (i == 1 && j == 1) {/*공백으로둔다.*/}
			else
				recursive(i*n/3+y, j*n/3+x, n/3);
		}
	}

}

int main() {//다섯번째(가운데)가 공백
	int n; cin >> n;
	for (int i = 0; i < n; i++) {//초기화
		for (int j = 0; j < n; j++) {
			map[i][j] = ' ';
		}
	}
	
	recursive(0,0,n);
	
	for (int i = 0; i < n; i++) {//출력
		for (int j = 0; j < n; j++) {
			cout << map[i][j];
		}
		cout << endl;
	}
	return 0;
}