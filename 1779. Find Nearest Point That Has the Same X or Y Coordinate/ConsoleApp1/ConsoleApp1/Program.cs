using System;
namespace MyApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {

        }
        public static int NearestValidPoint(int x, int y, int[][] points)
        {
            int index = -1;
            int small_distance = int.MaxValue;
            for (int i = 0; i < points.Length; i++)
            {
                if (points[i][0] == x || points[i][1] == y)
                {
                    if (small_distance > Math.Abs(x - points[i][0]) + Math.Abs(y - points[i][1]))
                    {
                        index = i;
                        small_distance = Math.Abs(x - points[i][0]) + Math.Abs(y - points[i][1]);
                    }
                    
                }
            }
            return index;
        }
    }
}