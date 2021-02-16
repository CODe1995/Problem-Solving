package boj1074;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer=0,N,r,c;
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		int x=0,y=0;
		int n = (int)Math.pow(2, N);		
		while (n>0) {
			if(c<x+n/2 && r<y+n/2) {//4사분면에 위치
			}
			else if(c>=n/2+x && r<n/2+y) {//1
				x+=n/2;				
				answer+= n/2 * n/2;
			}
			else if(c>=n/2+x && r>=n/2+y) {//2
				x+=n/2;
				y+=n/2;			
				answer+= (n/2 * n/2)*3;
			}
			else if(c<n/2+x && r>=n/2+y) {//3
				y+=n/2;
				answer+= (n/2 * n/2)*2;
			}
			n>>=1;
		}
		System.out.println(answer);
	}
}