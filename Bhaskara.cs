
using System;

namespace AlgoritimoBhaskara
{
	class Program
	{
		public static void Main(string[] args)
		{
			var a = MathUtility.Bhaskara(0,0,0);
			var b = MathUtility.Bhaskara(0,0,6);
			var c = MathUtility.Bhaskara(0,2,6);
			var d = MathUtility.Bhaskara(1,1,-12);
			var e = MathUtility.Bhaskara(1,-4,4);
			var f = MathUtility.Bhaskara(1,0,1);
		}
	}
}

public static class MathUtility
{
	public static float[] Bhaskara(float a, float b, float c)
	{
		var roots = new float[0];
		
		if (a.CompareTo(0) == 0) {
			if (b.CompareTo(0) == 0) {
				if (c.CompareTo(0) == 0) {
					return roots;
				}
				return roots;
			}
			
			roots = new [] {
				-c / b
			};
			return roots;
		}
		
		var delta = Math.Pow(b,2) - (4 * a * c);
		
		// There are no real roots
		if (delta < 0)
			return roots;
		
		if (delta > 0) {
			// There are two distinct roots
			roots = new [] {
				(float)(-b - Math.Sqrt(delta)) / (2 * a),
				(float)(-b + Math.Sqrt(delta)) / (2 * a)
				
			};
			return roots;
		}
		
		// There is exactly one real root
		roots = new [] {
			-(b / (2 * a))
		};
		
		return roots;
	}
	
	public static float ClampBhaskara(float maxValue)
	{
		
		var clamped = 0f;
		
		if (roots.Length < 1)
			return roots[0];
		
		if (roots[0] > 0 && roots[1] > 0)
		{
			if (roots[0] > roots[1])
			{
				if (roots[0] < maxValue)
				{
					clamped = roots[0];
				}
			}
			else
			{
				if (roots[1] < maxValue)
				{
					clamped = roots[1];
				}
			}
		}
		
		return clamped;
	}
}