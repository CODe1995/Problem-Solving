package boj2217;

import java.util.Arrays;
import java.util.Scanner;

public class Main {	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] arr = new int[n];
		for(int i = 0 ; i<n;i++)
			arr[i]=scan.nextInt();
		Arrays.sort(arr, 0,n);
		for(int i = n-1;i>=0;i--) {
			arr[i] = arr[i]*(n-i);
		}
		Arrays.sort(arr, 0,n);
		System.out.println(arr[n-1]);
	}
}
