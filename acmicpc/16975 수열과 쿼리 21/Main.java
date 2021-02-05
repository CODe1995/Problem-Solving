package boj16975;
import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static long tree[],lazy[];
	static int nodes[];
	static long init(int s,int e,int index) {
		if(s==e)return tree[index]=nodes[s];		
		int mid = s+e>>1;
		return tree[index]=init(s,mid,index*2)+init(mid+1,e,index*2+1);
	}
	static void lazy_update(int s,int e,int index) {
		if(lazy[index]!=0) {
			if(s!=e) {
				lazy[index*2]+=lazy[index];
				lazy[index*2+1]+=lazy[index];
			}
			tree[index]+=lazy[index]*(e-s+1);
			lazy[index]=0;
		}
	}
	static void update(int s,int e,int index,int rs,int re,int diff) {
		lazy_update(s,e,index);
		if(s>re || e<rs) //범위 벗어남
			return;		
		if(rs<=s&&e<=re) {	//AC
//		if(s<=rs&&re<=e) {	//WA
//		if(s==e) {			//TLE
			lazy[index]=diff;
			lazy_update(s,e,index);
			return;
		}
		int mid = s+e >>1;
		update(s,mid,index*2,rs,re,diff);
		update(mid+1,e,index*2+1,rs,re,diff);
		tree[index]=tree[index*2]+tree[index*2+1];
	}
	static long query(int s,int e,int index,int target) {
		lazy_update(s,e,index);
		if(s>target||target>e) {
			return 0;
		}
		if(target<=s&&e<=target) {
			return tree[index];
		}
		int mid=s+e>>1;
		return query(s,mid,index*2,target)+query(mid+1,e,index*2+1,target);
	}
	public static void main(String[] args) throws IOException{
		int N = Integer.parseInt(bf.readLine());
		tree = new long[N*4];
		lazy = new long[N*4];
		nodes = new int[N];
		st=new StringTokenizer(bf.readLine());
		for(int i =0;i<N;i++)
			nodes[i]=Integer.parseInt(st.nextToken());
		init(0,N-1,1);
		int M = Integer.parseInt(bf.readLine());
		for(int i=0;i<M;i++) {
			String[] str = bf.readLine().split(" ");
			int s = Integer.parseInt(str[1]);
			if(str[0].equals("1")) {
				int e = Integer.parseInt(str[2]);
				int diff = Integer.parseInt(str[3]);
				update(0,N-1,1,s-1,e-1,diff);
			}
			else {
				sb.append(query(0,N-1,1,s-1)).append("\n");
			}
		}
		System.out.println(sb);
	}
}
