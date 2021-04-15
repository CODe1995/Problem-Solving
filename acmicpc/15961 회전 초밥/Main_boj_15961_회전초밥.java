package jungol2577;
import java.util.*;
import java.io.*;

public class Main_jungol_2577_회전초밥 {
	static StringBuilder sb = new StringBuilder();
	static int N,D,K,C,arr[],visited[],answer;
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());//레일크기
		D = stoi(st.nextToken());//초밥가짓수
		K = stoi(st.nextToken());//연속된접시수
		C = stoi(st.nextToken());//쿠폰번호
		arr = new int[N];
		for(int i =0;i<N;i++)arr[i]=Integer.parseInt(br.readLine());
		visited = new int[D+1];
		solution();
	}
	static void solution() {
		int unique = 0;
		for(int i=0;i<K;i++) {
			if(visited[arr[i]]==0)unique++;
			visited[arr[i]]++;
		}
		answer = unique;
		for(int i =1;i<N;i++) {
			if(unique>=answer) {
				if(visited[C]==0)answer=unique+1;
				else answer=unique;
			}
			//sliding window
			visited[arr[i-1]]--;//pop
			if(visited[arr[i-1]]==0)unique--;
			if(visited[arr[(i+K-1)%N]]==0)unique++;
			visited[arr[(i+K-1)%N]]++;//push
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(answer);
	}
}