package boj16956;

import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static class Pos{
		int x,y;
		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		char field[][] = new char[N][M];
		Deque<Pos> dq= new ArrayDeque<Main.Pos>();
		for(int i=0;i<N;i++){
			String tmp = bf.readLine();
			for(int j =0;j<M;j++) {
				if(tmp.charAt(j)=='.')
					field[i][j] = 'D';				
				else field[i][j] = tmp.charAt(j);
				if(field[i][j]=='W')dq.add(new Pos(j,i));
			}
		}
		int answer = 1;
		int direction[][] = {{0,1},{1,0},{-1,0},{0,-1}};
		while(!dq.isEmpty()) {
			Pos tmp = dq.pollFirst();
			int x = tmp.x;
			int y = tmp.y;
			for(int[] dpos:direction) {
				int nx = x+dpos[0];
				int ny = y+dpos[1];
				if(0<=nx&&nx<M&&0<=ny&&ny<N&&field[ny][nx]=='S') {
					answer = 0;
					dq.clear();
					break;
				}
			}
		}
		System.out.println(answer);
		if(answer!=0)
			for(int i =0;i<N;i++) {
				for(int j =0;j<M;j++) {
					System.out.print(field[i][j]);
				}
				System.out.println();
			}
	}
}
