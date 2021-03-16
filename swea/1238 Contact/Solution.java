import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,start,answer;
	static HashMap<Integer, ArrayList<Integer>> graph;
	static boolean visited[];
	static void bfs() {
		Deque<Integer> dq = new ArrayDeque<Integer>();
		dq.add(start);
		visited[start]=true;
		int tmp = 0;
		while(!dq.isEmpty()) {
			int dqSize = dq.size();
			tmp = 0;
			for(int i =0;i<dqSize;i++) {				
				int cur = dq.pollFirst();
				tmp = Math.max(tmp, cur);
				if(!graph.containsKey(cur)) {//끝노드인경우
					continue;
				}
				for(int child:graph.get(cur)) {
					if(visited[child]==true)continue;//이미 방문했다면 패스
					dq.add(child);//안했다면 다음 순회에 넣음
					visited[child]=true;
				}				
			}
		}
		answer = Math.max(tmp, answer);
	}
	static void input() throws IOException{		
		st = new StringTokenizer(br.readLine());
		graph = new HashMap<>();
		N = Integer.parseInt(st.nextToken());
		start = Integer.parseInt(st.nextToken());
		visited = new boolean[101];
		answer = 0;
		st = new StringTokenizer(br.readLine());		
		for(int i =0;i<N/2;i++) {
			int num1 = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken());
			if(graph.containsKey(num1)) {
				graph.get(num1).add(num2);
			}else {
				ArrayList<Integer> ar = new ArrayList<>();
				ar.add(num2);
				graph.put(num1, ar);
			}
		}
		bfs();
	}

	public static void main(String[] args) throws IOException {
		for(int t=1;t<=10;t++) {
			input();
			sb.append("#").append(t).append(" ").append(answer).append("\n");			
		}
		System.out.println(sb);
	}
}