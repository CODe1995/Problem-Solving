package boj1062;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int N,K,answer;
	static String[] arr;
	static boolean selected[];
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
//		arr = new ArrayList<>();
		arr = new String[N];
		for(int i =0;i<N;i++) {
			String s = br.readLine();
			s=s.replaceAll("[antic]", "");//antatica 제외
//			arr.add(s);
			arr[i]=s;
		}
		if(K<5)return;
		if(K==26) {
			answer = N;
			return;
		}
		selected = new boolean[26];
		selected['a'-'a']=true;
		selected['n'-'a']=true;
		selected['t'-'a']=true;
		selected['i'-'a']=true;
		selected['c'-'a']=true;//5개는 고르고 시작
//		answer = counting();
		solve(5,1);
	}
	public static void solve(int depth,int index) {
		if(depth==K) {
			int countPos = counting();
			answer = Math.max(countPos, answer);
			return;
		}
		for(int i = index;i<='z'-'a';i++) {
			if(selected[i])continue;
			selected[i]=true;
			solve(depth+1,i+1);
			selected[i]=false;		
		}
	}
	
	public static int counting() {//익힌 단어의 갯수 반호나
		int possible = 0;		
		for(int i =0;i<N;i++) {
//			char[] cur rr.get(i).toCharArray();
//			char[] cur = arr[i].toCharArray();
			boolean flag = true;
			for(int j =0;j<arr[i].length();j++) {
				char x = arr[i].charAt(j);
				if(!selected[x-'a']) {//하나라도 못익혔으면 의미없음
					flag = false;
					break;
				}
			}
			if(flag)possible++;
		}		
		return possible;
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(answer);
	}
}