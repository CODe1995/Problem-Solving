#include <iostream>
#include <string>
using namespace std;

int main() {
	//고정지출 A, 생산 한대당 B 가변비용, 노트북 가격은 C
	int A, B, C, n=0;
	cin >> A >> B >> C;
	int profit = C - B; // 순이익
	if (profit <= 0) {	//순이익이 0원이하이면 수익X
		cout << -1;
		return 0;
	}

	n = A / profit;

	cout << ++n<<endl;
	return 0;
}