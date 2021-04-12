package swea1249;
import java.util.*;
import java.io.*;

public class Solution_DFS {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,answer,field[][],dp[][],visited[][];
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static void dfs(int x,int y) {
		if(x==N-1 && y==N-1) {
			answer = Math.min(answer, dp[N-1][N-1]);
			return;
		}
		if(dp[y][x]>=answer)return;
		for(int i=0;i<4;i++) {
			int nx = direction[i][0]+x;
			int ny = direction[i][1]+y;
			if(!isValid(nx,ny))continue;
			if(visited[ny][nx]==0||dp[ny][nx]>dp[y][x]+field[ny][nx]) {
				dp[ny][nx] = dp[y][x]+field[ny][nx];
				visited[ny][nx]=1;
				dfs(nx,ny);
			}
		}
	}
	static boolean isValid(int x,int y) {
		if(x<0 || y<0 || x>=N || y>=N)return false;
		return true;
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
			dfs(0,0);
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