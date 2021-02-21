package boj2116;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,answer;
	static int dice[][];
	static int max4(int a,int b,int c,int d) {
		return Math.max(a, Math.max(b, Math.max(c, d)));
	}
	static int sideMax(int up_index,int df[]) {//윗면 숫자 index, 주사위전개도
		//옆면에서 가장 큰 수를 return
		switch(up_index) {
		case 1:case 6:return max4(df[2],df[3],df[4],df[5]);
		case 2:case 4:return max4(df[1],df[3],df[5],df[6]);
		case 3:case 5:return max4(df[1],df[2],df[4],df[6]);	
		}
		return -1;
	}
	static int findIndex(int value, int field[]) {//값으로 index 반환
		for(int i =1;i<=6;i++) {
			if(field[i]==value) {
				return i;
			}
		}
		return -1;
	}
	static int oppo(int index) {//반대편(마주보는) 숫자를 알려줌
		switch(index) {
		case 1:return 6;
		case 2:return 4;
		case 3:return 5;
		case 6:return 1;
		case 5:return 3;
		case 4:return 2;
		}
		return -1;
	}
	static void solution(int depth,int down_value,int sum) {//depth, 주사위 아랫면 값, 옆면 합
		if(depth==N) {
			answer = Math.max(answer, sum);
			return;
		}		
		int current_down_index = findIndex(down_value,dice[depth+1]);
		int current_up_index = oppo(current_down_index);		
		int current_up_value = dice[depth+1][current_up_index];
		solution(depth+1, current_up_value ,sum+sideMax(current_up_index,dice[depth+1]));
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		dice = new int[N+1][7];
		//  1
		// 2345  1이 윗면, 6이 아랫면
		//  6
		// 1-6, 2-4, 3-5, 4-2, 5-3, 6-1  대치 관계
		for(int i =1; i<=N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =1;j<=6;j++)dice[i][j] = Integer.parseInt(st.nextToken());
		}
		for(int i =1;i<=6;i++) {//1번 주사위를 1~6면까지
			solution(0,dice[1][i],0);
		}
		System.out.println(answer);
	}
}