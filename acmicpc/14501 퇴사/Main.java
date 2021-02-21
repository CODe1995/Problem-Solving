package boj14501;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,answer;
	static Work work[];
	static void solution(int depth,int sum,int prev_rev) {
		if(depth>=N) {
			if(depth==N)sum+=prev_rev;
			answer = Math.max(answer, sum);
			return;
		}
		if(work[depth].cost==1)solution(depth+work[depth].cost,sum+prev_rev+work[depth].revenue,0);
		else solution(depth+work[depth].cost,sum+prev_rev,work[depth].revenue);
		solution(depth+1,sum+prev_rev,0);
	}
	static class Work{
		int cost,revenue;
		public Work() {}
		public Work(int cost, int revenue) {this.cost = cost;this.revenue = revenue;}		
	}
	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		work = new Work[N];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			work[i] = new Work(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
		}
		solution(0,0,0);
		System.out.println(answer);
	}
}