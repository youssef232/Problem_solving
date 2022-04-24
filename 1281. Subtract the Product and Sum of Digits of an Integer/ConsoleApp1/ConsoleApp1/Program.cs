using System;
namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(SubtractProductAndSum(22));
        }
        public static int SubtractProductAndSum(int n)
        {
            int sum = 0;
            int product = 1;
            while(n != 0)
            {
                int digit = n % 10;
                sum += digit;
                product *= digit;
                n = n / 10;
            }
            return product - sum;

        }
    }
}