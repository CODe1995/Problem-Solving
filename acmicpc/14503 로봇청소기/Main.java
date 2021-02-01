package boj14503;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int N,M,x,y,d,i,j,answer;
	static int field[][];
	static int dirX[] = {0,1,0,-1};
	static int dirY[] = {-1,0,1,0};
	static class Ksh{
		int x,y,d;
		Ksh(){		}
		Ksh(int y,int x,int d){
			this.x=x;
			this.y=y;
			this.d=d;
		}
	}
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(bf.readLine());
		Queue<Ksh> dq = new LinkedList<>();		
		dq.add(new Ksh(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())));
		field = new int[N][M];
		for(i=0;i<N;i++) {
			st = new StringTokenizer(bf.readLine());
			for(j=0;j<M;j++)
				field[i][j] = Integer.parseInt(st.nextToken());
		}
		while(true) {
			Ksh tmp = dq.poll();
			x = tmp.x;
			y = tmp.y;
			d = tmp.d;
			if(field[y][x]==0) {//현재 위치 청소
				field[y][x]=2;
				answer+=1;
				
			}
			int i =0;
			for(i =0;i<4;i++) {//방향 회전하며 확인
				d-=1;
				if(d==-1)d=3;
				int nx = x+dirX[d];
				int ny = y+dirY[d];
				if(0<=nx && nx<M && 0<=ny && ny<N && field[ny][nx]==0) {
					dq.add(new Ksh(ny,nx,d));
					break;
				}
			}
			if(i==4) {//위 반복문을 다 돌고 나온거라면?
				int f=0;
				if(d>1)f=d-2;
				else f=d+2;
				int nx = x+dirX[f];
				int ny = y+dirY[f];
				if(0<=nx && nx<M && 0<=ny && ny<N && field[ny][nx]!=1)
					dq.add(new Ksh(ny,nx,d));
				else {
					System.out.println(answer);
					return;
				}
			}
		}
	}
}
