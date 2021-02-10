package boj17086;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int field[][] = new int[N][M];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++)
				field[i][j] = Integer.parseInt(st.nextToken());
		}
		
		//BFS		
		//8방향		
		int[][] direction = new int[][] {{0,1},{1,0},{0,-1},{-1,0},{1,1},{-1,-1},{1,-1},{-1,1}};
		int answer = 0;
		for(int y=0;y<N;y++) {
			for(int x=0;x<M;x++) {
				if(field[y][x]==1)continue;
				Queue<int[]> q = new LinkedList<>();
				int[][] visited = new int[N][M];
				visited[y][x]=1;
				q.add(new int[]{x,y});
				while(!q.isEmpty()) {
					int[] cur_pos = q.poll();
					for(int[] next_pos:direction) {
						int nx = next_pos[0] + cur_pos[0];
						int ny = next_pos[1] + cur_pos[1];
						if(0<=nx&&nx<M&&0<=ny&&ny<N&&visited[ny][nx]==0) {
							visited[ny][nx]=visited[cur_pos[1]][cur_pos[0]]+1;
							if(field[ny][nx]==0) {
								q.add(new int[] {nx,ny});
							}else {//상어발견!
								if(answer<visited[ny][nx]-1)answer=visited[ny][nx]-1;
								q.clear();
								break;
							}
						}
					}
				}
			}
		}
		System.out.println(answer);
	}
}