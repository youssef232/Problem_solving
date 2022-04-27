using System;
namespace MyApp
{
    internal class Program
    {
        public static void Main(string[] arg)
        {
            Console.WriteLine(IsHappy(119));
        }
        public static bool IsHappy(int n)
        {
            ISet<int> set = new HashSet<int>();
            while (n != 1 && !set.Contains(n))
            {
                set.Add(n);
                n = sum_of_square_of_number_digit(n);
            }
            return n == 1;
        }
        public static int sum_of_square_of_number_digit(int num)
        {
            int total_sum = 0;
            int reminder = 0;
            while (num > 0)
            {
                num = Math.DivRem(num, 10, out reminder);
                total_sum += (int) Math.Pow(reminder, 2);
            }
            return total_sum;
        }
    }
}