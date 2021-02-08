package boj20361;
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	public static void main(String[] args) throws IOException{
		//기본 입력
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());//컵수
		int X = Integer.parseInt(st.nextToken());//정답위치
		int K = Integer.parseInt(st.nextToken());//바꾸는횟수	
		for(int k=0;k<K;k++) {//바꾸는 횟수만큼 반복
			st = new StringTokenizer(br.readLine());//입력
			int a = Integer.parseInt(st.nextToken());//바꾸는 컵 위치
			int b = Integer.parseInt(st.nextToken());//바꾸는 컵 위치
			if(X==a)X=b;//정답이 들어있는 컵을 서로 바꾸게 되면 위치가 바뀌므로 갱신
			else if(X==b)X=a;
		}
		System.out.println(X);
	}
}
