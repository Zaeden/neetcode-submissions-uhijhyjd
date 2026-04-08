class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn = len(s)
        tn = len(t)

        if sn != tn:
            return False

        count_s = {}
        for character in s:
            if character not in count_s:
                count_s[character] = 1
            else:
                count_s[character] = count_s[character] + 1

        count_t = {}
        for character in t:
            if character not in count_t:
                count_t[character] = 1
            else:
                count_t[character] = count_t[character] + 1

        # print(count_s, count_t)

        for character in count_s:
            if character not in count_t or count_s[character] != count_t[character]:
                return False
        
        return True

