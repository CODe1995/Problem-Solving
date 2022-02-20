package swea1251_하나로;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer, N;
	static Island[] island;
	static double E;
	static int parent[];
	static PriorityQueue<Load> loads;

	static void init() throws IOException {
		answer = 0;
		N = Integer.parseInt(br.readLine());
		parent = new int[N];
		for (int i = 0; i < N; i++)
			parent[i] = i;
		island = new Island[N];
		for (int i = 0; i < N; i++) {
			island[i] = new Island();
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			island[i].x = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			island[i].y = Integer.parseInt(st.nextToken());
		}
		E = Double.parseDouble(br.readLine());
	}

	static class Island {
		int x, y;
	}

	static long getDistancePow(int a, int b) {
		long xAbs = Math.abs(island[a].x - island[b].x);
		long yAbs = Math.abs(island[a].y - island[b].y);
		long xDiff = xAbs * xAbs;
		long yDiff = yAbs * yAbs;
		return xDiff + yDiff;
	}

	static void makeLoad() {
		loads = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				if(i==j)
					continue;
				long dist = getDistancePow(i, j);
				Load load = new Load();
				load.src = i;
				load.dest = j;
				load.dist = dist;
				loads.add(load);
			}
		}
	}
	
	static long getTotalDist() {
		int cnt = 0;
		long totalDist = 0;
		while(!loads.isEmpty()) {
			Load load = loads.poll();
			if(getParent(load.src) == getParent(load.dest))
				continue;	
			totalDist += load.dist;
			combineParent(load.src, load.dest);
			cnt++;
			if(cnt == N-1) {
				break;
			}
		}
		return totalDist;
	}

	static class Load implements Comparable<Load> {
		int src, dest;
		long dist;

		@Override
		public int compareTo(Load o) {
			return Long.compare(dist, o.dist);
		}
	}

	static int getParent(int x) {
		if (x == parent[x])
			return x;
		return parent[x] = getParent(parent[x]);
	}

	static void combineParent(int a, int b) {
		a = getParent(a);
		b = getParent(b);
		if (a == b)
			return;
		if (a < b) {
			parent[b] = a;
		} else {
			parent[a] = b;
		}
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			makeLoad();
			long ans = Math.round(getTotalDist()*E);
			System.out.println("#" + tc + " " + ans);
		}
	}
}