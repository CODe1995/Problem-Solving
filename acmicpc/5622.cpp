#include <iostream>
using namespace std;


int main() {
	int numc[8] = {3,6,9,12,15,19,22,26};
	int time = 0;
	while (1) {
		char ch = getchar();
		if (ch == '\n')
			break;
		for (int i = 0; i < 8;i++) {
			if (ch - 'A' + 1 <= numc[i]) {
				time += 1 + i + 2;
				break;
			}			
		}
	}
	cout << time<<endl;
	return 0;
}