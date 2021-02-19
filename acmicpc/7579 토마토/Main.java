package boj7579;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int field[][] = new int[N][M];
		Deque<int[]> dq = new ArrayDeque<>();
		int tcnt=0;//토마토수
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++) {
				field[i][j]=Integer.parseInt(st.nextToken());
				if(field[i][j]==1)dq.add(new int[] {j,i});
				else if(field[i][j]==0)tcnt++;
			}
		}
		int answer = 0;		
		int visited[][] = new int[N][M];
		while(!dq.isEmpty()&&tcnt>0) {
			answer++;
			int size = dq.size();			
			for(int s =0;s<size;s++) {
				int x = dq.peekFirst()[0];
				int y = dq.pollFirst()[1];
				visited[y][x]=1;
				for(int pos[]:new int[][] {{0,1},{1,0},{-1,0},{0,-1}}) {
					int nx = x+pos[0];
					int ny = y+pos[1];
					if(0>nx || 0>ny || M<=nx || N<=ny || field[ny][nx]!=0 || visited[ny][nx]==1)continue;
					field[ny][nx]=1;
					visited[ny][nx]=1;
					tcnt--;
					dq.add(new int[] {nx,ny});
				}
			}
		}
		
		System.out.println(tcnt==0?answer:-1);
	}
}