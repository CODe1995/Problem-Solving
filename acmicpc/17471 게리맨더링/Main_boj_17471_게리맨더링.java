package boj17471;
import java.util.*;
import java.io.*;

public class Main_boj_17471_게리맨더링 {
	static StringBuilder sb = new StringBuilder();
	static int N,answer=Integer.MAX_VALUE;
	static int ppl[];//인구수
	static ArrayList[] graph;
	static boolean choice[];
	static int makeNums(int index,int cnt,int scnt) {
		if(cnt>=Math.pow(2, N)/2)return cnt;
		if(index==N+1) {
			if(scnt==N)return cnt+1;
			int sectorA[] = new int[scnt];
			int sectorB[] = new int[N-scnt];
			int sa=0;
			int sb=0;
			for(int i =1;i<=N;i++) {
				if(choice[i])sectorA[sa++]=i;
				else sectorB[sb++]=i;
			}
			BFS();
			return cnt+1;
		}
		choice[index]=true;
		cnt=makeNums(index+1,cnt,scnt+1);
		choice[index]=false;
		cnt=makeNums(index+1,cnt,scnt);		
		return cnt;
	}
	static boolean BFS() {
		//sectorA true
		boolean visited[] = new boolean[N+1];
		int scoreA = 0;
		int scoreB = 0;
		Queue<Integer> q = new LinkedList<Integer>(); 
		for(int i =1;i<=N;i++) {
			if(choice[i]) {
				q.add(i);
				visited[i]=true;
				scoreA+=ppl[i];
				break;
			}
		}
		while(!q.isEmpty()) {
			int cur = q.poll();
			for(int i=0;i<graph[cur].size();i++) {
				int next = (int) graph[cur].get(i);
				if(!visited[next] && choice[next]) {
					q.add(next);
					visited[next]=true;
					scoreA+=ppl[next];
				}
			}
		}
		for(int i=1;i<=N;i++) {
			if(choice[i]!=visited[i])return false;
		}
		//sectorB false
		for(int i =1;i<=N;i++) {
			if(!choice[i]) {
				q.add(i);
				visited[i]=true;
				scoreB+=ppl[i];
				break;
			}
		}
		while(!q.isEmpty()) {
			int cur = q.poll();
			for(int i=0;i<graph[cur].size();i++) {
				int next = (int) graph[cur].get(i);
				if(!visited[next] && !choice[next]) {
					q.add(next);
					visited[next]=true;
					scoreB+=ppl[next];
				}
			}
		}
		for(int i=1;i<=N;i++) {
			if(!visited[i])return false;
		}
		answer = Math.min(Math.abs(scoreA-scoreB), answer);
		return true;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = stoi(br.readLine());
		ppl = new int[N+1];
		choice = new boolean[N+1];
		graph = new ArrayList[N+1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1;i<=N;i++)ppl[i]=stoi(st.nextToken());//인구수 저장
		for(int i=1;i<=N;i++) {
			st = new StringTokenizer(br.readLine());
			graph[i] = new ArrayList<Integer>();
			int gc = stoi(st.nextToken());
			for(int j=0;j<gc;j++) {
				graph[i].add(stoi(st.nextToken()));
			}
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		makeNums(1,0,0);
		System.out.println(answer==Integer.MAX_VALUE?-1:answer);
	}
}