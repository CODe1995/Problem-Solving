package boj2589;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static class node{
		int x,y;
		node(int x,int y){
			this.x = x;
			this.y = y;
		}
	}
	static int H,W;
	static char field[][];
	static int dirx[]= {0,1,-1,0};
	static int diry[]= {1,0,0,-1};
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
	static int bfs(int rx, int ry) {
		int visited[][] = new int[H][W];
		visited[ry][rx]=1;
		Deque<node> q = new LinkedList<node>();
		node n = new node(rx,ry);
		q.addLast(n);
		int maxcnt = 0 ;
		while(!q.isEmpty()) {
			node qxy = q.pollFirst();
			for(int i = 0 ; i <4;i++) {
				int nextX = qxy.x + dirx[i];
				int nextY = qxy.y + diry[i];
				if(0<=nextX && nextX<W && 0<=nextY && nextY<H && field[nextY][nextX]=='L' && visited[nextY][nextX]==0) {
					visited[nextY][nextX]=visited[qxy.y][qxy.x]+1;
					if(maxcnt<visited[nextY][nextX])maxcnt=visited[nextY][nextX];
					node nnd = new node(nextX,nextY);
					q.addLast(nnd);
				}
			}
		}
		return maxcnt-1;
	}
	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());
		H = Integer.parseInt(st.nextToken());
		W = Integer.parseInt(st.nextToken());
		field = new char[H][W];
		for(int i = 0 ; i < H;i++) {
			st = new StringTokenizer(br.readLine());
			String tmp = st.nextToken();
			for(int j = 0 ; j < W;j++)
				field[i][j] = tmp.charAt(j);
		}
		int max = 0;
		for(int i = 0 ; i < H;i++)
			for(int j = 0 ; j < W; j++) {
				if(field[i][j]=='L') {
					int tmp = bfs(j,i);
					if (max<tmp)max=tmp;
				}	
			}
		System.out.println(max);
	}
}
