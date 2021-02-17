package boj15686;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer=Integer.MAX_VALUE,N,M;
	static ArrayList<int[]> chicken = new ArrayList<int[]>();
	static ArrayList<int[]> house = new ArrayList<int[]>();
	static int[][] house_del;
	static void refresh(int[] newarr) {
		int[] hd = new int[house.size()];
		Arrays.fill(hd, Integer.MAX_VALUE);
		for(int i = 0;i<M;i++) {
			for(int j =0;j<house.size();j++) {
				if(hd[j] > house_del[newarr[i]][j]){
					hd[j]=house_del[newarr[i]][j];
				}
			}
		}
		int sum = 0;
		for(int i =0;i<house.size();i++) {
			sum+=hd[i];
		}
		answer= Math.min(answer, sum);
	}
	static boolean checked[];
	static void combination(int depth,int[] newarr,int index) {
		if(depth==M) {
//			System.out.println(Arrays.toString(newarr));
			refresh(newarr);
			return;
		}
		for(int i = index;i<chicken.size();i++) {
			newarr[depth] = i;
			combination(depth+1,newarr,i+1);
		}
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<N;j++) {
				int c = Integer.parseInt(st.nextToken());
				if(c==2)
					chicken.add(new int[] {j,i});
				else if(c==1)
					house.add(new int[] {j,i});
			}
		}
		house_del = new int[chicken.size()][house.size()];
		for(int i =0;i<chicken.size();i++) {
			int cx = chicken.get(i)[0];
			int cy = chicken.get(i)[1];
			for(int j =0;j<house.size();j++) {
				int hx = house.get(j)[0];
				int hy = house.get(j)[1];
				house_del[i][j] = Math.abs(hy-cy)+Math.abs(hx-cx);
			}
		}
		checked = new boolean[chicken.size()];
		combination(0,new int[M],0);
		System.out.println(answer);
	}
}