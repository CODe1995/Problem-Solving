package swea1855_영준이의진짜BFS;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static ArrayList<Integer>[] graph;
	static int N, logN;
	static int depths[], parents[][];
	static long answer;

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			answer = 0;
			logN = (int) log2(N)+1;
			parents = new int[N+1][logN];
			depths = new int[N + 1];
			parents[1][0] = 0;
			depths[1] = 1;
			graph = new ArrayList[N + 1];
			for (int i = 0; i < N + 1; i++) {
				graph[i] = new ArrayList<Integer>();
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 2; i <= N; i++) {
				int parent = Integer.parseInt(st.nextToken());
				parents[i][0] = parent;
				graph[parent].add(i);
			}
			setDepthAndParent();
			for (int i = 1; i < logN; i++) {
				for (int j = 1; j < N + 1; j++) {
					parents[j][i] = parents[parents[j][i - 1]][i - 1];
				}
			}
			bfs();
			System.out.println("#" + tc + " " + answer);
		}
	}

	static double log2(int x) {
		return Math.log(x) / Math.log(2);
	}

	static void setDepthAndParent() {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(1);
		while (!queue.isEmpty()) {
			int cur = queue.poll();
			for (int i = 0; i < graph[cur].size(); i++) {
				int child = graph[cur].get(i);
				depths[child] = depths[cur] + 1;
				parents[child][0] = cur;
				queue.add(child);
			}
		}
	}

	static int getDistance(int a, int b) {
		int dist = 0;
		if (depths[a] > depths[b]) {
			int temp = b;
			b = a;
			a = temp;
		}
		for (int i = logN-1; i >= 0; i--) {
			if (depths[b] - depths[a] >= 1 << i) {
				b = parents[b][i];
				dist += 1<<i;
			}
		}
		if (a == b) {
			return dist;
		}
		for (int i = logN-1; i >= 0; i--) {
			if (parents[a][i] != parents[b][i]) {
				a = parents[a][i];
				b = parents[b][i];
				dist+=(1<<i)*2;
			}
		}
		// 같은 부모를 바라보고 depth도 같은 경우
		if(a!=b) {
			return dist+2;
		}
		return dist;
	}

	static void bfs() {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(1);
		int prev = 1;
		while (!queue.isEmpty()) {
			int cur = queue.poll();
			for (int child : graph[cur]) {
				int dist =getDistance(prev, child) ;
				answer += dist;
//				System.out.println(String.format("%s->%s : %s", prev,child,dist));
				prev = child;
				queue.offer(child);
			}
		}
	}
}