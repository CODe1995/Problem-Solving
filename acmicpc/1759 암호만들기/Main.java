package boj1759;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int L,C;
	static char[] arr;
	static char vowel[] = new char[] {'a','e','i','o','u'};
	static boolean checked[];
	static ArrayList<char[]> answer = new ArrayList<>();
	static boolean checkVowel(char x) {//모음인지 판단
		for(int i =0;i<5;i++) {
			if(x == vowel[i])return true;
		}
		return false;
	}
	static void dfs(int depth,int index,int moum, int jaum) {
		if(depth==L) {
			if(moum>=1 && jaum>=2) {
				char[] tmp = new char[L];
				int size=0;
				for(int i =0;i<C;i++) {
					if(checked[i])
						tmp[size++] = arr[i];
				}
				answer.add(tmp);
			}
			return;
		}
		for(int i = index;i<C;i++) {
			if(checked[i])continue;
			checked[i]=true;
			int cv = checkVowel(arr[i])?1:0;			
			dfs(depth+1,i+1,moum+cv,jaum+1-cv);			
			checked[i]=false;			
		}
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		arr = new char[C];	
		checked = new boolean[C];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<C;i++)
			arr[i] = st.nextToken().charAt(0);
		Arrays.sort(arr);
		dfs(0,0,0,0);
		for(int i =0;i<answer.size();i++)
			System.out.println(answer.get(i));		
	}
}