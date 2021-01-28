package boj1120;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(bf.readLine());
		String A = st.nextToken();
		String B = st.nextToken();
		int answer = 51;//차이를 저장
		for(int i = 0;i<=B.length()-A.length();i++) {
			int cnt=A.length();//차이나는 문자의 갯수
			for(int j = 0; j<A.length();j++) {
//				System.out.printf("i:%d j:%d >>> %c %c\n",i,j,B.charAt(j+i),A.charAt(j));
				if(B.charAt(j+i) == A.charAt(j))cnt--;				
			}
			if(answer>cnt) {//차이가 작을수록 정답
				answer = cnt;//겹치지 않은 갯수
			}
		}
		System.out.println(answer);
	}
}
