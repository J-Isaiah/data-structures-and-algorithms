

class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet <>();

        for (int x : nums){
            seen.add(x);
        }

return seen.size() != nums.length;
        
        
    }
}