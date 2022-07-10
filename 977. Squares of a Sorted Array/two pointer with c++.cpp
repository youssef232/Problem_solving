# include <iostream>
# include <vector>
using namespace std;

int main(){
    cout<<"molNa";

}
vector<int> sortedSquares(vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    vector<int> answer;
    answer.assign(0, nums.size())
    for (int i =nums.size() -1 ; i <=0 ; i--)
    {
        if(abs(nums[left]) > abs(nums[right])){
            answer[i] = nums[left] * nums[left];
            left++;
        }else{
            answer[i] = nums[right] * nums[right];
            right--;
        }
    }
    
    return answer;
}