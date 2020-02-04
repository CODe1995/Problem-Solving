#include <iostream>
using namespace std;
int reverse(int);

int reverse(int N) {
	int result = 0;
	result += 100 * (N % 10);
	result += N % 100 - N%10;
	result += N / 100;
	return result;
}
int main(void) {
	int A, B;
	cin >> A >> B;
	cout << (reverse(A) > reverse(B) ? reverse(A) : reverse(B)) << endl;

	return 0;
}