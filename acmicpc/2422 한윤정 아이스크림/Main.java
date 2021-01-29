package boj2422;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	static void func() {
		
	}
	static long comb(int n) {
		long ret=1;
		for(int i=3;i<=n;i++) {
			ret*=i;
		}
		for(int i=1;i<=3;i++) {
			ret/=i;
		}
		return ret;
	}
	static void solve() throws IOException {
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		boolean X[][] = new boolean[201][201];//default false

		for(int i =0;i<M;i++) {//금지된 조합을 체크함.
			st = new StringTokenizer(bf.readLine());
			int a =Integer.parseInt(st.nextToken());
			int b =Integer.parseInt(st.nextToken());
			X[a][b]= true;
			X[b][a]= true;
		}
		
		int answer = 0;
		for(int i =1;i<=N-2;i++) {//첫번째 수 선택
			for(int j =i+1;j<=N-1;j++) {//두번째 수 선택
				if(X[i][j])continue;//X인경우
				for(int k=j+1;k<=N;k++) {
					//i-k, j-k 겹치는 경우 비교
					if(X[i][k] || X[k][j])continue;
					answer++;
				}
			}
		}
		System.out.println(answer);
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(bf.readLine());
		sb = new StringBuilder();
		solve();
	}
}
