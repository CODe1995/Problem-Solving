package boj9095;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int dp[] = new int[11];
	public static void main(String[] args) throws IOException {
		dp[0]=1;
		dp[1]=1;
		dp[2]=2;
		for(int i =3;i<=10;i++)dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
		int t = Integer.parseInt(br.readLine());
		while(t-->0)System.out.println(dp[Integer.parseInt(br.readLine())]);		
	}
}