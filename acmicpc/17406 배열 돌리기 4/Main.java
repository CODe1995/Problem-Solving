package boj17406;
import java.util.*;
import java.io.*;
public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] origin_field,fake_field;
	static int N,M,R,answer = Integer.MAX_VALUE;
	static ArrayList<Query> query;
	static int direction[][] = {{0,1},{1,0},{0,-1},{-1,0}};//시계반대
	static void rotate(int x,int y,int cnt) {//cnt는 한 면의 최대 길이
		if(cnt==1)return;
		int rx = x, ry=y;//초기 좌표 저장
		int tmp = fake_field[ry][rx];//첫 좌표 저장(맨마지막에 저장)
		for(int[] dPos:direction) {//4방
			while(true) {
				int dx = dPos[0], dy = dPos[1];
				int nx = x+dx;
				int ny = y+dy;
				if(rx>nx || nx>=rx+cnt || ny>=ry+cnt || ry>ny)
					break;//좌표 벗어나면 다음 방향으로
				fake_field[y][x] = fake_field[ny][nx];
				x= nx; y= ny;
			}
		}
		fake_field[ry][rx+1]=tmp;
//		print();
	}
	
	static void solution(int r,int c,int s) {
		int y = r-s-1;
		int x = c-s-1;
		int cnt = s*2+1;
		int Layer = s+1;
		for(int l =0;l<Layer;l++) {			
			rotate(x+l,y+l,cnt);//겉만 돌린다
			cnt-=2;
		}		
	}
	static void print() {//필드 출력 테스트
		System.out.println("================");
		for(int i=0;i<N;i++) {
			for(int j =0;j<M;j++) {
				System.out.print(fake_field[i][j]+" ");
			}
			System.out.println();
		}
	}
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		origin_field = new int[N][M];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++) {
				origin_field[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		query = new ArrayList<>();
		for(int i=0;i<R;i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			query.add(new Query(r,c,s));
		}
		arr = new int[R];
		newarr = new int[R];
		checked = new boolean[R];
		for(int i =0;i<R;i++)arr[i]=i;//arr초기화(index)
		permutation(0,-1);//입력된 쿼리의 모든 경우의 수 뽑아내기
	}
	static class Query{
		int r,c,s;
		public Query(int r, int c, int s) {
			this.r = r;
			this.c = c;
			this.s = s;
		}
	}
	static int arr[];
	static int newarr[];
	static boolean checked[];
	static void permutation(int depth,int index) {
		if(depth==R) {
			
			//deep copy
			fake_field = origin_field.clone();//copy
			for(int i =0;i<N;i++)fake_field[i] = origin_field[i].clone();
			
//			print();
			for(int i =0;i<R;i++) {
				int r = query.get(newarr[i]).r;
				int c = query.get(newarr[i]).c;
				int s = query.get(newarr[i]).s;
//				System.out.println(r+" "+c+" "+s+" 수행");
				solution(r,c,s);
//				print();
			}//fake_field 변경완료
			int tmp = Integer.MAX_VALUE;
			for(int i =0;i<N;i++) {
				int sum = 0;
				for(int j =0;j<M;j++)			
					sum+=fake_field[i][j];
				tmp = Math.min(tmp, sum);
			}
//			System.out.print("tmp:"+tmp+" answer:"+answer+" ==> ");
			answer = Math.min(tmp, answer);
			return;
		}
		for(int i =0;i<R;i++) {
			if(checked[i])continue;
			checked[i]=true;
			newarr[depth]=arr[i];
			permutation(depth+1,i);
			checked[i]=false;
		}
	}
	public static void main(String[] args) throws IOException {		
		input();
		System.out.println(answer);
	}
}