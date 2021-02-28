package boj1967;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static HashMap<Integer, ArrayList<Node>> graph = new HashMap<>();
	static boolean visited[] = new boolean[10001];
	static int deepNode,answer;
	static class Node{
		int node,length;
		public Node(int node, int length) {this.node = node;this.length = length;}
	}
	static void dfs(int node,int sum) {
		if(visited[node])return;//방문 가지치기
		visited[node] = true;
		if(sum>answer) {
			answer = sum;
			deepNode = node;
		}
		for(int i =0;i<graph.get(node).size();i++) {
			dfs(graph.get(node).get(i).node,sum+graph.get(node).get(i).length);
		}
	}

	public static void main(String[] args) throws IOException {
		int N = stoi(br.readLine());
		for(int i =0;i<N-1;i++) {
			st = new StringTokenizer(br.readLine());
			int node = stoi(st.nextToken());
			int childNode = stoi(st.nextToken());
			int length = stoi(st.nextToken());
			if(!graph.containsKey(node))graph.put(node, new ArrayList<Node>());//초기화
			if(!graph.containsKey(childNode))graph.put(childNode, new ArrayList<Node>());//자식노드 초기화			
			graph.get(node).add(new Node(childNode,length));
			graph.get(childNode).add(new Node(node,length));//양방향(무방향)그래프
		}
		if(graph.size()>0) {
			dfs(1,0);
			visited = new boolean[10001];
			dfs(deepNode,0);
		}
		System.out.println(answer);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}