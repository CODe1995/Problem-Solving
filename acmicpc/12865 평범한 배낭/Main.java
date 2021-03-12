package boj12865;

import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,K,dp[][],W[],V[];
	static int solution(int depth,int w) {
		if(dp[depth][w]>0)return dp[depth][w];
		if(depth==N)return 0;
		int case1 = 0;
		if(w+W[depth]<=K) //담을 수 있다면
			case1 = V[depth] + solution(depth+1,w+W[depth]);		
		int case2 = solution(depth+1,w);//안담는 경우
		return dp[depth][w] = Math.max(case1, case2);
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		dp = new int[101][100001];
		W = new int[101];
		V = new int[101];
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			W[i]=Integer.parseInt(st.nextToken());
			V[i]=Integer.parseInt(st.nextToken());
		}
		System.out.println(solution(0,0));		
	}
}
