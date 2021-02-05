package boj1010;

import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb= new StringBuilder();
	static StringTokenizer st;	
	static long dp[][] = new long[30][30];
	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(bf.readLine());
		for(int i=1;i<30;i++)
			for(int j=0;j<=i;j++) {
				if(i==j||j==0)dp[i][j]=1;
				else dp[i][j]=dp[i-1][j]+dp[i-1][j-1];
			}
		for(int t=0;t<T;t++) {		
			st = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());			
			System.out.println(dp[b][a]);			
		}
	}
}
