package boj2961;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] foods;
	static boolean[] choice;
	static int N;
	static int answer = Integer.MAX_VALUE;
//	static boolean checked[];
	static void set(int depth,int index) {
		if(depth==N) {
			int sour = 1;//신
			int bit = 0;//쓴
			for(int i =0;i<N;i++) {
				if(choice[i]) {
					sour*=foods[i][0];
					bit+=foods[i][1];
				}
			}
			if(sour==1 && bit==0)return;
//			System.out.print(Arrays.toString(choice));
//			System.out.println(" >>> "+(sour-bit));
			answer = Math.min(answer, Math.abs(sour-bit));
			return;
		}
		for(int i =index;i<N;i++) {
			choice[i] = true;
			set(depth+1,i+1);
			choice[i] = false;
			set(depth+1,i+1);
		}
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		foods = new int[N][2];
		choice = new boolean[N];
//		checked=new boolean[N];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			foods[i][0] = Integer.parseInt(st.nextToken());
			foods[i][1] = Integer.parseInt(st.nextToken());
		}
		set(0,0);
		System.out.println(answer);
		
	}
}