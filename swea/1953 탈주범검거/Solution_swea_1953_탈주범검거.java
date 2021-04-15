package swea1953;
import java.util.*;
import java.io.*;

public class Solution_swea_1953_탈주범검거 {
	static StringBuilder sb = new StringBuilder();
	static int[][] field;
	static int[][] visited;
	static int N,M,L;
	static int direction[][] = new int[][] {{0,-1},{0,1},{-1,0},{1,0}};//상하좌우
	static Pos hole;
	static class Pos{
		int x,y;
		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = stoi(br.readLine());
		for(int t=1;t<=T;t++) {
			st = new StringTokenizer(br.readLine());
			N = stoi(st.nextToken());
			M = stoi(st.nextToken());
			int r = stoi(st.nextToken());
			int c = stoi(st.nextToken());
			hole = new Pos(c,r);
			L = stoi(st.nextToken());
			field = new int[N][M];
			visited = new int[N][M];
			for(int i =0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				for(int j =0;j<M;j++)field[i][j]=stoi(st.nextToken());
			}
			solution();
			int answer = 0;
			for(int i =0;i<N;i++)for(int j =0;j<M;j++)
				if(visited[i][j]>0)answer++;
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}	
		
	}
	static void solution() {
		Queue<Pos> q = new LinkedList<>();
		q.add(hole);
		visited[hole.y][hole.x]=1;
		while(!q.isEmpty()) {
			Pos cur = q.poll();
			if(visited[cur.y][cur.x]==L)continue;
			for(int d:getDirection(field[cur.y][cur.x])) {
				int nx = direction[d][0]+cur.x;
				int ny = direction[d][1]+cur.y;
				if(!canMove(nx,ny))continue;
				if(!checkDenied(d,field[ny][nx])||visited[ny][nx]>0||field[ny][nx]==0)continue;
				visited[ny][nx]=visited[cur.y][cur.x]+1;
				q.offer(new Pos(nx,ny));
			}
		}
	}
	static int[] getDirection(int arch) {//모양을 넘겨주면 나아갈 수 있는 방향을 반환함
		switch(arch) {
		case 1:return new int[] {0,1,2,3};
		case 2:return new int[] {0,1};
		case 3:return new int[] {2,3};
		case 4:return new int[] {0,3};
		case 5:return new int[] {1,3};
		case 6:return new int[] {1,2};
		case 7:return new int[] {0,2};
		}
		return new int[] {};
	}
	static boolean checkDenied(int d,int nextArch) {//현재 방향에서 다음 방향으로 접근 가능한지 반환함
		switch(nextArch) {
		case 1:return true;
		case 2:
			if(d==0||d==1)return true;
			return false;
		case 3:
			if(d==2||d==3)return true;
			return false;
		case 4:
			if(d==1||d==2)return true;
			return false;
		case 5:
			if(d==0||d==2)return true;
			return false;
		case 6:
			if(d==0||d==3)return true;
			return false;
		case 7:
			if(d==1||d==3)return true;
			return false;
		}
		return false;
	}
	static boolean canMove(int nx,int ny) {//좌표 범위 체크
		if(0>nx || 0>ny || nx>=M || ny>=N)return false;
		return true;
	}
	public static void main(String[] args) throws IOException {		
		input();
		System.out.println(sb);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}