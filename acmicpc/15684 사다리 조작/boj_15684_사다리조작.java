import java.util.*;
import java.io.*;

public class boj_15684_사다리조작 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,H,answer=-1;
	static int[][] ladders;	
	
	static boolean checkLadders() {		
		for(int i =0;i<N;i++) {
			int nx,ny;
			nx = i;
			ny = 0;
			boolean moved = false;// 연속이동불가
			while(ny<H) {
				if(ladders[ny][nx]==0 || moved) {//하강
					ny++;
					moved = false;
				}
				else if(ladders[ny][nx]==1 && !moved) {//우측
					nx++;
					moved = true;
				}
				else if(ladders[ny][nx]==-1 && !moved) {//좌측
					nx--;
					moved = true;
				}
			}//끝에 도달
			if(nx!=i) {//결과 값이 다름
				return false;
			}
		}
		return true;
	}
	
	static void solution(int depth,int number) {
		if(checkLadders()) {
			if(answer==-1)answer=depth;
			else answer = Math.min(answer, depth);
			return;
		}
		if(depth == 3) {
			return;
		}
		for(int next_number = number;next_number<N*H;next_number++) {
			int x = next_number%N;
			int y = next_number/N;
			if(ladders[y][x]==0) {
				if(x+1<N&&ladders[y][x]==0&&ladders[y][x+1]==0) {//오른쪽 설치가능
					ladders[y][x]=1;
					ladders[y][x+1]=-1;
					solution(depth+1,next_number+1);
					ladders[y][x]=0;
					ladders[y][x+1]=0;		
				}
			}
		}
	}
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); //사다리 갯수
		M = Integer.parseInt(st.nextToken()); //가로선 갯수
		H = Integer.parseInt(st.nextToken()); //높이
		ladders = new int[H][N];
		//0 하강, 1 오른쪽, -1 왼쪽
		for(int i =0;i<M;i++) {
			int a,b;
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken())-1;
			b = Integer.parseInt(st.nextToken())-1;
			ladders[a][b] = 1;
			ladders[a][b+1] = -1;
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		solution(0,0);			
		System.out.println(answer);
	}
}