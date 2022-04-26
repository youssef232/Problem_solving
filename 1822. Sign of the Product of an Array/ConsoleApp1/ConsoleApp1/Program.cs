using System;
namespace MyApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] nums = {9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24};
            Console.WriteLine(arraySign(nums));
        }

        public static int arraySign(int[] nums)
        {
            int product = 1;
            foreach (int num in nums)
            {
                if (num == 0)
                    return 0;
                if (num < 0)
                    product *= -1;

            }
            return product;
        }
    }
}