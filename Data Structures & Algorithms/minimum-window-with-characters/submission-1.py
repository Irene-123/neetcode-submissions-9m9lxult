class Solution:
	def minWindow(self, s: str, t: str) -> str:
		tmap = collections.defaultdict(int) 
		window = collections.defaultdict(int)

		for tc in t:
			tmap[tc]+=1

		have, need = 0, len(tmap)
		res, i = float('inf'), 0
		res_indexes = [-1, -1]

		for j in range(len(s)):
			c = s[j]
			window[c] += 1

			if c in tmap and tmap[c] == window[c]:
				have+= 1
			
			while have == need:
				if j - i + 1 < res:
					res = j - i + 1
					res_indexes = [i, j]

				window[s[i]] -= 1

				if s[i] in tmap and window[s[i]] < tmap[s[i]]:
					have -= 1
				i += 1

		if res_indexes[0] == -1:
			return ""
		return s[res_indexes[0]: res_indexes[1]+1]

				

