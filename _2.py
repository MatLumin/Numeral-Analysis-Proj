from typing import *;
from floating_point_error_fixer import cut_floating_point_to_precision;



def dbgp_1(n, current_x, current_y, privious_x, privious_y):
	msg:str = f"""
n={n}
current_x={current_x}
current_y={current_y}
privious_x={privious_x}
privious_y={privious_y}
	""";
	print(msg);





def eular_function(y:float, x:float, h:float, f:Callable[[float, float], float])->float:
	return y + h * f(x, y);


def solve_by_eular(target_x:float, x:float, y:float, h:float, f:Callable[[float, float], float])->float:
	n:int = 1;
	privious_x = x; # a typo :]
	privious_y = y;
	while True:
		print("-----")
		print("")
		current_x = cut_floating_point_to_precision(privious_x + (n * h));
		current_y = cut_floating_point_to_precision(privious_y + h * f(privious_x,privious_y));
		dbgp_1(n, current_x,current_y,privious_x,privious_y,);
		if current_x >= target_x:
			output:float = current_y;
			output= cut_floating_point_to_precision(output);
			print(f"reached above or equal of target_x  = {target_x}");
			print(f"f({target_x})={current_y}")
			return output;
			

		privious_x = current_x;
		privious_y = current_y;

		n += 1;



if __name__ == "__main__":

	def f(x,y):return (x+y)**(0.5)
	print(solve_by_eular(2.1, 0.2, 1.24, 0.1, f));