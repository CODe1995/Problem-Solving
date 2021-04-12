package swea5644;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int M,A,moveA[],moveB[],answer,AX,AY,BX,BY;
	static int[][] direction = new int[][] {{0,0},{0,-1},{1,0},{0,1},{-1,0}};//X상우하좌
	static ArrayList<AP> aps;
	static class AP implements Comparable<AP>{
		int x,y,length,power;
		public AP(int x, int y, int length, int power) {
			this.x = x;
			this.y = y;
			this.length = length;
			this.power = power;
		}
		@Override
		public int compareTo(AP o) {
			return o.power-this.power;//파워 큰 순 정렬
		}
	}
	static void move() {
		AX=0;AY=0;BX=9;BY=9;
		for(int t=0;t<=M;t++) {
			int maxP = 0; //이번 시간에서 얻을 수 있는 최대 파워
			//가능한 AP 수집
			ArrayList<Integer> aPos = new ArrayList<>();
			ArrayList<Integer> bPos = new ArrayList<>();
			for(int i=0;i<A;i++) {//각 송신기별 거리 탐색
				AP ap = aps.get(i);
				int da = Math.abs(AX-ap.x) + Math.abs(AY-ap.y);
				int db = Math.abs(BX-ap.x) + Math.abs(BY-ap.y);
				if(ap.length>=da)aPos.add(i);
				if(ap.length>=db)bPos.add(i);
			}
			if(!aPos.isEmpty()||!bPos.isEmpty()) {
				if(!aPos.isEmpty() && !bPos.isEmpty()) {//둘 다 가능한 AP가 있을 때
					if(aPos.get(0)==bPos.get(0)) {//만약 둘 다 최고 파워가 같은 AP라면					
						if(aPos.size()>=2) maxP = Math.max(aps.get(aPos.get(1)).power+aps.get(bPos.get(0)).power,maxP);
						if(bPos.size()>=2) maxP = Math.max(aps.get(aPos.get(0)).power+aps.get(bPos.get(1)).power,maxP);
					}
					else maxP = Math.max(aps.get(aPos.get(0)).power+aps.get(bPos.get(0)).power,maxP);
				}
				if(!aPos.isEmpty()) maxP = Math.max(aps.get(aPos.get(0)).power,maxP);
				if(!bPos.isEmpty()) maxP = Math.max(aps.get(bPos.get(0)).power,maxP);
				answer+=maxP;			
			}
			if(t==M)continue;			
			AX += direction[moveA[t]][0];
			AY += direction[moveA[t]][1];
			BX += direction[moveB[t]][0];
			BY += direction[moveB[t]][1];
		}
	}
	static void input() throws IOException {
		int T = stoi(br.readLine());
		for(int t=1;t<=T;t++) {
			answer = 0;
			st = new StringTokenizer(br.readLine());
			M = stoi(st.nextToken());//필드크기
			A = stoi(st.nextToken());//BC갯수
			moveA = new int[M];
			moveB = new int[M];
			st = new StringTokenizer(br.readLine());
			for(int i =0;i<M;i++)moveA[i]=stoi(st.nextToken());
			st = new StringTokenizer(br.readLine());
			for(int i =0;i<M;i++)moveB[i]=stoi(st.nextToken());
			aps = new ArrayList<>();
			for(int i=0;i<A;i++) {
				st = new StringTokenizer(br.readLine());
				aps.add(new AP(stoi(st.nextToken())-1,stoi(st.nextToken())-1,stoi(st.nextToken()),stoi(st.nextToken())));
			}	
			Collections.sort(aps);
			move();
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
	}
	public static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();		
		System.out.println(sb);
	}
}