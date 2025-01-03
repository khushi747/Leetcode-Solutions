class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int n=nums.size();
        long long sum=0;
        for (int &num: nums){
            sum=sum+num;
        }
        int split=0;
        long long leftsum=0;
        long long rightsum=0;
        for(int i=0;i<n-1;i++){
            leftsum+=nums[i];
            rightsum=sum-leftsum;
            if(leftsum>=rightsum){
                split++;
            }
        }
        return split;
    }
};