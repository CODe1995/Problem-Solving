package boj1260;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static HashMap<Integer, ArrayList<Integer>> graph;
	static boolean[] visited;
	static int N,M,V;
	static void dfs(int x) {
		if(!graph.containsKey(x))return;
		for(Integer v:graph.get(x)) {
			if(visited[v])continue;
			visited[v]=true;
			sb.append(v).append(" ");
			dfs(v);
		}
	}
	static void bfs() {
		Deque<Integer> dq = new ArrayDeque<Integer>();
		dq.add(V);
		visited[V]=true;
		while(!dq.isEmpty()) {
			int x  = dq.pollFirst();
			sb.append(x).append(" ");
			if(!graph.containsKey(x))continue;			
			for(Integer v:graph.get(x)) {
				if(visited[v])continue;
				visited[v]=true;
				dq.add(v);
			}
		}
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
		graph = new HashMap<>();
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if(graph.containsKey(a))graph.get(a).add(b);
			else graph.put(a, new ArrayList<Integer>(){{add(b);}});
			if(graph.containsKey(b))graph.get(b).add(a);
			else graph.put(b, new ArrayList<Integer>(){{add(a);}});
			graph.get(a).sort((o1,o2)->o1-o2);
			graph.get(b).sort((o1,o2)->o1-o2);
		}		
		visited = new boolean[N+1];
		sb.append(V).append(" ");		
		visited[V]=true;
		dfs(V);
		sb.append("\n");
		visited = new boolean[N+1];
		bfs();
		System.out.println(sb);
	}
}