package boj9252;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		char[] A = br.readLine().toCharArray();
		char[] B = br.readLine().toCharArray();
		int dp[][] = new int[B.length+1][A.length+1];
		int max = 0;
		for(int i =1;i<=B.length;i++) {//dp init
			for(int j=1;j<=A.length;j++) {
				if(B[i-1]==A[j-1]) {
					dp[i][j] = dp[i-1][j-1]+1;
				}
				else {
					dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
				}
			}
		}
		int i=B.length, j=A.length;
		Stack<Character> stack = new Stack<>();
		while(i>=1 && j>=1) {
			if(dp[i][j]==dp[i-1][j])i--;
			else if(dp[i][j]==dp[i][j-1])j--;			
			else {//상,좌 다를때
				max = Math.max(max, dp[i][j]);
//				sb.append(A[j-1]);
				stack.add(A[j-1]);
				i--;j--;
			}
		}
				
		
		
		System.out.println(max);
		for(i =0;i<max;i++) {
			System.out.print(stack.pop());	
		}
		
		
	}
}