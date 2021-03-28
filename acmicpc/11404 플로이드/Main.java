package boj11404;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int N,M,dp[][],arr[][],INF = Integer.MAX_VALUE;
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = stoi(br.readLine());//도시수
		M = stoi(br.readLine());//버스수
		dp = new int[N+1][N+1];
		arr = new int[N+1][N+1];
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int from = stoi(st.nextToken());
			int to = stoi(st.nextToken());
			int dist = stoi(st.nextToken());
			if(arr[from][to]==0 || (arr[from][to]!=0 && arr[from][to]>dist))
				arr[from][to]=dist;
		}
		
		for(int i=1;i<=N;i++) {
			for(int j=1;j<=N;j++) {
				if(i==j)dp[i][j]=0;
				else{
					dp[i][j]=arr[i][j]==0?INF:arr[i][j];
				}
			}
		}
		
		for(int k=1;k<=N;k++) {
			for(int i=1;i<=N;i++) {
				for(int j=1;j<=N;j++) {
					if(dp[i][k]==INF || dp[k][j]==INF)continue;
					if(dp[i][j]>dp[i][k]+dp[k][j])
						dp[i][j]=dp[i][k]+dp[k][j];
				}
			}
		}
		
		for(int i=1;i<=N;i++) {
			for(int j=1;j<=N;j++) {
				if(dp[i][j]==INF)sb.append(0).append(" ");
				else sb.append(dp[i][j]).append(" ");
			}
			sb.append("\n");
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}