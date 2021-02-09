package boj13116;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static void solution() {

	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for(int t=0;t<T;t++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());			
			while(a!=b) {
				while(a>b)a/=2;
				while(b>a)b/=2;
//				System.out.println(a+", "+b);
			}
			System.out.println(a*10);
		}

	}
}