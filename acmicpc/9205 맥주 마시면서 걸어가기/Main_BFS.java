package boj9205;
import java.util.*;
import java.io.*;

public class Main_BFS {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static boolean dp[][],visited[][];
	static boolean bfs() {
		Deque<Integer> dq = new ArrayDeque<>();
		dq.add(0);
		while(!dq.isEmpty()) {
			int cur = dq.pollFirst();
			for(int i =0;i<N+2;i++) {
				if(cur==N+1 && i==N+1 && dp[cur][i])return true;
				if(cur==i || visited[cur][i])continue;				
				if(dp[cur][i])dq.add(i);
				visited[cur][i]=true;
			}
		}
		return false;
	}
	static void input() throws IOException{
		int T = Integer.parseInt(br.readLine());
		for(int t=0;t<T;t++) {
			N = Integer.parseInt(br.readLine());
			int pos[][] = new int[N+2][];
			for(int i =0;i<N+2;i++) {
				st = new StringTokenizer(br.readLine());
				pos[i] = new int[] {Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())};
			}
			dp = new boolean[N+2][N+2];
			visited = new boolean[N+2][N+2];
			for(int i =0;i<N+2;i++) {
				for(int j=0;j<N+2;j++) {
					int d = Math.abs(pos[i][0]-pos[j][0])+Math.abs(pos[i][1]-pos[j][1]);
					dp[i][j] = d<=1000?true:false;
				}
			}
			sb.append(bfs()?"happy":"sad").append("\n");
		}
		System.out.println(sb);
	}
	public static void main(String[] args) throws IOException {
		input();		
	}
}