package swea3282_01Knapsack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	static class Product implements Comparable<Product> {
		int weight;
		int cost;

		public Product(int weight, int cost) {
			this.weight = weight;
			this.cost = cost;
		}

		@Override
		public int compareTo(Product o) {
			if (cost == o.cost) {
				return weight - o.weight;
			}
			return cost - o.cost;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int tc = 1; tc <= T; tc++) {
			ArrayList<Product> arr = new ArrayList<>();
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int v = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				Product product = new Product(v, c);
				arr.add(product);
			}
			Collections.sort(arr);
			int dp[] = new int[K + 1];
			for (int i = 0; i < N; i++) {
				for (int j = K; j >= 0; j--) {
					Product product = arr.get(i);
					if (product.weight <= j) {
						dp[j] = Integer.max(dp[j], dp[j - product.weight] + product.cost);
					}
				}
			}

			sb.append("#").append(tc).append(" ").append(dp[K]).append("\n");
		}
		System.out.println(sb);
	}
}
