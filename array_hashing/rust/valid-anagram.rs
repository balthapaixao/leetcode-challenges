impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut chars = [0; 26];
        for c in 0..s.len() {
            chars[s.as_bytes()[c] as usize - 97] += 1;
            chars[t.as_bytes()[c] as usize - 97] -= 1;
        }

        chars.iter().all(|c| *c == 0)
    }
}
