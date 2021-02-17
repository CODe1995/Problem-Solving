package boj1992;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static char field[][];
	static void solution(int n,int x,int y) {
		boolean flag = true;
		int prev = field[y][x];
		for(int i =0;i<n;i++) {
			for(int j =0;j<n;j++)
				if(field[y+i][x+j]!=prev) {
					flag = false;
					break;
				}
			if(!flag)break;
		}
		if(flag)sb.append(prev-48);
		else {
			sb.append("(");
			solution(n/2,x,y);
			solution(n/2,x+n/2,y);
			solution(n/2,x,y+n/2);
			solution(n/2,x+n/2,y+n/2);
			sb.append(")");
		}
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		field = new char[N][N];
		for(int i =0;i<N;i++) {
			String tmp = br.readLine();
			for(int j =0;j<N;j++)
				field[i][j] = tmp.charAt(j);
		}
		solution(N,0,0);
		System.out.println(sb);
	}
}
