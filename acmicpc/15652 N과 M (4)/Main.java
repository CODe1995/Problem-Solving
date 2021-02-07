package boj15652;

import java.util.Scanner;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static Scanner sc = new Scanner(System.in);
	static int N,M;
	static int[] newarr;
	static void solution(int depth,int index) {
		if(depth==M) {
			for(int i =0;i<M;i++) {
				sb.append(newarr[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		for(int i =index;i<N;i++) {
			newarr[depth] = i+1;
			solution(depth+1,i);
		}
	}
	public static void main(String[] args) {
		N = sc.nextInt();
		M = sc.nextInt();
		newarr=new int[M];
		solution(0,0);
		System.out.println(sb);
	}
}