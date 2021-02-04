package boj2263;

import java.io.*;
import java.util.*;
public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb= new StringBuilder();
	static StringTokenizer st;
	static int N;
	static int[] postorder,inorder,pos;
	static void preorder(int instart,int inend,int poststart,int postend) {
		if(instart>=inend || poststart>=postend)return;
		int root = postorder[postend-1];
		sb.append(root).append(" ");
		int mid = pos[root-1];
		int lens = mid-instart;
		preorder(instart,mid,poststart,poststart+lens);
		preorder(mid+1,inend,poststart+lens,postend-1);
		return;
	}
	public static void main(String[] args) throws IOException{
		N = Integer.parseInt(bf.readLine());
		postorder = new int[N];
		inorder = new int[N];
		pos = new int[N];
		st = new StringTokenizer(bf.readLine());
		for(int i =0;i<N;i++)inorder[i] = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(bf.readLine());
		for(int i =0;i<N;i++)postorder[i] = Integer.parseInt(st.nextToken());
		for(int i =0;i<N;i++)pos[inorder[i]-1] = i;
		preorder(0,N,0,N);
		System.out.println(sb);
	}
}
