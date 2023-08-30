object Solution {
    import scala.collection.mutable._

    def groupAnagrams(strs: Array[String]): List[List[String]] = {
        val map = new HashMap[String, ListBuffer[String]]()

        for (word <- strs) {
            val sortedWord = word.sorted

            if (!map.contains(sortedWord)) {
                map(sortedWord) = new ListBuffer[String]()
            }

            map(sortedWord).append(word)
        }

        map.values.map(_.toList).toList 
    }
}