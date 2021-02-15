package boj14500;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M, field[][],visited[][],answer=0;	
	static int direction[][] = new int[][]{{0,1},{1,0},{-1,0},{0,-1}};	
	static int ms[][][] = {
			{{0,0},{0,-1},{0,1},{1,0}},//ㅏ
			{{0,0},{0,-1},{-1,0},{1,0}},//ㅗ
			{{0,0},{-1,0},{0,-1},{0,1}},//ㅓ
			{{0,0},{-1,0},{1,0},{0,1}}//ㅜ
	};
//	static void print(int s) {
//		System.out.println("==================↓"+s);
//		for(int i =0;i<N;i++) {
//			for(int j=0;j<M;j++) {
//				System.out.print(visited[i][j]);
//			}
//			System.out.println();
//		}
//	}
	static void dfs(int x,int y,int depth, int sum) {
		if(depth==4) {
//			if(answer<sum) {
//				print(sum);
//			}
			answer = Math.max(answer, sum);
			return;
		}
		visited[y][x]=1;
		for(int pos[]:direction) {
			int nx = x+pos[0];
			int ny = y+pos[1];
			if(0>nx || 0>ny || N<=ny || M<=nx || visited[ny][nx]==1)continue;//필드밖,방문
			visited[ny][nx]=1;//방문체크
			dfs(nx,ny,depth+1,sum+field[y][x]);
			visited[ny][nx]=0;//방문해제
		}
		visited[y][x]=0;
	}
	static int exs(int x,int y) {
		int exs_answer = 0;
		for(int[][] posf:ms) {//4
			int sum =0;
			for(int[] pos:posf) {//1
				int nx = x+pos[0];
				int ny = y+pos[1];
				if(0>nx || 0>ny || N<=ny || M<=nx)break;//필드밖 하나라도 나가면 무효
				sum+=field[ny][nx];
			}			
			exs_answer = Math.max(sum, exs_answer);
		}
		return exs_answer;
	}
	static void input() throws IOException{
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new int[N][M];
		visited = new int[N][M];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0;j<M;j++)
				field[i][j] = Integer.parseInt(st.nextToken());
		}
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				dfs(j,i,0,0);
				answer = Math.max(answer, exs(j,i));
			}
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(answer);
	}
}