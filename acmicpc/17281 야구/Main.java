package boj17281;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,answer;
	static int scoreboard[][];	
	static int member_position[] = new int[9];//멤버순서(순열)
	static boolean checked[] = new boolean[9];
	static void play_game() {
		int field[] = new int[4];//홈,1,2,3루
		int position = 0;//포지션
		int score = 0;
		for(int i =0;i<N;i++) {//이닝수만큼 게임시작
			int out = 0;//3되면 다음 이닝시작. 없으면 게임끝
			while(true) {//스코어보드 순서				
				int curF = scoreboard[i][member_position[position++%9]-1];//현재 순서가 취한 행동
				if(curF==0) {//아웃
					out++;
				}else if(curF==1) {//안타(1루 전진)
					field[0]=1;//타자를 대기시킨다.
					if(field[3]==1) {//3루에 사람이 있다면?
						score++;//1점추가
					}
					for(int f=3;f>0;f--) {//한칸씩 땡겨간다(타자는 1루로)
						field[f]=field[f-1];
						field[f-1]=0;//땡겨와진곳에선 초기화
					}
				}else if(curF==2) {//2루전진
					field[0]=1;//타자 대기
					for(int f=2;f<4;f++) {//2~3루에 사람이 있다면?
						if(field[f]==1) {
							score++;
							field[f]=0;//홈에 들어갔음
						}
					}
					for(int f=3;f>1;f--) {
						field[f]=field[f-2];
						field[f-2]=0;//땡겨와진곳에선 초기화
					}
				}else if(curF==3) {//3루 전진
					field[0]=1;//타자 대기
					for(int f=1;f<4;f++) {//1~3루에 사람이 있다면?
						if(field[f]==1) {
							score++;
							field[f]=0;
						}
					}
					for(int f=3;f>2;f--) {
						field[f]=field[f-3];
						field[f-3]=0;//땡겨와진곳에선 초기화
					}
				}else {//4 홈런
					field[0]=1;//타자 대기
					for(int f=0;f<4;f++) {
						if(field[f]==1)score++;					
					}
					field[0]=0;//필드초기화
					field[1]=0;//필드초기화
					field[2]=0;//필드초기화
					field[3]=0;//필드초기화
				}
				if(out==3) {//아웃 3번이라면?
					//이닝을 끝내고 현재 타자는 저장해야함.
					out=0;
					field[0]=0;//필드초기화
					field[1]=0;//필드초기화
					field[2]=0;//필드초기화
					field[3]=0;//필드초기화							
					break;
				}
			}
		}		
		answer = Math.max(answer, score);//최대점수 갱신
	}
	static void permu(int depth) {
		if(depth==9) {
			play_game();//순열이 완성됐다면 게임 시작
			return;
		}
		if(depth==3) {
			permu(depth+1);
			return;
		}
		for(int i =1;i<9;i++) {
			if(checked[i])continue;//이미 선택됐다면 다른 숫자, 4번째는 1번으로 고정			
			checked[i]=true;
			member_position[depth] = i+1;
			permu(depth+1);
			checked[i]=false;			
		}
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		scoreboard = new int[N][9];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<9;j++) {
				scoreboard[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		member_position[3] = 1;
		permu(0);//순열 생성
		System.out.println(answer);
	}
}