class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> s= new HashSet<Integer>();

        for (int i : nums){
            s.add(i);
        }

        if (nums.length == s.size()){return false;}
        return true;
    }
}