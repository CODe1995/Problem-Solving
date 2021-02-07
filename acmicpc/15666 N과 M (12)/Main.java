package boj15666;
import java.util.*;
import java.io.*;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int N,M,arr[], newarr[];
	static void solution(int depth,int index) {
		if(depth==M) {
			for(int i =0;i<M;i++) {
				sb.append(newarr[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		int prev = -1;
		for(int i =index;i<N;i++) {
			if(prev==arr[i])continue;
			prev = arr[i];
			newarr[depth]=arr[i];
			solution(depth+1,i);
		}
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N];
		newarr = new int[M];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<N;i++)arr[i] = Integer.parseInt(st.nextToken());
		Arrays.sort(arr);
		solution(0,0);
		System.out.println(sb);
	}
}
