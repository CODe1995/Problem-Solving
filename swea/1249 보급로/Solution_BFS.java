package swea1249;
import java.util.*;
import java.io.*;

public class Solution_BFS {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,field[][],dp[][],visited[][],answer;
	static int direction[][] = new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
	static class Pos{
		int x,y;
		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static void bfs() {
		Deque<Pos> dq = new ArrayDeque<>();
		dq.add(new Pos(0,0));
		while(!dq.isEmpty()) {
			Pos cur = dq.pollFirst();
			if(cur.y==N-1 && cur.x==N-1)
				answer = Math.min(answer, dp[N-1][N-1]);
			if(answer<=dp[cur.y][cur.x])continue;
			for(int i =0;i<4;i++) {
				int nx = cur.x+direction[i][0];
				int ny = cur.y+direction[i][1];
				if(0>nx || 0>ny || nx>=N || ny>=N)continue;
				if(visited[ny][nx]==0||dp[ny][nx]>dp[cur.y][cur.x]+field[ny][nx]) {
					visited[ny][nx]=1;
					dp[ny][nx]=dp[cur.y][cur.x]+field[ny][nx];
					dq.addLast(new Pos(nx,ny));
				}
			}
		}
	}
	static void input() throws IOException{
		int T = stoi(br.readLine());
		for(int t=1;t<=T;t++) {
			N = stoi(br.readLine());
			answer = Integer.MAX_VALUE; 
			field = new int[N][N];
			dp = new int[N][N];
			for(int i =0;i<N;i++)Arrays.fill(dp[i],Integer.MAX_VALUE);
			visited = new int[N][N];
			
			for(int i =0;i<N;i++) {
				char[] arr = br.readLine().toCharArray();
				for(int j =0;j<N;j++) {
					field[i][j] = arr[j]-48;
				}
			}
			
			visited[0][0]=1;
			dp[0][0]=0;
			bfs();
			sb.append("#").append(t).append(" ").append(answer).append("\n");
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