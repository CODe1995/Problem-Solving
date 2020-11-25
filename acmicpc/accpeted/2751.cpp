//#include <iostream>
//#include <algorithm>
//#include <vector>
//
//using namespace std;
////머지로 해야함.. 시간복잡도가 O(N)임..
//
//int Merge_Sort(vector<int> v) {
//	int size = v.size();
//	for (int i = 0; i < v.size(); i+=2) {
//		cout << v[i] <<" ";
//	}
//	cout << endl;
//
//	return 0;
//}
//
//
//int main() {
//	int N;
//	cin >> N;
//	vector<int> v(N);
//	for (int i = 0; i < N; i++) {
//		cin >> v[i];		
//	}
//	/*
//	1. 두개가 될 때까지 절반으로 나눔
//	2. 두개부터 서로 비교해서 정렬
//	3. 정렬된 두개를 Merge함
//	*/
//	//생성된 방의 크기 :  _msize(arr)/sizeof(int)
//
//	Merge_Sort(v);
//
//
//	return 0;
//}