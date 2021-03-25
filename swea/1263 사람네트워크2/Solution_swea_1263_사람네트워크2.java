package swea1263;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer,N,dp[][],INF = 10000000;
	static void input() throws IOException {
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			answer = Integer.MAX_VALUE;
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			dp = new int[N][N];
			for(int i =0;i<N;i++) {
				for(int j =0;j<N;j++) {
					dp[i][j] = Integer.parseInt(st.nextToken());
					if(i!=j && dp[i][j]==0)dp[i][j]=INF;
					
				}
			}
			
			for(int k =0;k<N;k++) {
				for(int i =0;i<N;i++) {
					if(i==k)continue;
					for(int j=0;j<N;j++) {
						if(i==j || j==k)continue;
						if(dp[i][k]+dp[k][j] < dp[i][j]) {
							dp[i][j] = dp[i][k] + dp[k][j];
						}
					}
				}
			}
			
			
			for(int i =0;i<N;i++) {
				int tmp = 0;
//				System.out.println(Arrays.toString(dp[i]));
				for(int j =0;j<N;j++) {					
					tmp+=dp[i][j];
				}
				answer = Math.min(tmp, answer);
			}
			
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

	public static void main(String[] args) throws IOException {
		input();
		
	}
}