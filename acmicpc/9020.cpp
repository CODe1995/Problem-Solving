#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;
//주어진 수의 두 소수의 합 출력하기
bool pnCheck(int);
bool pnCheck(int num) {//prime number check function
	for (int i = 2; i <= sqrt(num); i++) {
		if (num % i == 0)
			return false;
	}
	return true;
}

int main() {
	int T; cin >> T;
	int gbhPartition = 0;
	for (int i = 0; i < T; i++) {
		int target;	cin >> target;
		for (int j = 2; j < target / 2 + 1; j++) {
			if (pnCheck(j) && pnCheck(target - j)) {//both prime number
				if (gbhPartition != 0) {
					if (abs(target - gbhPartition - gbhPartition) > abs(target - j - j)) {
						gbhPartition = j;
					}
				}
				else { gbhPartition = j; }
			}
		}
		cout << gbhPartition << " " << target - gbhPartition << endl;
		gbhPartition = 0;	
	}
	return 0;
}