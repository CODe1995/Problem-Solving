package swea;
import java.util.*;
import java.io.*;

public class Solution_swea_1868_파핑파핑지뢰찾기 {
	static StringBuilder sb = new StringBuilder();
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1},{1,1},{-1,-1},{1,-1},{-1,1}};
	static int field[][],parent[];
	static class Pos{
		int x,y;

		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}
	static int getParent(int x) {
		if(x==parent[x])return x;
		return parent[x]=getParent(parent[x]);
	}
	static void unionParent(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a==b)return;
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = stoi(br.readLine());
		for(int tc=1;tc<=TC;tc++) {
			int N = stoi(br.readLine());
			field = new int[N][N];
			for(int i=0;i<N;i++) {
				String line = br.readLine();
				for(int j=0;j<N;j++) {
					char cur = line.charAt(j);
					if(cur=='.')field[i][j]=9;
					else if(cur=='*')field[i][j]=-1;					
				}
			}
			parent = new int[N*N];
			for(int i=0;i<N*N;i++)parent[i]=i;
			
			for(int i =0;i<N;i++) {//Field에 폭탄의 개수를 적어줌
				for(int j =0;j<N;j++) {
					if(field[i][j]==9) {
						int bomb = 0;
						for(int[] dir:direction) {
							int nx = j+dir[0];
							int ny = i+dir[1];
							if(0>nx||0>ny||nx>=N||ny>=N)continue;
							if(field[ny][nx]==-1)bomb++;
						}
						field[i][j]=bomb;
					}
				}
			}
			
			for(int i =0;i<N;i++) {//8방을 탐색해서 0이 있다면 union해줌
				for(int j =0;j<N;j++) {
					if(field[i][j]==-1)continue;
					for(int[] dir:direction) {
						int nx = j+dir[0];
						int ny = i+dir[1];
						if(0>nx||0>ny||nx>=N||ny>=N)continue;
						if(field[ny][nx]==0) {
							int curNum = i*N+j;
							int nextNum = ny*N+nx;
							unionParent(getParent(curNum),getParent(nextNum));
							break;
						}
					}
				}
			}
			int answer = 0;
			boolean visited[] = new boolean[N*N];
			for(int i =0;i<N*N;i++) {
				int x = i%N;
				int y = i/N;
				if(field[y][x]==-1)continue;
				if(visited[getParent(i)])continue;
				visited[getParent(i)]=true;
				answer++;
			}
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}