package boj2437;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, weightList[];
	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		weightList = new int[N];
		for(int i = 0;i<N;i++)
			weightList[i] = Integer.parseInt(st.nextToken());
	}
	
	static void play() {
		Arrays.sort(weightList);
		int sum = 0;
		for(int i = 0;i<N;i++) {
			if(sum+1<weightList[i])
				break;
			sum += weightList[i];
		}
		System.out.println(sum+1);
	}

	public static void main(String[] args) throws IOException {
		input();
		play();
	}
}
