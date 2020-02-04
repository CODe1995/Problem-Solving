#include <iostream>
using namespace std;

int main() {
	int x, y, w, h;
	cin >> x >> y >> w >> h;
	int list[4] = {h-y,w-x,y,x},pos=0;
	for (int i = 1; i < 4; i++) {
		if (list[pos] > list[i])
			pos = i;
	}
	cout << list[pos] << endl;
	return 0;
}