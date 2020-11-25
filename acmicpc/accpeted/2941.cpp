#include <iostream>
#include <string>
using namespace std;


int main() {
	string alpha[8] = {"c=","c-","dz=","d-","lj","nj","s=","z="};
	string str;
	int cnt = 0;
	cin >> str;
	for (int i = 0;i<8;i++) {
		int n = str.find(alpha[i]);
		if (n<string::npos) {//즉 문자가 있을때
			cnt++;
			str.replace(n, alpha[i].size(), (alpha[i].size() == 2 ? "__" : "___"));
			i = -1;
			continue;
		}
	}
	for (int i = 0; i < str.size(); i++) {
		if (str[i] != '_')
			cnt++;
	}
	cout << cnt << endl;

	return 0;
}