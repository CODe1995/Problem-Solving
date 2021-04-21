package boj15683;
import java.util.*;
import java.io.*;

public class Main_boj_15683_감시 {
	static StringBuilder sb = new StringBuilder();
	static int N,M,field[][],size,answer;
	static ArrayList<Pos> cctvs;
	static int direction[][] = new int[][] {{0,-1},{0,1},{-1,0},{1,0}};//상하좌우
	static String[] getDirection = {"","0,1,2,3","23,01","03,31,12,20","023,301,123,210","0123"};	
	static class Pos{
		int x,y;
		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());
		M = stoi(st.nextToken());
		field = new int[N][M];
		cctvs=new ArrayList<>();
		int cnt=0;
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++) {
				field[i][j]=stoi(st.nextToken());
				if(1<=field[i][j] && field[i][j]<=5)
					cctvs.add(new Pos(j,i));
				else if(field[i][j]==0)cnt++;
			}
		}
		size = cctvs.size();
		answer= N*M;
		dfs(0,cnt);
	}
	static void dfs(int depth,int spots) {
		if(depth==size) {
			answer = Math.min(spots,answer);
			return;
		}
		int rx = cctvs.get(depth).x;
		int ry = cctvs.get(depth).y;
		int spec = field[ry][rx];
		String[] curd = getDirection[spec].split(",");
		for(int i=0;i<curd.length;i++) {
			ArrayList<Pos> install = new ArrayList<>();
			for(char c:curd[i].toCharArray()) {
				int x = c-'0';
				int nx = rx+direction[x][0];
				int ny = ry+direction[x][1];
				while(0<=nx && 0<=ny && nx<M && ny<N && field[ny][nx]!=6) {
					if(field[ny][nx]==0) {
						field[ny][nx]=7;//7을 감시경로로 표시
						install.add(new Pos(nx,ny));
						spots--;
					}
					nx+=direction[x][0];
					ny+=direction[x][1];
				}				
			}
			dfs(depth+1,spots);
			for(int j =0;j<install.size();j++) {
				field[install.get(j).y][install.get(j).x]=0;
				spots++;
			}
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(answer);
	}
}