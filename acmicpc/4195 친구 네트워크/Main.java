package boj4195;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M;
	static HashMap<String, String> parent;
	static HashMap<String, Integer> parentCnt;
	static String getParent(String x) {
		if(x.contains(parent.get(x)))return x;
		parent.put(x, getParent(parent.get(x)));
		return parent.get(x);
	}
	static void union(String a,String b) {
		if(!parent.containsKey(a)) {
			parent.put(a, a);
			parentCnt.put(a, 1);
		}
		if(!parent.containsKey(b)) {
			parent.put(b, b);	
			parentCnt.put(b, 1);		
		}
		a = getParent(a);
		b = getParent(b);		
		//compareToIgnoreCase -> 대소 무시
		int comp = a.compareToIgnoreCase(b);
		if(comp<0) {
			parent.put(b, a);
			parentCnt.put(a, parentCnt.get(b)+parentCnt.get(a));
		}
		else if(comp>0) {
			parent.put(a, b);
			parentCnt.put(b,parentCnt.get(a)+parentCnt.get(b));
		}
		
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		for(int i =0;i<N;i++) {
			parent = new HashMap<>();	
			parentCnt = new HashMap<>();
			M = Integer.parseInt(br.readLine());
			for(int j =0;j<M;j++) {
				st = new StringTokenizer(br.readLine());
				String a = st.nextToken();
				String b = st.nextToken();
				union(a,b);
				System.out.println(parentCnt.get(getParent(a)));
			}			
		}
	}
}