package swea3307;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer,N, arr[],dp[];
	static void input() throws IOException{
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			answer = 0;
			N = Integer.parseInt(br.readLine());
			arr = new int[N+1];
			dp = new int[N+1];
			int max = 0;
			dp[0]= 1;
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<N;i++)arr[i]=Integer.parseInt(st.nextToken());
			for(int i=1;i<N;i++) {
				dp[i]=1;
				for(int j =0;j<i;j++) {
					if(arr[i]>arr[j] && dp[j]+1>dp[i])
						dp[i]=dp[j]+1;
				}
				max = Math.max(dp[i], max);
			}			
			sb.append("#").append(t).append(" ").append(max).append("\n");
		}
		System.out.println(sb);
	}

	public static void main(String[] args) throws IOException {
		input();
	}
}