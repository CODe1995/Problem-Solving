package boj10826;
import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static BigInteger dp[];
	static BigInteger solution(int n) {
		if(n==1)return dp[n];
		if(dp[n]!= null)return dp[n];
		return solution(n-1).add(solution(n-2));
	}

	public static void main(String[] args) throws IOException {
		dp = new BigInteger[10001];
		dp[0] = new BigInteger("0");
		dp[1] = new BigInteger("1");
		dp[2] = new BigInteger("1");
		for(int i =0;i<=10000;i++)dp[i] = solution(i);
		System.out.println(dp[Integer.parseInt(br.readLine())]);
	}
}