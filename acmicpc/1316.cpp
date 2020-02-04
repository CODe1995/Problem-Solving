#include <iostream>
#include <string>
using namespace std;

int main() {
	int alpha[26] = {0,};
	int n,cnt=0;
	bool flag = true;
	cin >> n;
	while (n--) {
		string str; cin >> str;
		//요소 검사 false되면 바로 break;
		for (int i = 0;i<str.size();i++) {
			char ch = str[i];//입력값
			char bch=NULL;			
			//alpha 증가
			//근데, 직전 ch랑 동일하면 증가 X
			if (i > 0) {
				bch = str[i - 1];
				if (bch != ch) { alpha[ch - 'a']++; }
				if (alpha[ch - 'a'] > 1) {
					flag = false;
					break;
				}
			}else{ alpha[ch - 'a']++; }
		}
		if (flag)
			cnt++;
		//초기화
		flag = true;
		for (int i = 0; i < 26; i++)
			alpha[i] = 0;
	}
	cout << cnt << endl;
	return 0;
}