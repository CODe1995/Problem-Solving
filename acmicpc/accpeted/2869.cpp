#include <iostream>
#include <string>
using namespace std;
int main() {
	int V, A, B,res=0,i;
	cin >> A >> B >> V;
	//A 올라가 B 미끄러져 V최종목표

	cout << (V - B) - 1 / (A - B) + 1 << endl;
	return 0;
}