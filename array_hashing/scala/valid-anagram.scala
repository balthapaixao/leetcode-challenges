object Solution {
    def isAnagram(s: String, t: String): Boolean = {
        if (s.length != t.length) {
            return false
        } 

        val charsCount = Array.fill(26)(0)

        val toIdx = (_: Char) - 'a'

        for (c <- s) {
            charsCount(toIdx(c)) += 1
        }

        for (c <- t) {
            charsCount(toIdx(c)) -= 1
        }

        charsCount.forall(_ == 0)
    }
}