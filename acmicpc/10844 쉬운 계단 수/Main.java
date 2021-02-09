package boj10844;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static long dp[][] = new long[101][11]; 
	static int mod = 1000000000;
	static void solution() {
		for(int i =1;i<=9;i++)
			dp[1][i] = 1;
		for(int i=2;i<=N;i++) {
			dp[i][0]=dp[i-1][1];
			for(int j =1;j<=9;j++) {
				dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%mod;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		solution();
		long sum = 0;
		for(int i=0;i<=9;i++) {
			sum+=dp[N][i];
		}
		System.out.println(sum%mod);
	}
}