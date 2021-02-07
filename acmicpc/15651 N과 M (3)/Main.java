package boj15651;

import java.io.IOException;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static StringBuilder sb = new StringBuilder();
	static int N;
	static int M;
	static int[] newarr;
	static void solution(int depth) {
		if(depth==M) {
			for(int i =0;i<M;i++)
				sb.append(newarr[i]).append(" ");
			sb.append("\n");
			return;
		}
		for(int i =0;i<N;i++) {
			newarr[depth]=i+1;
			solution(depth+1);
		}
	}
	public static void main(String[] args) throws IOException{
		N = sc.nextInt();
		M = sc.nextInt();
		newarr = new int[M];
		solution(0);
		System.out.println(sb);
	}
}
