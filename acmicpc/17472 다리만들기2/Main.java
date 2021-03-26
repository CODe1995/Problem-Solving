package boj17472;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,field[][],parent[],islandNumber,answer,visited[][];
	static ArrayList<DIST> query;
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};
	static class DIST{
		int start,end,dist;
		public DIST(int start, int end, int dist) {
			this.start = start;
			this.end = end;
			this.dist = dist;
		}		
	}
	static int getParent(int x) {
		if(parent[x] == x)return x;
		return parent[x] = getParent(parent[x]);
	}
	static void unionParent(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}
	static void initIsland(int x,int y,int num) {//섬을 찾는 메소드		
		for(int[] dir:direction) {
			int nx = x+dir[0];
			int ny = y+dir[1];
			if(nx<0 || nx>=M || ny<0 || ny>=N || field[ny][nx]==0 || field[ny][nx]==num)continue;
			field[ny][nx]=num;//섬 번호를 체크함			
			initIsland(nx,ny,num);
		}		
	}
	
	static void setBridge(int x,int y) {//뻗어서 다리가 연결된다면 일단 체크
		int curNum = field[y][x];//현재 섬의 번호
		for(int[] dir:direction) {			
			int nx = x+dir[0];
			int ny = y+dir[1];
			boolean foundIsland = false;//다른섬을 찾았는지 여부 체크
			while(0<=nx && nx<M && 0<=ny && ny<N && field[ny][nx]!=curNum){//다른섬번호 또는 0이어야함
				if(field[ny][nx]!=0) {//다른섬 발견
					foundIsland=true;
					break;
				}
				nx+=dir[0];
				ny+=dir[1];				
			}
			if(foundIsland) {//다른섬 찾았다면
				int dist = Math.abs(nx-x)+Math.abs(ny-y)-1;//거리체크
				if(dist<2) {//거리미달
					continue;
				}
				if(visited[curNum][field[ny][nx]]==0||visited[curNum][field[ny][nx]]>=dist) {
					query.add(new DIST(curNum,field[ny][nx],dist));//거리입력
					visited[curNum][field[ny][nx]]=dist;
					visited[field[ny][nx]][curNum]=dist;
				}
			}
		}
	}
	static void kruskal() {
		for(DIST q:query) {
			int a = q.start;
			int b = q.end;
			if(getParent(a)==getParent(b))continue;//이미연결
			unionParent(a,b);
			answer+=q.dist;
		}
	}
	static void input() throws IOException{
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new int[N][M];
		query = new ArrayList<>();		
		ArrayList<int[]> island = new ArrayList<>();
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++) {
				field[i][j]=Integer.parseInt(st.nextToken());
				if(field[i][j]==1) {
					island.add(new int[] {j,i});
					field[i][j]=-1;//섬 식별을 위해 -1로 초기화
				}
			}
		}
		int islandNum = 1;//섬번호는 1번부터 시작해서 6번까지 존재
		for(int[] isPos:island) {//섬에 번호 새기기
			if(field[isPos[1]][isPos[0]]==-1) {
				field[isPos[1]][isPos[0]]=islandNum;
				initIsland(isPos[0],isPos[1],islandNum++);
			}
		}
		visited = new int[islandNum+1][islandNum+1];
		parent = new int[islandNum];
		for(int i =0;i<islandNum;i++)parent[i]=i;
		
		for(int[] isPos:island) {//각 섬에 다리 설치
			setBridge(isPos[0],isPos[1]);
		}
		Collections.sort(query,(o1,o2)->{
			return o1.dist-o2.dist;
		});
//		for(int[] d:field) {
//			System.out.println(Arrays.toString(d));
//		}
		kruskal();
		int prev = getParent(parent[1]);
		for(int i =2;i<parent.length;i++) {
			if(getParent(parent[i])!=prev) {
				answer=-1;
				break;
			}
		}
		System.out.println(answer==0?-1:answer);

	}
	public static void main(String[] args) throws IOException {
		input();
	}
}