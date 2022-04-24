using System;
namespace MyApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            uint n = 00000000000000000000000000001111;
            Console.WriteLine(HammingWeight(n));
        }
        public static uint HammingWeight(uint n)
        {
            uint ones = 0;
            //for (int i = 0; i < 32; ++i)
            //{
            //    if (((n >> i )&1)== 1)
            //    {
            //        ones++;
            //    }
            //}
            while(n != 0)
            {
                ones += (n & 1);
                n >>= 1;

            }
            return ones;
        }
    }
}