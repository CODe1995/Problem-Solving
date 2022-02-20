package swea4006_고속도로건설2;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer, N, M;
	static ArrayList<Load> loads;
	static int[] parent;

	static class Load implements Comparable<Load> {
		int src, dest, cost;

		@Override
		public int compareTo(Load o) {
			return cost - o.cost;
		}
	}

	static void init() throws IOException {
		answer = 0;
		N = Integer.parseInt(br.readLine());
		parent = new int[N + 1];
		for (int i = 0; i <= N; i++)
			parent[i] = i;
		M = Integer.parseInt(br.readLine());
		loads = new ArrayList<>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			Load load = new Load();
			load.src = Integer.parseInt(st.nextToken());
			load.dest = Integer.parseInt(st.nextToken());
			load.cost = Integer.parseInt(st.nextToken());
			loads.add(load);
		}
		Collections.sort(loads);
	}

	static int findParent(int x) {
		if (parent[x] == x)
			return x;
		return parent[x] = findParent(parent[x]);
	}

	static boolean union(int a, int b) {
		a = findParent(a);
		b = findParent(b);
		if (a == b)
			return false;
		if (a < b)
			parent[b] = a;
		else
			parent[a] = b;
		return true;
	}

	static long getAnswer() {
		long answer = 0;
		int cnt = 0;
		for (int i = 0; i < M; i++) {
			Load load = loads.get(i);
			if(union(load.src, load.dest)){
				answer += load.cost;
				if(++cnt == N) {
					break;
				}
			}
		}
		return answer;
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			System.out.println("#" + tc + " " + getAnswer());
		}
	}
}