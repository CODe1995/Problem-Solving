package boj1939;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M, start, end, maxCost;
	static ArrayList<ArrayList<Node>> graph;

	static class Node {
		int dest, cost;

		public Node(int dest, int cost) {
			this.dest = dest;
			this.cost = cost;
		}
	}

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		maxCost = 0;

		graph = new ArrayList<>();
		for (int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a, b, c;
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			maxCost = Math.max(maxCost, c);
			graph.get(a).add(new Node(b, c));// 양방향
			graph.get(b).add(new Node(a, c));
		}

		st = new StringTokenizer(br.readLine());
		start = Integer.parseInt(st.nextToken());
		end = Integer.parseInt(st.nextToken());
	}

	static void play() {
		int left = 0, right = maxCost;
		int mid = 0;
		while (left <= right) {
			mid = (left + right) / 2;
			if (bfs(mid)) {
				left += 1;
			} else {
				right -= 1;
			}
		}
		System.out.println((left + right) / 2);
	}

	static boolean bfs(int cost) {
		boolean visited[] = new boolean[N + 1];
		Queue<Integer> q = new LinkedList<>();
		q.add(start);
		visited[start] = true;
		while (!q.isEmpty()) {
			int cur = q.poll();
			// 종료조건
			if (cur == end)
				return true;

			for (Node node : graph.get(cur)) {
				// 방문체크
				if (visited[node.dest])
					continue;
				// 코스트체크
				if (node.cost >= cost) {
					q.add(node.dest);
					visited[node.dest] = true;
				}
			}
		}
		return false;
	}

	public static void main(String[] args) throws IOException {
		input();
		play();
	}
}