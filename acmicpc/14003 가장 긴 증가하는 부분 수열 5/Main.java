package boj14003;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();

	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int arr[] = new int[N+1];
		st = new StringTokenizer(br.readLine());
		for(int i =1;i<=N;i++)arr[i]=Integer.parseInt(st.nextToken());
		Vector<Integer> v = new Vector<>();
		v.add(arr[1]);
		int dp[] = new int[N+1];
		for(int i=2;i<=N;i++) {
			if(v.lastElement()<arr[i]) {
				v.add(arr[i]);
				dp[i]=v.size()-1;//index 기록
				continue;
			}
			int index = Collections.binarySearch(v, arr[i]);
			if(index<0)index=-index-1;
			v.set(index,arr[i]);
			dp[i]=index;
		}
		int answer = v.size();
//		if(v.isEmpty()||v.get(0)<0)answer++;
		sb.append(answer).append("\n");
		Vector<Integer> print = new Vector<>();
		int topIndex = v.size()-1;
		for(int i =N;i>=1;i--) {
			if(dp[i]==topIndex) {
				print.add(arr[i]);
				topIndex--;
			}
		}
		for(int i =print.size()-1;i>=0;i--) {
			sb.append(print.get(i)).append(" ");
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}