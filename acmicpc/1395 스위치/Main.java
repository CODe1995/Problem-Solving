package boj1395;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static long tree[],lazy[];
	static long nodes[];
	static long init(int start,int end,int index) {
		if(start==end) return tree[index]=nodes[start];
		int mid = start+end>>1;
		return tree[index] = init(start,mid,index*2)+init(mid+1,end,index*2+1);
	}
	static void lazy_update(int start,int end,int index) {
		if(lazy[index]!=0) {
			if(start!=end) {
				lazy[index*2]=lazy[index*2]==0?1:0;
				lazy[index*2+1]=lazy[index*2+1]==0?1:0;
			}
			tree[index]=(end-start+1)-tree[index];//범위-현재갯수 = 반전
			lazy[index]=0;
		}
	}
	static void reverse(int start,int end,int index,int qs,int qe) {//update
		lazy_update(start,end,index);
		if(qe<start||end<qs)return;
		if(qs<=start&&end<=qe) {
			tree[index] = (end-start+1)-tree[index];//갯수반전
			if(start!=end) {
				lazy[index*2]=lazy[index*2]==0?1:0;
				lazy[index*2+1]=lazy[index*2+1]==0?1:0;
			}
			lazy[index]=0;
			return;
		}
		int mid = start+end>>1;
		reverse(start,mid,index*2,qs,qe);
		reverse(mid+1,end,index*2+1,qs,qe);
		tree[index]=tree[index*2]+tree[index*2+1];
	}
	static long query(int start,int end,int index,int qs,int qe) {
		lazy_update(start,end,index);
		if(qs>end||qe<start)return 0;
		if(qs<=start&&end<=qe) {
			return tree[index];
		}
		int mid = start+end>>1;		
		return query(start,mid,index*2,qs,qe)+query(mid+1,end,index*2+1,qs,qe);
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		tree = new long[N*4];
		lazy = new long[N*4];
		nodes = new long[N+1];
		init(0,N-1,1);
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			if(a==0) {
				reverse(0,N-1,1,b-1,c-1);
			}else {
				System.out.println(query(0,N-1,1,b-1,c-1));
			}
		}
	}
}
