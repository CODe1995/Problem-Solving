package boj1012;
import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int[][] field;
	static int[][] visited;
	static int answer,N,M;
	static Deque<Pos> dq;
	static int direction[][] = {{0,1},{1,0},{-1,0},{0,-1}};
	static class Pos{
		int x,y;
		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
		
	}
	static void dfs(int x,int y) {
		Deque<Pos> dfsq = new ArrayDeque<Main.Pos>();
		dfsq.add(new Pos(x,y));
		while(!dfsq.isEmpty()) {
			x = dfsq.peekFirst().x;
			y = dfsq.pollFirst().y;
			for(int[] dpos : direction) {
				int nx = x+dpos[0];
				int ny = y+dpos[1];
				if(0<=nx && nx<M && 0<=ny && ny<N && visited[ny][nx]==0 && field[ny][nx]==1) {
					dfsq.add(new Pos(nx,ny));
					visited[ny][nx]=1;
				}
			}
		}
	}
	public static void main(String[] args) throws IOException{
		int T = Integer.parseInt(bf.readLine());
		for(int t =0;t<T;t++) {
			answer =0;
			st = new StringTokenizer(bf.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());			
			field = new int[N][M];
			visited = new int[N][M];
			dq= new ArrayDeque<>();
			for(int i=0;i<K;i++){
				st = new StringTokenizer(bf.readLine());
				int a =Integer.parseInt(st.nextToken());
				int b =Integer.parseInt(st.nextToken());
				field[b][a]=1;
				dq.add(new Pos(a,b));
			}
			while(!dq.isEmpty()) {
				int x = dq.peekFirst().x;
				int y = dq.pollFirst().y;
				if(visited[y][x]==0) {
					answer++;
					dfs(x,y);
				}
			}
			System.out.println(answer);
		}
	}
}
