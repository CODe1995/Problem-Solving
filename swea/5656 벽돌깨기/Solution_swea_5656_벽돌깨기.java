package swea5656;
import java.util.*;
import java.io.*;

public class Solution_swea_5656_벽돌깨기 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,W,H,field[][],choice[],answer;
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static int[][] copyField;
	static boolean[][] visited;
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static void shoot() {		
		for(int i =0;i<H;i++)System.arraycopy(field[i], 0, copyField[i], 0, W);
		
		Queue<Pos> q = new LinkedList<>();
		int remain = 0;
		for(int t =0;t<N;t++) {
			for(int i =0;i<H;i++)Arrays.fill(visited[i], false);
			int brokeLine = choice[t];
			for(int i=0;i<H;i++) {
				if(copyField[i][brokeLine]>0) {
					visited[i][brokeLine]=true;
					q.offer(new Pos(brokeLine,i));
					break;				
				}
			}
			while(!q.isEmpty()) {
				Pos cur = q.poll();
				int power = copyField[cur.y][cur.x];
				copyField[cur.y][cur.x]=0;//해당 블럭 삭제
				if(power>1)
					for(int d=0;d<4;d++) {//4방탐색
						for(int p=1;p<=power-1;p++) {
							int nx = direction[d][0]*p+cur.x;
							int ny = direction[d][1]*p+cur.y;
							if(0>nx||0>ny||W<=nx||H<=ny)break;
							if(field[ny][nx]==0||visited[ny][nx])continue;
							visited[ny][nx]=true;
							q.offer(new Pos(nx,ny));
						}
					}
			}//블럭 확산 끝
			remain = getRemain();
			answer = Math.min(answer, remain);
			if(remain==0)return;
//			gravity();
			for(int i=0;i<W;i++) {				
				for(int j =H-1;j>=0;j--) {
					if(copyField[j][i]==0) {
						for(int k =j-1;k>=0;k--) {
							if(copyField[k][i]>0) {
								copyField[j][i]=copyField[k][i];
								copyField[k][i]=0;
								break;
							}
						}
					}
				}
			}
		}		
//		answer = Math.min(getRemain(copyField), answer);
	}
	static int getRemain() {
		int tmp = 0;
		for(int i =0;i<H;i++) {
			for(int j =0;j<W;j++) {
				if(copyField[i][j]>0)
					tmp++;
			}
		}
		return tmp;
	}
	static void printBlock() {
		for(int i =0;i<H;i++) {
			for(int j =0;j<W;j++) {
				System.out.print(copyField[i][j]);
			}
			System.out.println();
		}
	}
	static boolean isEmpty(int pos) {
		for(int i=0;i<H;i++) {
			if(field[i][pos]>0)
				return false;
		}
		return true;
	}
	static void combination(int depth) {
		if(depth==N) {
			shoot();
			return;
		}
		if(answer==0)return;
		for(int i =0;i<W;i++) {
			if(isEmpty(i))continue;
			choice[depth]=i;
			combination(depth+1);
		}
	}
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());
		W = stoi(st.nextToken());
		H = stoi(st.nextToken());
		answer = Integer.MAX_VALUE;
		field = new int[H][W];
		copyField = new int[H][W];
		choice = new int[N];
		visited = new boolean[H][W];
		for(int i =0;i<H;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<W;j++) {
				field[i][j] = stoi(st.nextToken());
			}
		}
	}
	public static void main(String[] args) throws IOException {		
		int T = stoi(br.readLine());
		for(int t=1;t<=T;t++) {
			input();
			combination(0);
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}