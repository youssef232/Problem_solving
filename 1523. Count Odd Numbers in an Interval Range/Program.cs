using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int low = 10;
            int high = 20;
            Console.WriteLine( countOdds(low,high));
        }

        public static int countOdds(int low, int high)
        {
            if((low % 2 == 0 && high % 2 ==0) || (low % 2 == 0 && high % 2 == 1))
            {
                return assistMethod(high) - assistMethod(low);
            }
            else { return assistMethod(high) - assistMethod(low) + 1; }
        }

        public static int assistMethod(int num)
        {
            if (num % 2 == 0)
                return (int)(num / 2);
            else
            {
                return (int)(num / 2) + 1;
            }
        }
    }
    
}