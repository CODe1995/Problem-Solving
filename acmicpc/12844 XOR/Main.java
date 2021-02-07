package boj12844;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static long tree[],lazy[];
	static int nodes[];
	static void lazy_update(int start,int end,int index) {
		if(lazy[index]!=0) {
			if(start!=end) {
				lazy[index*2]^=lazy[index];
				lazy[index*2+1]^=lazy[index];
			}
			tree[index]^=lazy[index]*((end-start+1)%2);
			lazy[index]=0;
		}
	}
	static long update(int start,int end,int index,int qs,int qe, int diff) {
		lazy_update(start,end,index);
		if(qe<start || end<qs)return tree[index];
		if(qs<=start && end<=qe) {
			lazy[index]=diff;
			lazy_update(start,end,index);
			return tree[index];
		}
		int mid = start+end>>1;
		return tree[index] = update(start,mid,index*2,qs,qe,diff)^update(mid+1,end,index*2+1,qs,qe,diff);		
	}
	static long query(int start,int end,int index,int qs,int qe) {
		lazy_update(start,end,index);
		if(start>qe || qs>end)return 0;
		if(qs<=start&&end<=qe) {
			return tree[index];
		}
		int mid = start+end>>1;
		return query(start,mid,index*2,qs,qe)^query(mid+1,end,index*2+1,qs,qe);
	}
	static long init(int start,int end,int index) {
		if(start==end) {			
			return tree[index]=nodes[start];		
		}
		int mid = start+end >>1;
		return tree[index]=init(start,mid,index*2)^init(mid+1,end,index*2+1);
	}
	public static void main(String[] args) throws IOException {		
		int N = Integer.parseInt(br.readLine());
		tree = new long[N*4];
		lazy = new long[N*4];
		nodes = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<N;i++)nodes[i]=Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(br.readLine());
		init(0,N-1,1);
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if(t==1) {
				int k = Integer.parseInt(st.nextToken());
				update(0,N-1,1,a,b,k);
			}
			else {
				System.out.println(query(0,N-1,1,a,b));
			}			
		}
	}
}
