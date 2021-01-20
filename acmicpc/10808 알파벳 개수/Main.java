package boj10808;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int[] arr = new int[26];
		for(int i = 0 ; i<s.length();i++)
			arr[(int)s.charAt(i)-97]++;
		for(int x:arr)
			System.out.print(x+" ");
		sc.close();
	}
}
