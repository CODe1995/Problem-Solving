package boj14888;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, arr[],max=Integer.MIN_VALUE,min=Integer.MAX_VALUE;
	static void permutation(int plus, int minus, int multi, int div,int depth,int sum) {
//		System.out.println(plus+","+minus+","+multi+","+div+" : "+sum);
		if(depth==N) {
			min = Math.min(min, sum);
			max = Math.max(max, sum);
			return;
		}
		if(plus>0)permutation(plus-1,minus,multi,div,depth+1,sum+arr[depth]);
		if(minus>0)permutation(plus,minus-1,multi,div,depth+1,sum-arr[depth]);
		if(multi>0)permutation(plus,minus,multi-1,div,depth+1,sum*arr[depth]);
		if(div>0)permutation(plus,minus,multi,div-1,depth+1,sum/arr[depth]);
	}
	public static int stoi(String s ) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<N;i++)arr[i]=Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		permutation(stoi(st.nextToken()),stoi(st.nextToken()),stoi(st.nextToken()),stoi(st.nextToken()),1,arr[0]);
		System.out.println(max+"\n"+min);
//			operation[i]=Integer.parseInt(st.nextToken());
		//+ - * /
	}
}
