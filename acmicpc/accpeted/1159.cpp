#include <iostream>
#include <vector>
using namespace std;
int main() {
	int N;
	int arr[26] = { 0, };
	cin >> N;
	vector<string> v(N);
	for (int i = 0; i < N; i++) {
		cin >> v[i];
		arr[v[i].at(0) - 97]++;
	}
	bool flag=false;
	for (int i = 0; i < 26; i++) {
		if (arr[i] >= 5) {
			cout << (char)(i + 97);
			flag = true;
		}
	}
	if (!flag) {
		cout << "PREDAJA";
	}
	cout << endl;

	return 0;
}