package longestPalindrome

func longestPalindrome(s string) string {
	res := ""
	resLen, l, r := 0, 0, 0

	for i := 0; i < len(s); i++ {
		l, r = i, i
		// equivalent to a while loop
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if (r - l + 1) > resLen {
				res = s[l : r+1]
				resLen = r - l + 1
			}
			r += 1
			l -= 1
		}

		l, r = i, i+1
		// equivalent to a while loop
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if (r - l + 1) > resLen {
				res = s[l : r+1]
				resLen = r - l + 1
			}
			r += 1
			l -= 1
		}
	}
	return res
}
