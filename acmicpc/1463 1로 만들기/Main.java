package boj1463;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int dp[] = new int[1000001];
	static int solution(int n) {
		if(dp[n]!=0)return dp[n];
		if(n%3==0 && n%2==0) return dp[n]=Math.min(Math.min(solution(n/3)+1,solution(n-1)+1),solution(n/2)+1);
		else if(n%3==0) return dp[n]=Math.min(solution(n/3)+1,solution(n-1)+1);
		else if(n%2==0) return dp[n]=Math.min(solution(n/2)+1,solution(n-1)+1);
		else return dp[n]=solution(n-1)+1;
	}
	public static void main(String[] args) throws IOException {
		dp[1]=0;
		dp[2]=1;
		dp[3]=1;
		dp[4]=2;
		for(int i =5;i<1000001;i++)solution(i);
		System.out.println(dp[Integer.parseInt(br.readLine())]);
	}
}