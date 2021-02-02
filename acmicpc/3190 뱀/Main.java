package boj3190;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static class Pos{
		int x,y;
		Pos(int x,int y){
			this.x = x;
			this.y = y;
		}
	}
	static class Move{
		int move;
		char direction;
		public Move(int move, char direction) {
			this.move = move;
			this.direction = direction;
		}
	}
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,K,L;
	static int dirX[] = {1,0,-1,0};//우하좌상
	static int dirY[] = {0,1,0,-1};
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());//필드수
		int[][] field = new int[N][N];
		
		st = new StringTokenizer(bf.readLine());
		K = Integer.parseInt(st.nextToken());//사과
		
		for(int i =0;i<K;i++) {
			st = new StringTokenizer(bf.readLine());
			field[Integer.parseInt(st.nextToken())-1][Integer.parseInt(st.nextToken())-1]=1;//사과는 1
		}		
		
		Deque<Pos> snake = new ArrayDeque<Main.Pos>();//뱀 관리 꼬리-몸통-머리 순
		snake.add(new Pos(0,0));//몸추가
		field[0][0]=2;//뱀은 2
		Deque<Move> query = new ArrayDeque<>();//정수X, 문자C
		
		st = new StringTokenizer(bf.readLine());
		L = Integer.parseInt(st.nextToken());//방향전환 횟수
		
		for(int i =0;i<L;i++) {//쿼리삽입
			st = new StringTokenizer(bf.readLine());
			query.add(new Move(Integer.parseInt(st.nextToken()),st.nextToken().charAt(0)));
		}

		int cur_direction = 0;//오른쪽으로 스타트
		int answer =0 ;
		while(true) {
			Move tmp = query.poll();
			int move = 99999;//쿼리를 다 수행했더라도 뱀은 계속 움직여야함.
			if(tmp != null)
				move = tmp.move;
			for(int i =answer;i<move;i++) {
				//다음 이동되는 좌표
				int nx = snake.peekLast().x+dirX[cur_direction];
				int ny = snake.peekLast().y+dirY[cur_direction];
				if(0<=nx && nx<N && 0<=ny && ny<N && field[ny][nx]!=2) {
					if(field[ny][nx]==1) {//사과가있는 경우 몸을 늘린다.
						field[ny][nx]=2;
						snake.addLast(new Pos(nx,ny));//머리를 사과자리에.
					}
					else {//단순이동
						Pos tmp2 = snake.pollFirst();//꼬리제거
						field[tmp2.y][tmp2.x]=0;
						snake.addLast(new Pos(nx,ny));//머리로이동
						field[ny][nx]=2;
					}
					answer++;
//					System.out.println("=================="+answer);
//					for(int z =0;z<field.length;z++) {
//						System.out.println(Arrays.toString(field[z]));
//					}
				}
				else {//벽에 또는 몸통에 부딪히면 게임종료
					System.out.println(answer+1);
					return;
				}
			}
			//움직인 이후 방향전환
			if(tmp.direction=='D') {
				cur_direction++;
				if(cur_direction>3)cur_direction=0;
			}
			else if(tmp.direction=='L') {
				cur_direction--;
				if(cur_direction<0)cur_direction=3;
			}
		}
		
	}
}