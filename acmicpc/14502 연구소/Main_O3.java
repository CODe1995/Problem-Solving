package boj14502;
import java.util.*;
import java.io.*;

public class Main_O3 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] field;
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
				if(field[i][j]==0)cnt++;
				else if(field[i][j]==3)field[i][j]=0;
			}
		}
		return cnt;
	}
	static void spreadVirus(int x,int y) {
		for(int[] dir:direction) {
			int nx = dir[0]+x;
			int ny = dir[1]+y;
			if(0>nx||0>ny||M<=nx||N<=ny||field[ny][nx]!=0)continue;
			field[ny][nx]=3;
			spreadVirus(nx,ny);		
		}
	}
	static void setWall() {
		int Area = N*M;
		for(int first =0;first<Area;first++) {
			if(field[first/M][first%M]!=0)continue;
			field[first/M][first%M]=1;
			for(int second = first+1;second<Area;second++) {
				if(field[second/M][second%M]!=0)continue;
				field[second/M][second%M]=1;
				for(int third = second+1;third<Area;third++) {
					if(field[third/M][third%M]!=0)continue;
					field[third/M][third%M]=1;	
					for(Pos cur:virus)
						spreadVirus(cur.x,cur.y);
					answer = Math.max(countSafe(),answer);
					field[third/M][third%M]=0;
				}
				field[second/M][second%M]=0;
			}
			field[first/M][first%M]=0;
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
		setWall();
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(answer);
	}
}
