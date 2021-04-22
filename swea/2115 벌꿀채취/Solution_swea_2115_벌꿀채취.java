package swea;
import java.util.*;
import java.io.*;

public class Solution_swea_2115_벌꿀채취 {
	static StringBuilder sb = new StringBuilder();
	static int field[][], M, C, answer;	
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = stoi(br.readLine());
		for(int tc=1;tc<=TC;tc++) {
			st = new StringTokenizer(br.readLine());
			int N = stoi(st.nextToken());
			M = stoi(st.nextToken());
			C = stoi(st.nextToken());
			field = new int[N][N];
			for(int i =0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				for(int j =0;j<N;j++)
					field[i][j] = stoi(st.nextToken());
			}
			answer = Integer.MIN_VALUE;
			for(int i =0;i<N;i++) {//1번째 선택
				for(int j =0;j<N;j++) {
					if(j+M>N)continue;//1번째 선택 범위초과
					int first = getProfit(j,i);
					int second = 0;
					for(int k=i;k<N;k++) {//2번째 선택
						for(int l=0;l<N;l++) {
							if(k==i && l<j+M)continue;
							if(l+M>N)continue;//두번째 선택 범위초과
							second = getProfit(l,k);							
							answer = Math.max(answer, first+second);
						}
					}
				}
			}
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
	}
	static int getProfit(int x,int y) {
		int[] arr = new int[M];
		for(int i =0;i<M;i++)arr[i] = field[y][x+i];
		return powerSet(0,arr,0,0,0);
	}
	static int powerSet(int depth,int array[],int sum,int powsum,int maxPowSum) {
		if(depth==M) {			
			if(sum>C)return 0;
			return powsum;
		}
		maxPowSum = Math.max(maxPowSum, powerSet(depth+1,array,array[depth]+sum,array[depth]*array[depth]+powsum,maxPowSum));
		maxPowSum = Math.max(maxPowSum, powerSet(depth+1,array,sum,powsum,maxPowSum));
		return maxPowSum;
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}