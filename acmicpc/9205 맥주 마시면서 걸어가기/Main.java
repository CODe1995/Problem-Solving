package boj9205;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static void input() throws IOException{
		int T = Integer.parseInt(br.readLine());
		for(int t=0;t<T;t++) {
			N = Integer.parseInt(br.readLine());
			int pos[][] = new int[N+2][];
			for(int i =0;i<N+2;i++) {
				st = new StringTokenizer(br.readLine());
				pos[i] = new int[] {Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())};
			}
			boolean dp[][] = new boolean[N+2][N+2];
			for(int i =0;i<N+2;i++) {
				for(int j=0;j<N+2;j++) {
					int d = Math.abs(pos[i][0]-pos[j][0])+Math.abs(pos[i][1]-pos[j][1]);
					dp[i][j] = d<=1000?true:false;
				}
			}
			for(int k =0;k<N+2;k++)
				for(int i =0;i<N+2;i++) {
					if(i==k)continue;
					for(int j =0;j<N+2;j++) {
						if(j==i||j==k)continue;
						if(!dp[i][j] && dp[i][k] && dp[k][j])//경유해서 가는 경우
							dp[i][j]=true;
					}
				}
//			for(int i =0;i<N+2;i++)
//				System.out.println(Arrays.toString(dp[i]));
			sb.append(dp[0][N+1]?"happy":"sad").append("\n");
		}
		System.out.println(sb);
	}
	public static void main(String[] args) throws IOException {
		input();		
	}
}