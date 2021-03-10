package boj5427;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[][] field;
	static int[][] visited;
	static Deque<Pos> fireq;
	static int[][] direction = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static Deque<Pos> boss;
	static int answer,N,M;//주인공좌표, 정답
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static void solution() {
		int runTime = 0;
		while(true) {
			runTime++;
			//상근이 이동
			int bsize = boss.size();
			for(int i =0;i<bsize;i++) {
				Pos cur = boss.pollFirst();
				if(field[cur.y][cur.x]=='*') {//불이번졌다면
					continue;
				}
				for(int[] dir:direction) {
					int nx = cur.x+dir[0];
					int ny = cur.y+dir[1];
					if((nx<0 || nx>=M || ny<0 || ny>=N) && field[cur.y][cur.x]!='*') {//탈출조건
						System.out.println(runTime);
						return;
					}
					if(field[ny][nx]!='.' || visited[ny][nx]!=0)continue;
					visited[ny][nx]=1;
					boss.offerLast(new Pos(nx,ny));
				}	
			}
			if(boss.isEmpty()) {
				System.out.println("IMPOSSIBLE");
				return;
			}
			//불이동
			int qsize = fireq.size();
			for(int i =0;i<qsize;i++) {
				Pos cur = fireq.pollFirst();
				for(int[] dir:direction) {
					int nx = cur.x+dir[0];
					int ny = cur.y+dir[1];
					if(nx<0 || nx>=M || ny<0 || ny>=N || field[ny][nx]!='.')continue;
					field[ny][nx]='*';
					fireq.addLast(new Pos(nx,ny));
				}
			}
		}
	}
	static void input() throws IOException{
		int T = Integer.parseInt(br.readLine());
		for(int t=0;t<T;t++) {
			answer =0;
			boss = new ArrayDeque<Main.Pos>();
			fireq = new ArrayDeque<Main.Pos>();
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			field = new char[N][M];
			visited = new int[N][M];
			for(int i =0;i<N;i++) {
				field[i] = br.readLine().toCharArray();
				for(int j =0;j<M;j++) {
					if(field[i][j]=='*') {//불
						fireq.offer(new Pos(j,i));
					}else if(field[i][j]=='@') {
						field[i][j]='.';
						boss.add(new Pos(j,i));
						visited[i][j]=1;
					}
				}
			}
			solution();			
		}
	}

	public static void main(String[] args) throws IOException {
		input();
	}
}