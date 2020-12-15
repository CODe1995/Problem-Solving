#include <iostream>
#include <string>
using namespace std;

int main() {	
	int X,N;	cin >> X;
	int mo, ja;
	//X가 속한 범위의 N을 먼저 구하자
	for(N=1;X>0;)
		X -= N++;	
	N--;
	//분자+분모 = N+1
	//N이 홀수면 분자감소 분모증가
	//N이 짝수면 분자증가 분모감소
	if (N % 2) {//짝수라면
		ja = 1-X;
		mo = N+X;
	}
	else {
		ja = N+X;
		mo = 1-X;
	}



	cout << ja<<"/"<<mo << endl;

	return 0;
}