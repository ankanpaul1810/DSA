class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        HashSet<Integer>hs=new HashSet<>();
        int n=nums.length;
        int max=Integer.MIN_VALUE;
        int i=0,j=0;
        int sum=0;
        while(j<n){
            sum+=nums[j];
            while(i<=j&&hs.contains(nums[j])){
                sum-=nums[i];
                hs.remove(nums[i]);
                i++;
            }
            max=Math.max(max,sum);
            hs.add(nums[j]);
            j++;
        }
        return max;
    }
};