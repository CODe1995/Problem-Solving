package boj2636;
import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int[][] field;
	static int[][] visited;
	static int answer,N,M,chzcnt;
	static Deque<Pos> dq;
	static int direction[][] = {{0,1},{1,0},{-1,0},{0,-1}};
	static class Pos{
		int x,y,time;
		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static int dfs() {
		int time = 1;
		while(chzcnt>0) {
			answer = chzcnt;
			Deque<Pos> dq = new ArrayDeque<Main.Pos>();
			dq.add(new Pos(0,0));
			visited[0][0]=time+1;
			while(!dq.isEmpty()) {
				int x = dq.peekFirst().x;
				int y = dq.pollFirst().y;
				for(int[] dpos : direction) {
					int nx = x+dpos[0];
					int ny = y+dpos[1];
					if(0<=nx && nx<M && 0<=ny && ny<N && visited[ny][nx]<=time) {
						if(field[ny][nx]==0)
							dq.add(new Pos(nx,ny));
						else if(field[ny][nx]==1) {//해당 자리에 치즈?
							field[ny][nx]=0;
							chzcnt--;	
						}
						visited[ny][nx]=time+1;//지난곳은 못가게. 다음 시간에 올 수 있게.
					}
				}
			}
			time++;
		}
		return time-1;
	}
	public static void main(String[] args) throws IOException{
		answer =0;
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());			
		field = new int[N][M];
		visited = new int[N][M];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(bf.readLine());				
			for(int j =0;j<M;j++) {
				field[i][j]=Integer.parseInt(st.nextToken());
				if(field[i][j]==1)chzcnt++;
			}
		}
		System.out.println(dfs()+"\n"+answer);
	}
}
