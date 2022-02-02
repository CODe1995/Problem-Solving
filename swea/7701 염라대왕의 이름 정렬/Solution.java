package swea7701_염라대왕의이름정렬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Iterator;
import java.util.TreeSet;

public class Solution {
	static class Name implements Comparable<Name> {
		String name;

		public Name(String name) {
			this.name = name;
		}

		@Override
		public int compareTo(Name o) {
			if (name.length() == o.name.length()) {
				String str[] = new String[2];
				str[0] = name;
				str[1] = o.name;
				Arrays.sort(str);
				if (str[0].equals(name))
					return -1;
				else
					return 1;
			}
			return name.length() - o.name.length();
		}

		@Override
		public String toString() {
			return name;
		}
		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append("\n");
			int N = Integer.parseInt(br.readLine());
			ArrayList<Name> names = new ArrayList<>();
			HashSet<String> visited = new HashSet<>();
			
			for (int i = 0; i < N; i++) {
				Name name = new Name(br.readLine());
				if(visited.contains(name.name))
					continue;
				visited.add(name.name);
				names.add(name);				
			}
			Collections.sort(names);
			
			Iterator<Name> iter = names.iterator();
			while(iter.hasNext()) {
				Name name = iter.next();
				sb.append(name.name).append("\n");
			}
		}
		System.out.println(sb);
	}
}
