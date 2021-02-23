package boj20055;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,K,answer;
	static ArrayList<Belt> dq;
	static class Belt{
		int durability;
		boolean robot;
		public Belt(int durability, boolean robot) {
			this.durability = durability;
			this.robot = robot;
		}
	}
	static void solution() {
		int zero_cnt = 0;//내구도 0인 컨베이어 벨트 수
		while(true) {
			answer++;
			dq.add(0,dq.remove(N*2-1));//컨베이어 벨트 한칸씩 이동
			for(int i=N-1;i>-1;i--) {//로봇있는지 탐색
				Belt curbelt = dq.get(i);//벨트의 상태를 가져옴
				if(!curbelt.robot)continue;//로봇 없다면 패스
				
				curbelt.robot=false;//현재 로봇은 다음칸으로 가거나 사라지므로 미리 없애준다.
				if(i==N-1) {continue;}//끝에 도달했다면?				
				
				Belt nextbelt = dq.get(i+1);//이동할 벨트 상황
				if(nextbelt.durability>0 && !nextbelt.robot) {//내구도 1이상, 로봇 없다면 로봇이동					
					if(nextbelt.durability==1) {//다음이 0이므로 내구도 0 갯수 증가
						zero_cnt++;
						if(zero_cnt==K)return;
					}
					nextbelt.robot=true;//로봇이동시키기
					nextbelt.durability--;
				}else curbelt.robot=true;//다음으로 이동을 못했으므로
			}
			Belt firstbelt = dq.get(0);
			if(firstbelt.durability>0 && !firstbelt.robot) {//내구도 1이상, 로봇없다면
				if(firstbelt.durability==1) {//현재벨트 내구도가 1이면 0될 예정
					zero_cnt++;
					if(zero_cnt==K)return;
				}
				firstbelt.durability--;
				firstbelt.robot=true;
			}
			Belt lastbelt = dq.get(N-1);
			if(lastbelt.robot) {//마지막에 로봇이 있다면?
				lastbelt.robot=false;
			}
		}
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		dq = new ArrayList<>();//내구도,로봇이 있는지 여부 체크
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<2*N;i++)dq.add(new Belt(Integer.parseInt(st.nextToken()),false));
		solution();
		System.out.println(answer);
	}
}