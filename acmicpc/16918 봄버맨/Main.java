package boj16918;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,T;
	static char field[][],field2[][],field3[][];
	static void solution() {

	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		field = new char[N][M];
		field2 = new char[N][M];
		field3 = new char[N][M];
		ArrayList<int[]> bombs = new ArrayList<>();
		for(int i =0;i<N;i++) {
			String tmp = br.readLine();
			for(int j =0;j<M;j++) {
				field[i][j] = tmp.charAt(j);
				if(field[i][j]=='O') {
					bombs.add(new int[] {j,i});
				}
			}
		}
		for(int i=0;i<N;i++)Arrays.fill(field2[i],'O');//폭탄 꽉 채움
		for(int i=0;i<N;i++)Arrays.fill(field3[i],'O');//폭탄 꽉 채움
		for(int[] pos:bombs) {//폭탄 펑
			for(int dir[]:new int[][] {{0,0},{0,1},{1,0},{-1,0},{0,-1}}) {
				int nx = pos[0]+dir[0];
				int ny = pos[1]+dir[1];
				if(0>nx || M<=nx || 0>ny || N<=ny || field3[ny][nx]=='.')continue;
				field3[ny][nx]='.';
			}
		}
		//1 - 2 - 3 - 2 - 1 반복
		if(T%2==0)print(field2);
		else if(T%5==0 || T%5==1)print(field);
		else print(field3);	
	}
	static void print(char[][] f) {
		for(int i =0;i<N;i++) {
			for(int j=0;j<M;j++) {
				System.out.print(f[i][j]);
			}
			System.out.println();
		}
	}
}
