package boj1914;

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static BigInteger dp[] = new BigInteger[101];
	static void hanoi(int n,int from,int sub,int to) {
		if(n==0)return;
		hanoi(n-1,from,to,sub);
		System.out.println(from+" "+to);
		hanoi(n-1,sub,from,to);
	};
	public static void main(String[] args) throws IOException{
		dp[0] = new BigInteger("0");
		for(int i =1;i<=100;i++)
			dp[i]=dp[i-1].multiply(new BigInteger("2")).add(new BigInteger("1"));
		int N = Integer.parseInt(bf.readLine());
		System.out.println(dp[N]);		
		if(N<=20)
			hanoi(N,1,2,3);
	}
}
