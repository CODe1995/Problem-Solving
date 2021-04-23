package boj;
import java.util.*;
import java.io.*;

public class Main_boj_14891_톱니바퀴 {
	static StringBuilder sb = new StringBuilder();
	static ArrayList<Integer> order;
	static boolean visited[] = new boolean[4];
	static class Magnet{
		ArrayList<Integer> status = new ArrayList<>();
		int flagIndex;//기준 index만 있으면 계산 가능
		public void add(int x) {//SN 정보 추가(init)
			status.add(x);
		}
		public void cw() {//시계방향 회전
			flagIndex = (flagIndex==0?8:flagIndex)-1;
		}
		public void ccw() {//반시계방향 회전
			flagIndex = (flagIndex+1)%8;
		}
		public int getScore(int num) {//자석 번호를 인자값으로			
			int pow = (int) Math.pow(2, num-1);
			int head = status.get(flagIndex);
			return head==0?0:pow;
		}
		public int leftStatus() {
			return status.get((flagIndex+6)%8);//왼쪽 자석 정보 넘겨준다
		}
		public int rightStatus() {
			return status.get((flagIndex+2)%8);//오른쪽 자석 정보 넘겨준다
		}
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		Magnet magnet[] = new Magnet[4];
		for(int i =0;i<4;i++) {//자석에 값 추가
			magnet[i] = new Magnet();
			char[] inp = br.readLine().toCharArray();
			for(int j =0;j<8;j++)
				magnet[i].add(inp[j]-48);
		}
		
		int K = stoi(br.readLine());
		for(int k=0;k<K;k++) {//자석 회전 명령 실행
			visited = new boolean[4];
			st = new StringTokenizer(br.readLine());
			int num = stoi(st.nextToken());
			int turn = stoi(st.nextToken());//-1 ccw
			execute(num,turn,magnet);
		}
		
		int answer = 0;
		for(int i=0;i<4;i++)
			answer+=magnet[i].getScore(i+1);
		
		sb.append(answer).append("\n");		
	}
	static void execute(int num,int turn,Magnet[] magnet) {
		int index = num-1;
		if(visited[index])return;//이미 돌렸다면 회전시킨다.
		visited[index]=true;
		if(num<4&&magnet[index].rightStatus() != magnet[index+1].leftStatus())
			execute(num+1,-turn,magnet);
		if(num>1&&magnet[index].leftStatus() != magnet[index-1].rightStatus())
			execute(num-1,-turn,magnet);		
		if(turn==1) magnet[index].cw();
		else magnet[index].ccw();
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();	
		System.out.println(sb);
	}
}