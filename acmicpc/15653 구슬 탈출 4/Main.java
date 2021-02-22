package boj15653;
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char field[][];
	static int N,M,RED[],BLUE[],HOLE[],answer = Integer.MAX_VALUE;
	static HashMap<String, Integer> visited = new HashMap<>();//RB좌표,이동횟수
	static int direction[][] = new int[][] {{0,-1},{0,1},{-1,0},{1,0}};//상하좌우
	static void solution(int[] red,int[] blue,int move) {
		String prev_key = gets(red[0],red[1],blue[0],blue[1]);
		visited.put(prev_key, move);
		for(int p=0;p<4;p++) {
			int pos[] = direction[p];//나아갈 방향

			int bnx = blue[0]+pos[0];
			int bny = blue[1]+pos[1];
			while(field[bny][bnx]=='.') {//벽만날때까지
				bnx+=pos[0];	bny+=pos[1];
			}
			if(field[bny][bnx]=='O') {
				continue; }//구멍만나면 게임 끝
			bnx-=pos[0];	bny-=pos[1];//벽만났다면 한칸 뒤로.
			
			int rnx = red[0]+pos[0];
			int rny = red[1]+pos[1];
			while(field[rny][rnx]=='.') {//벽만날때까지
				rnx+=pos[0];	rny+=pos[1];
			}
			if(field[rny][rnx]=='O') {//빨강만 구멍만난경우?
				answer = Math.min(move+1,answer);
				continue; 
			}
			rnx-=pos[0];	rny-=pos[1];//벽만났다면 한칸 뒤로.
			
			if(rnx==bnx && rny==bny) {//구슬 겹치는 경우
				if(p==0) {//상
					if(red[1]<blue[1])bny+=1;
					else rny+=1;
				}
				else if(p==1) {//하
					if(red[1]>blue[1])bny-=1;
					else rny-=1;
				}
				else if(p==2) {//좌
					if(red[0]<blue[0])bnx+=1;
					else rnx+=1;
				}
				else if(p==3) {//우
					if(red[0]>blue[0])bnx-=1;
					else rnx-=1;
				}
			}//두 구슬이 겹친다면 우선순위 정해주기
			//중복체크
			String next_key = gets(rnx,rny,bnx,bny);
			if(visited.containsKey(next_key) && move+1>visited.get(next_key)) {//종료조건
				//이미 방문했다면.
				continue;
			}
			solution(new int[] {rnx,rny},new int[] {bnx,bny},move+1);
		}
	}
	public static String gets(int a,int b,int c,int d) {
		return a+" "+b+" "+c+" "+d;
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new char[N][M];
		for(int i =0;i<N;i++) {
			field[i] = br.readLine().toCharArray();
			for(int j =0;j<M;j++) {
				if(field[i][j]=='O') {HOLE = new int[] {j,i};}
				else if(field[i][j]=='B') {BLUE = new int[] {j,i};field[i][j]='.';}
				else if(field[i][j]=='R') {RED = new int[] {j,i};field[i][j]='.';}
			}
		}
		visited.put(gets(RED[0],RED[1],BLUE[0],BLUE[1]), 1);
		solution(RED,BLUE,0);
		System.out.println(answer==Integer.MAX_VALUE?-1:answer);
	}
}