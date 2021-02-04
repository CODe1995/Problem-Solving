package boj10999;

import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb= new StringBuilder();
	static StringTokenizer st;
	static int N,M,K;
	static long[] lazy,nodes,tree;
	static void propagate(int start,int end,int index) {//checked
		if(lazy[index]!=0) {
			tree[index]+=lazy[index]*(end-start+1);
			if(start!=end) {
				lazy[index*2]+=lazy[index];
				lazy[index*2+1]+=lazy[index];
			}
			lazy[index]=0;
		}
	}
	static void update(int start,int end,int index,int left,int right,long changeNum) {
		propagate(start,end,index);
		if(left>end || right<start)return;
		if(left<=start && right>=end) {//여기때문에 TLE났었음..
//			tree[index] += (end-start+1)*changeNum;
//			if(start!=end) {
//				lazy[index*2]+=changeNum;
//				lazy[index*2+1]+=changeNum;
//			}
			lazy[index]=changeNum;
			propagate(start,end,index);
			return;
		}
		int mid = (start+end)>>1;
		update(start,mid,index*2,left,right,changeNum);
		update(mid+1,end,index*2+1,left,right,changeNum);
		tree[index]=tree[index*2]+tree[index*2+1];
	}
	static long query(int start,int end,int index,int left,int right) {//checked
		propagate(start,end,index);
		if(left>end||right<start)return 0;
		if(left<=start&&end<=right)return tree[index];
		int mid = (start+end)>>1;
		return query(start,mid,index*2,left,right)+query(mid+1,end,index*2+1,left,right);
	}
	static long init(int start, int end, int index) {//checked
		if(start==end)return tree[index]=nodes[start];
		int mid = (start+end)>>1;
		return tree[index] = init(start,mid,index*2)+init(mid+1,end,index*2+1);
	}
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
//		int height = (int)Math.ceil(Math.log10((double)N)/Math.log(2));
//		int size = (int)Math.pow(2, height+1);
		int size = N*4;
		tree= new long[size];
		lazy= new long[size];
		nodes = new long[N];
		for(int i =0;i<N;i++)
			nodes[i] = Integer.parseInt(bf.readLine());
		init(0,N-1,1);
		for(int i =0;i<M+K;i++) {
			st = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(st.nextToken());
			if(a==1) {
				int left = Integer.parseInt(st.nextToken());
				int right = Integer.parseInt(st.nextToken());
				long value = Integer.parseInt(st.nextToken());
				update(0,N-1,1,left-1,right-1,value);
			}
			else{
				int left = Integer.parseInt(st.nextToken());
				int right = Integer.parseInt(st.nextToken());				
				sb.append(query(0,N-1,1,left-1,right-1)).append("\n");
			}
		}
		System.out.println(sb);
	}
}
