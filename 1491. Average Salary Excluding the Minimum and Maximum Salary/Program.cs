using System;

namespace MyApp
{
    internal class Program
    {
        public static void  Main(string[] args)

        {
            int[] arr = { 4000, 3000, 1000, 2000 };
            Console.WriteLine(Average(arr));
        }
        public static double Average(int[] salary)
        {

            int sum = 0;
            int minimum = salary[0];
            int maximum = salary[0];
            for (int i = 0; i < salary.Length; i++)
            {
                if (salary[i] < minimum)
                {
                    minimum = salary[i];
                }else if(salary[i] > maximum)
                {
                    maximum = salary[i];
                }
                sum += salary[i];
            }
            return (sum - minimum - maximum)/(salary.Length - 2) ;
        }
    }
}