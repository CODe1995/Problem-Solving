import java.util.*;
import java.io.*;

public class boj21609_상어중학교 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,answer;
	static int field[][];
	static int[][] direction = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static Group delGroup;
	static class Pos{
		int x,y;
		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}		
	}
	
	static class Group{
		Pos standard;//기준블럭의 좌표
		ArrayList<Pos> normalblocks = new ArrayList<>();
		ArrayList<Pos> rainblocks = new ArrayList<>();
	}
	static boolean IsOutField(int x,int y) {
		if(x<0||y<0||x>=N||y>=N)return true;
		return false;
	}
	static void findGroup() {
		boolean visited[][] = new boolean[N][N];
		for(int i =0;i<N;i++) {
			for(int j=0;j<N;j++) {
				if(visited[i][j]||field[i][j]==0||field[i][j]<=-1)continue;
				else {
					visited[i][j]=true;
					Group group = new Group();
					Deque<Pos> dq = new ArrayDeque<>();
					group.normalblocks.add(new Pos(j,i));
					group.standard = new Pos(j,i);
					dq.add(new Pos(j,i));
					boolean[][] rainvisited = new boolean[N][N]; 
					while (!dq.isEmpty()){
						Pos cur = dq.pollFirst();						
						for(int[] dir:direction) {//4방탐색
							int nx = cur.x + dir[1];
							int ny = cur.y + dir[0];
							if(IsOutField(nx, ny)||visited[ny][nx]||field[ny][nx]<=-1)continue;
							if(field[ny][nx]==0 && !rainvisited[ny][nx]) {
								group.rainblocks.add(new Pos(nx,ny));
								dq.add(new Pos(nx,ny));
								rainvisited[ny][nx] = true;
							}
							else if(field[ny][nx]==field[group.standard.y][group.standard.x] && field[ny][nx]!=0) {
								if(group.standard.y==ny) {
									group.standard.x = Math.min(group.standard.x, nx);
								}else if(group.standard.y>ny) {
									group.standard.y = ny;
									group.standard.x = nx;
								}
								group.normalblocks.add(new Pos(nx,ny));								
								dq.add(new Pos(nx,ny));
								visited[ny][nx]=true;
							}
						}						
					}
					int normalBlockSize = group.normalblocks.size();
					int rainBlockSize = group.rainblocks.size();
					int totalSize = normalBlockSize+rainBlockSize;
					if(totalSize>=2) {//그룹 인정
						if(delGroup==null) {
							delGroup = group;//현재 그룹으로 초기화
						}
						else if(delGroup.normalblocks.size()+delGroup.rainblocks.size()<totalSize)//블럭 수가 현재가 더 많다면?
						{
							delGroup = group;
						}
						else if(delGroup.normalblocks.size()+delGroup.rainblocks.size()==totalSize) {//크기가 같다면?
							if(delGroup.rainblocks.size()>rainBlockSize)continue;//무지개 비교
							else if(delGroup.rainblocks.size()==rainBlockSize) {//무지개도 같다면?
								if(delGroup.standard.y > group.standard.y)continue;//행 비교
								else if(delGroup.standard.y == group.standard.y) {//행도 같다면?
									if(delGroup.standard.x > group.standard.x)continue;	//열비교							
								}
							}
							delGroup = group;//위 조건에서 다 살아남았다면 교체
						}
					}
				}
			}
		}
	}
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());//격자크기
		M = Integer.parseInt(st.nextToken());//색상수
		field = new int[N][N];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<N;j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
			}
		}		
	}
	static void delete() {
		int score = delGroup.normalblocks.size()+delGroup.rainblocks.size();
		score = score*score;
		answer += score;
		for(Pos d:delGroup.normalblocks) {
			field[d.y][d.x] = -2;
		}
		for(Pos d:delGroup.rainblocks) {
			field[d.y][d.x] = -2;
		}
		delGroup = null;
	}
	static void gravity() {
		for(int j =0;j<N;j++) {
			for(int i = N-1;i>=0;i--) {
				if(field[i][j]==-2) {
					for(int k=i-1;k>=0;k--) {
						if(field[k][j]==-1)break;
						if(field[k][j]>=0) {//이동 가능한 블럭 발견
							field[i][j] = field[k][j];
							field[k][j] = -2;
							break;
						}
					}
				}
			}
		}
	}
	static void rotate() {//반시계 90도 회전
		int[][] rotField = new int[N][N];
		
		for(int i =0;i<N;i++) {
			for(int j =0;j<N;j++) {
				rotField[N-1-j][i] = field[i][j];
			}
		}
		
		field = rotField;
	}
	public static void main(String[] args) throws IOException {
		input();
		while(true) {
			findGroup();
			if(delGroup==null) {
				break;
			}
			delete();
			gravity();
			rotate();
			gravity();
		}
		System.out.println(answer);		
	}
}