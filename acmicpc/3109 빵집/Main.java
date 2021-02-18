package boj3109;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,visited[][],answer;
	static char field[][];
	static int direction[][] = new int[][]{{1,-1},{1,0},{1,1}};
	static boolean dfs(int x,int y) {
		visited[y][x]=1;
		for(int pos[]:direction) {
			int nx = x+pos[0];
			int ny = y+pos[1];
			if(ny<0 || ny>=N)continue;//필드밖
			if(nx==M-1) {
				visited[ny][nx]=1;
				return true;//끝도달
			}
			if(visited[ny][nx]==0&&field[ny][nx]=='.')
				if(dfs(nx,ny))return true;
		}
		return false;
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new char[N][M];
		for(int i =0;i<N;i++) {
			String tmp = br.readLine();
			for(int j =0;j<M;j++)field[i][j]=tmp.charAt(j);
		}
		visited = new int[N][M];
		for(int i =0;i<N;i++)answer+=dfs(0,i)?1:0;	
		System.out.println(answer);
	}
}