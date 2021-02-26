package boj11559;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char field[][] = new char[12][6];
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static int[][] visited = new int[12][6];
	static int answer;
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static boolean bfs(int x,int y) {//특정 좌표에서 탐색하여 겹치는 뿌요 있는지 확인
		Deque<Pos> dq = new ArrayDeque<>();
		Deque<Pos> delete = new ArrayDeque<>(); 
		dq.add(new Pos(x,y));
		while(!dq.isEmpty()) {
			Pos cur = dq.pollFirst();
			char color = field[cur.y][cur.x];//현재 컬러
			
			for(int[] dir:direction) {
				int nx = dir[0]+cur.x;
				int ny = dir[1]+cur.y;
				if(0>nx || 6<=nx || 12<=ny || 0>ny || visited[ny][nx]==1 || field[ny][nx]=='.'||field[ny][nx]!=color)continue;//범위초과, 이미방문
				visited[ny][nx]=1;
				dq.add(new Pos(nx,ny));
				delete.add(new Pos(nx,ny));
			}
		}
		boolean ret = false;
		if(delete.size()>=4) {
			ret = true;
			while(!delete.isEmpty()) {//제거
				Pos del = delete.pollFirst();
				field[del.y][del.x]='.';
			}
		}
		return ret;
	}
	static void gravity() {
		for(int j =0;j<6;j++) {
			for(int i =11;i>=0;i--) {
				if(field[i][j]=='.') {
					int next = i-1;
					while(next>=0) {
						if(field[next][j]!='.') {//위에 돌이 있다면
							field[i][j]=field[next][j];//끌어내림
							field[next][j]='.';
							break;
						}
						next--;
					}
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		for(int i =0;i<12;i++) {
			field[i] = br.readLine().toCharArray();
		}
		
		boolean changed = false;//변경되었는가
		while(true) {
			for(int i =11;i>=0;i--) {
				for(int j =0;j<6;j++) {
					if(visited[i][j]==0)
						if(bfs(j,i))changed=true;
				}
			}
			if(!changed)break;//더 이상 변경되는게 없다면 종료
			if(changed) {gravity();visited=new int[12][6];answer++;changed=false;}
		}
		System.out.println(answer);
	}
}