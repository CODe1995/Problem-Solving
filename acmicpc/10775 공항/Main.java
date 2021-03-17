package boj10775;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int G,P;
	static int parent[];
	static int getParent(int x) {
		if(x==parent[x])return x;
		return parent[x] = getParent(parent[x]);
	}
	static void union(int a,int b) {
		a = getParent(a);
		b = getParent(b);		
		if(a<b)parent[b]=a;
		else if(a>b) parent[a]=b;
	}
	
	public static void main(String[] args) throws IOException {
		int answer = 0;
		G = Integer.parseInt(br.readLine());
		P = Integer.parseInt(br.readLine());
		parent = new int[G+1];
		for(int i =1;i<=G;i++)parent[i]=i;//게이트초기화
		boolean shutdown = false;
		for(int i =0;i<P;i++) {
			int x = Integer.parseInt(br.readLine());
			int point = getParent(x);//게이트가 가리키는 방향
			if(point==0)shutdown=true;//공항폐쇄
			if(!shutdown) {//공항 아직 열려있다면
				union(point,point-1);
				answer++;
			}
		}
		System.out.println(answer);
	}
}