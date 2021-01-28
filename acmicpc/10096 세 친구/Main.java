package boj10096;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));	
	public static StringBuilder solve() throws NumberFormatException, IOException {
		StringBuilder sb = new StringBuilder();		
		int N = Integer.parseInt(bf.readLine());
		int i = 0;
		String U = bf.readLine();
		
		if(N%2==0)return sb.append("NOT POSSIBLE");
		
		int slen = N/2;
		for(i = 0; i<U.length();i++)
			if(U.charAt(0)!=U.charAt(i))break;
		if(i==U.length())return sb.append(U.substring(0, slen));
		if(U.substring(0,slen).equals(U.substring(slen,N))&&U.substring(1, slen+1).equals(U.substring(slen+1)))return sb.append("NOT UNIQUE");
		
		int right = slen+1;		
		for(i =0; i<slen;i++) {
			if(U.charAt(i)!=U.charAt(right+i))
				if(U.substring(i+1, right).equals(U.substring(right+i))) {return sb.append(U.substring(right));}
				else break;
		}
		if(i==slen)return sb.append(U.substring(0, slen));
		
		right = slen;
		for(i=0;i<slen;i++) {
			if(U.charAt(i)!=U.charAt(right+i))
				if(U.substring(i, slen).equals(U.substring(right+i+1)))return sb.append(U.substring(0, slen));
				else return sb.append("NOT POSSIBLE");
		}
		if(i==slen)return sb.append(U.substring(0, slen));
		return null;
	}
	public static void main(String[] args) throws IOException {
		while(true)
			System.out.println(solve());		
	}
}
