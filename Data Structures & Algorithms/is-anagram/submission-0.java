class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freq = new int[26];

        for (var c : s.toCharArray())
            freq[c - 'a']++;

        for (var c : t.toCharArray())
            freq[c - 'a']--;

        for (var x : freq) {
            if (x != 0)
                return false;
        }

        return true;
    }
}