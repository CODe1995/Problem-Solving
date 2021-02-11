package boj16935;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] field;
	static int[] order;
	static int N,M;
	static void reverse_tb() {//상하반전
		for(int i=0;i<N/2;i++){
			for(int j =0;j<M;j++) {
				int tmp = field[i][j];
				field[i][j] = field[N-1-i][j];
				field[N-1-i][j]=tmp;
			}			
		}
	}
	static void reverse_lr() {//좌우반전
		for(int i=0;i<N;i++){
			for(int j =0;j<M/2;j++) {
				int tmp = field[i][j];
				field[i][j] = field[i][M-1-j];
				field[i][M-1-j] = tmp;
			}			
		}
	}
	static void rotate_right() {//오른쪽90도
		int[][] newarr = new int[M][N];
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				newarr[j][N-i-1] = field[i][j]; 
			}
		}
		int tmp = N;
		N=M;M=tmp;
		field = newarr;
	}
	static void rotate_left() {//왼쪽90도
		int[][] newarr = new int[M][N];
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				newarr[M-j-1][i] = field[i][j]; 
			}
		}
		int tmp = N;
		N=M;M=tmp;
		field = newarr;
	}
	static void turn_right() {//오른쪽 순회
		int[][] newarr = new int[N/2][M/2];
		for(int i =0;i<N/2;i++) {
			for(int j=0;j<M/2;j++) {
				newarr[i][j] = field[i][j];
			}
		}
		for(int i =0;i<N/2;i++) {
			for(int j =0;j<M/2;j++) {
				field[i][j] = field[i+N/2][j];//3->4
				field[i+N/2][j] = field[i+N/2][j+M/2];//2->3
				field[i+N/2][j+M/2] = field[i][j+M/2];//1->2
				field[i][j+M/2] = newarr[i][j];//4->1
			}
		}
	}
	static void turn_left() {//왼쪽 순회
		int[][] newarr = new int[N/2][M/2];
		for(int i =0;i<N/2;i++) {
			for(int j=0;j<M/2;j++) {
				newarr[i][j] = field[i][j];
			}
		}
		for(int i =0;i<N/2;i++) {
			for(int j =0;j<M/2;j++) {
				field[i][j] = field[i][j+M/2];//1->4
				field[i][j+M/2] = field[i+N/2][j+M/2];//2->1
				field[i+N/2][j+M/2] = field[i+N/2][j];//3->2 
				field[i+N/2][j] = newarr[i][j];//4->3
			}
		}
	}
	static void input() throws IOException{
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int order_cnt = Integer.parseInt(st.nextToken());
		field = new int[N][M];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<order_cnt;i++) {
			switch(Integer.parseInt(st.nextToken())) {
			case 1:
				reverse_tb();
				break;
			case 2:
				reverse_lr();
				break;
			case 3:
				rotate_right();
				break;
			case 4:
				rotate_left();
				break;
			case 5:
				turn_right();
				break;
			case 6:
				turn_left();
				break;
			}
		}
	}
	static void print() {
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				sb.append(field[i][j]).append(" ");
			}				
			sb.append("\n");
		}
		System.out.println(sb);
	}
	public static void main(String[] args) throws IOException {
		input();
		print();
	}
}