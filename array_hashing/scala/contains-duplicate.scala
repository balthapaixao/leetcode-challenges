import scala.collection.mutable.HashSet

object Solution {
  def containsDuplicate(nums: Array[Int]): Boolean = {
    val seen = new HashSet[Int]() 
    !nums.find(num => !seen.add(num)).isEmpty
  }
}
