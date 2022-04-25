using System;
namespace MyApp
{
    internal class Program
    {
        public static void Main(String [] arg)
        {
            int [] nums = { 1, 2, 3 , 5, 6 ,7};
            Console.WriteLine(maxPermiter(nums));
        }
        public static int maxPermiter(int [] nums)
        {
            Array.Sort(nums);
            Array.Reverse(nums);
            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i]< nums[i +1] + nums[i +2])
                {
                    return nums[i] + nums[i + 1] + nums[i + 2];
                }
            }
            return 0;
        }
    }
}