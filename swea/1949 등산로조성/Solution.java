package swea1949;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer,N,K, field[][];
	static boolean visited[][];
	static Deque<Pos> top;
	static int[][] direction = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static class Pos{
		int x,y;

		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
		
	}
	static void solution(int depth,boolean cut,int rx,int ry) {
		answer = Math.max(depth+1, answer);
		visited[ry][rx]=true;
		
		for(int[] dir:direction) {
			int nx = dir[0]+rx;
			int ny = dir[1]+ry;
			if(0>nx || 0>ny || ny>=N || nx>=N || visited[ny][nx])continue;//좌표밖,이미방문했다면			
			//산깎고 시도
			if(cut==false && field[ry][rx]<=field[ny][nx] && field[ry][rx]>field[ny][nx]-K) {
				int diff = field[ny][nx]-field[ry][rx]+1;
				field[ny][nx]-=diff;
				solution(depth+1,true,nx,ny);
				field[ny][nx]+=diff;
			}
			if(field[ry][rx]>field[ny][nx]) {
				solution(depth+1,cut,nx,ny);//안깎고 시도
			}
		}
		visited[ry][rx]=false;		
	}
	static void input() throws IOException{
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			answer = 0;
			top = new ArrayDeque<Solution.Pos>();
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			field = new int[N][N];
			int maxheight = 0;
			for(int i =0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				for(int j =0;j<N;j++) {
					field[i][j] = Integer.parseInt(st.nextToken());
					maxheight = Math.max(maxheight, field[i][j]);
				}					
			}
			for(int i =0;i<N;i++) {
				for(int j =0;j<N;j++)
					if(field[i][j]==maxheight)
						top.add(new Pos(j,i));//최고높이 꼭대기 좌표를 저장
			}
			for(Pos cur:top) {
				visited = new boolean[N][N];
				solution(0, false, cur.x,cur.y);
			}
				
			sb.append("#").append(t).append(" ").append(answer).append("\n");			
		}
		System.out.println(sb);
		
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}