package boj1167;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static HashMap<Integer, ArrayList<Node>> graph = new HashMap<>();
	static int V, answer, deepNode;
	static boolean visited[] = new boolean[100001];
	static class Node{
		int node,length;//노드번호, 간선길이
		public Node(int node, int length) {this.node = node;this.length = length;}
	}
	static void dfs(int node,int sum) {
		if(visited[node])return;//재방문 가지치기
		visited[node]=true;
		if(sum>answer) {
			answer = sum;
			deepNode = node;
		}
		for(int i=0;i<graph.get(node).size();i++) {
			dfs(graph.get(node).get(i).node,sum+graph.get(node).get(i).length);
		}
	}

	public static void main(String[] args) throws IOException {
		V = stoi(br.readLine());
		for(int i =1;i<=V;i++) {
			st = new StringTokenizer(br.readLine());
			int node = stoi(st.nextToken());
			graph.put(node, new ArrayList<Node>());//초기화
			while(true) {
				int childnode = stoi(st.nextToken());
				if(childnode==-1)break;//EXIT FLAG
				int length = stoi(st.nextToken());
				graph.get(node).add(new Node(childnode,length));
			}			
		}//그래프 만들기
		dfs(1,0);//진짜 루트 찾기
		visited= new boolean[100001];//방문초기화
		dfs(deepNode,0);//진짜 루트에서 검색
		System.out.println(answer);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}