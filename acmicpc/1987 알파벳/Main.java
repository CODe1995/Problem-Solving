package boj1987;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,alpha[] = new int[26],answer;
	static char field[][];
	static int visited[][];
	static int direction[][] = new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
	static void dfs(int x,int y,int cnt) {
		answer = Math.max(answer, cnt);
		visited[y][x]=1;
		alpha[field[y][x]-'A']=1;
		for(int pos[]:direction) {
			int nx = pos[0]+x;
			int ny = pos[1]+y;
			if (0>nx || 0>ny || nx>=M || ny>=N || visited[ny][nx]==1 || alpha[field[ny][nx]-'A']==1)continue;
			dfs(nx,ny,cnt+1);
		}
		alpha[field[y][x]-'A']=0;
		visited[y][x]=0;
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());
		M = stoi(st.nextToken());
		field = new char[N][];
		visited = new int[N][M];
		for(int i =0;i<N;i++)field[i] = br.readLine().toCharArray();
		
		dfs(0,0,0);
		System.out.println(answer+1);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}