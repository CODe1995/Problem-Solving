package boj2563;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer = 0;
	static int field[][] = new int[100][100];
	
	static void fill(int x,int y) {
		for(int i =0;i<10;i++)
			for(int j =0;j<10;j++) {
				if(field[y+i][x+j]==0)answer++;
				field[y+i][x+j]=1;		
			}
	}
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			fill(x,y);
		}
		System.out.println(answer);		
	}
}