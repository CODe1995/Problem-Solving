package boj1541;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static void solution() {

	}

	public static void main(String[] args) throws IOException {
		String order[] = br.readLine().split("-");
		int answer=0;
		for(int i =0;i<order.length;i++) {
			int sum = 0;			
			String[] tmp = order[i].split("\\+");//escape
			for(String t:tmp) {
				sum+=Integer.parseInt(t);
			}
//			System.out.println(sum);
			if(i==0)answer+=sum;
			else answer-=sum;
		}
		System.out.println(answer);
	}
}