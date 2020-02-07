#include <iostream>
#include <string>
using namespace std;
int main() {
	int pureN,N, F;
	cin >> pureN >> F;
	N = pureN;
	N -= N % 100;
	N = (N / F) * F;

	int pn,dn,cntpn=0,cntdn=0;
	do {//자릿수구하기
		pn = pureN / 10;
		cntpn++;
	} while (pn > 1);
	do {//자릿수구하기
		dn = N / 10;
		cntdn++;
	} while (dn > 1);
	if (cntdn != cntpn) {
		N += F;
	}
	if (N % F != 0)
		N += F;
	string result = to_string(N);
	int size = result.size();
	cout << result.at(size - 2) << result.at(size - 1) << endl;
	return 0;
}