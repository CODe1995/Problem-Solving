import java.util.*;
import java.io.*;

public class boj_20057_마법사_상어와_토네이도 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int field[][];
	static int N, answer;
	//1 1 2 2 5 7 7 10 10 55
	static int[][][] spread_field = new int[][][]{
		{{0,0,2,0,0},{0,10,7,1,0},{5,55,0,0,0},{0,10,7,1,0},{0,0,2,0,0}},//서
		{{0,0,0,0,0},{0,1,0,1,0},{2,7,0,7,2},{0,10,55,10,0},{0,0,5,0,0}},//남
		{{0,0,2,0,0},{0,1,7,10,0},{0,0,0,55,5},{0,1,7,10,0},{0,0,2,0,0}},//동
		{{0,0,5,0,0},{0,10,55,10,0},{2,7,0,7,2},{0,1,0,1,0},{0,0,0,0,0}}//북	
		};
	
	//서 남 동 북
	static int direction[][] = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
	static void spread(int x,int y,int d) {//모래를 흩뿌린다
		int origin_sand = field[y][x];//이동하는 좌표에 있는 모래양
		field[y][x]=0;
		if(origin_sand==0)return;//모래없으면 패스
		int added_sand = 0;//더해진 모래
		int vx = x-2;
		int vy = y-2;
		int last_x = -1;
		int last_y = -1;
		for(int i =0;i<5;i++) {
			for(int j =0;j<5;j++) {
				int nx = vx+j;
				int ny = vy+i;				
				float percent = spread_field[d][i][j];
				int add_sand =(int)(origin_sand*(percent/100));
				if(percent==55.0) {
					last_x = nx;
					last_y = ny;
					continue;
				}
				if(nx<0||nx>=N||ny<0||ny>=N) {//좌표 밖으로 이동된다면
					answer += add_sand;								
				}else {//좌표 내				
					field[ny][nx] += add_sand;				
				}
				added_sand+=add_sand;
			}			
		}		
		if(last_x<0||last_x>=N||last_y<0||last_y>=N) {//좌표 밖으로 이동된다면
			answer += origin_sand-added_sand;						
		}else {//좌표 내				
			field[last_y][last_x]+=origin_sand-added_sand;//남은모래더하기				
		}
	}
	
	static void solution() {
		int x = (N-1)/2;
		int y = (N-1)/2;
		int length = 1;//2 회마다 1씩 증가		
		int next_d = 0;//서쪽으로 시작
		int move_cnt = 0;//움직인 횟수
		while(true) {
			move_cnt++;
			for(int i =0;i<length;i++) {//한 방향으로 쭉 나아간다
				x = direction[next_d][0]+x;
				y = direction[next_d][1]+y;
				if(x==-1&&y==0)return;
				spread(x,y,next_d);
			}			
			next_d=(next_d+1)%4;//다음 이동 방향
			if(move_cnt%2==0)
				length++;	
		}
	}
	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		field = new int[N][N];
		for(int i =0;i<N;i++) {
			field[i] = new int[N];
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<N;j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		input();
		solution();
		System.out.println(answer);		
	}
}