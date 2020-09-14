import os
import math
import platform

def eval(a, b, c):
    roots = [0]
		
		if (a == 0) 
			if (b == 0) 
				if (c == 0) 
					return roots
				
				return roots
			
			
			roots = new [] 
				-c / b
			
			return roots
		
		var delta = Math.Pow(b,2) - (4 * a * c)
		
		""" There are no real roots """
		if (delta < 0)
			return roots
		
		if (delta > 0) 
			""" There are two distinct roots """
			roots = new [] 
				(float)(-b - Math.Sqrt(delta)) / (2 * a),
				(float)(-b + Math.Sqrt(delta)) / (2 * a)
				
			
			return roots;
		
		
		""" There is exactly one real root """
		roots = new [] 
			-(b / (2 * a))
		
		
		return roots

def eval_clamped()
    clamped = 0;
		
		if (roots.Length < 1)
			return roots[0]
		
		if (roots[0] > 0 and roots[1] > 0)
		
			if (roots[0] > roots[1])
			
				if (roots[0] < maxValue)
				
					clamped = roots[0]
				
			
			else
			
				if (roots[1] < maxValue)
				
					clamped = roots[1]
				
			
		
		
		return clamped
