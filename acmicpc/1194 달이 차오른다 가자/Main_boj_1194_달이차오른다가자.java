package boj1194;
import java.util.*;
import java.io.*;

public class Main_boj_1194_달이차오른다가자 {
	static StringBuilder sb = new StringBuilder();
	static int N,M,answer;
	static char[][] field;
	static int visited[][][];
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static Pos root;
	static class Pos{
		int x,y,keystatus;
		public Pos(int x, int y, int keystatus) {
			super();
			this.x = x;
			this.y = y;
			this.keystatus = keystatus;
		}
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new char[N][M];//a-f bit 2^5
		visited = new int[N][M][1<<6];
		for(int i =0;i<N;i++) {			
			field[i] = br.readLine().toCharArray();
			for(int j =0;j<M;j++) {
				if(field[i][j]=='0') {
					root = new Pos(j,i,0);
					field[i][j]='.';
				}
			}
		}
	}
	static void BFS() {
		Queue<Pos> q = new LinkedList<>();
		q.add(root);
		visited[root.y][root.x][root.keystatus]=1;
		while(!q.isEmpty()) {
			Pos cur = q.poll();
			for(int[] dir:direction) {
				int nx = cur.x+dir[0];
				int ny = cur.y+dir[1];
				if(nx<0 || ny<0 || nx>=M || ny>=N)continue;
				if(visited[ny][nx][cur.keystatus]!=0)continue;
				char cf = field[ny][nx];
				if(cf=='#') {//벽
					continue;
				}else if(cf=='1') {//출구
					answer = visited[cur.y][cur.x][cur.keystatus]+1;
					return;
				}else if(cf=='.') {//길
					q.offer(new Pos(nx,ny,cur.keystatus));
					visited[ny][nx][cur.keystatus]=visited[cur.y][cur.x][cur.keystatus]+1;
				}else if(0<=cf-'a' && cf-'a'<=5) {//키발견
					int keystatus = (1<<(cf-'a'))|cur.keystatus;
					visited[ny][nx][keystatus] = visited[cur.y][cur.x][cur.keystatus]+1;
					q.add(new Pos(nx,ny,keystatus));
				}else if('A'-'A'<=cf-'A' && cf-'A'<='F'-'A') {//문만나면
					if(((1<<(cf-'A'))&cur.keystatus) != 0) {//키소유
						q.add(new Pos(nx,ny,cur.keystatus));
						visited[ny][nx][cur.keystatus] = visited[cur.y][cur.x][cur.keystatus]+1;
					}
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		input();
		BFS();
		System.out.println(answer-1);
//		System.out.println(1<<0);
	}
}