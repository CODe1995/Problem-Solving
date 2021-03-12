package boj14502;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] field,visited;
	static int N,M,answer;
	static ArrayList<Pos> virus = new ArrayList<>();
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static int[][] direction = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static int countSafe() {
		int cnt=0;
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				if(visited[i][j]!=1&&field[i][j]==0)cnt++;
			}
		}
		return cnt;
	}
	static void spreadVirus() {
		visited=new int[N][M];
		for(Pos cur:virus) {
			visited[cur.y][cur.x]=1;
			Deque<Pos> dq = new ArrayDeque<Main.Pos>();
			dq.add(new Pos(cur.x,cur.y));
			while(!dq.isEmpty()) {
				Pos cv = dq.pollFirst();
				for(int[] dir:direction) {
					int nx = dir[0]+cv.x;
					int ny = dir[1]+cv.y;
					if(0>nx||0>ny||M<=nx||N<=ny||field[ny][nx]!=0||visited[ny][nx]!=0)continue;
					visited[ny][nx]=1;
					dq.add(new Pos(nx,ny));
				}
			}
		}
	}
	static void setWall(int depth,int index) {
		if(depth==3) {
			spreadVirus();
			answer = Math.max(countSafe(),answer);
			return;
		}
		for(int i = index;i<N*M;i++) {
			int x = i%M;
			int y = i/M;
			if(field[y][x]==0) {//비어있는곳이라면
				field[y][x]=1;//벽세움
				setWall(depth+1,i+1);
				field[y][x]=0;//복구
			}
		}
	}
	static void input() throws IOException{
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new int[N][M];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++) {
				field[i][j]=Integer.parseInt(st.nextToken());
				if(field[i][j]==2) {
					virus.add(new Pos(j,i));
				}
			}				
		}
		setWall(0,0);
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(answer);
	}
}
