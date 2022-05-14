# include<iostream>
# include <vector>
using namespace std;

int search(vector<int>, int);
int main(){

    vector <int> nums;
    nums.push_back(10);
    nums.push_back(20);
    nums.push_back(30);
    nums.push_back(40);
    cout<< search(nums, 30);
    return 0;
}

    int search(vector<int>& nums, int target) {
            int start = 0;
            int end = nums.size();
            int middle;

            while (start <= end)
            {
                middle = int((start + end) / 2);
                if (nums[middle] == target)
                {
                    return middle;
                }else if (nums[middle] > target)
                {
                    end = middle - 1;
                }else{  
                    start = middle + 1;
                }             
                
            }
            return -1;
            

    }