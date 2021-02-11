package boj16926;
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
		int R = Integer.parseInt(st.nextToken());
		int[][] field = new int[N][M];
		for(int i = 0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++)
				field[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int layer = Math.min(N, M)/2;
		int[][] direction = new int[][]{{1,0},{0,1},{-1,0},{0,-1}};//시계방향
		for(int r = 0;r<R;r++) {//몇바퀴 회전
			for(int l=0;l<layer;l++) {//몇번째 껍데기
				int x = l,y=l;//시작점은 무조건 좌측 최상단부터
				int tmp = field[y][x];//임시 저장해뒀다가 끝에서 변경
				for(int[] npos:direction) {
					while(true) {
						int nx = x+npos[0];
						int ny = y+npos[1];
						if(l<=nx&&nx<M-l&&l<=ny&&ny<N-l) {
							field[y][x] = field[ny][nx];//한칸겨옴
							x=nx;y=ny;
						}
						else break;
					}
				}				
				field[l+1][l] = tmp;//y좌표 한칸 아래로
			}			
		}
		for(int i=0;i<N;i++) {
			for(int j =0;j<M;j++)
				sb.append(field[i][j]).append(" ");
			sb.append("\n");
		}
		System.out.println(sb);
	}
}