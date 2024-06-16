from typing import *;
from fact import fact;



def tailor_dynamic(order:int ,y:float, x:float, step_legnth:float, functions:List[Callable[[float], float]])->float:
	assert functions.__len__() == order, f"tailor was called by order {order} but {functions.__len__()} function(s) were given!";
	h:float = step_legnth;
	sum:flaot = 0;
	sum += y;
	for k in range(0,order):
		current_f:Callable[[float], float] = functions[k];
		sum	+= ((h**(k+1))/fact(k+1)) * current_f(x,y);
	return sum;


def tailor_3rd(y:float, x:float, step_legnth:float, f:Callable[[float, float], float], f_:Callable[[float, float], float],f__:Callable[[float, float], float])->float:
	h = step_legnth;
	sum:float=0;
	sum = y;

	sum += h * f(x,y);
	sum += (h**2/2) * f_(x,y);
	sum += (h**3/6) * f__(x,y);

	return sum;


def tailor_2nd(y:float, x:float, step_legnth:float, f:Callable[[float, float], float], f_:Callable[[float, float], float])->float:
	h = step_legnth;
	sum:float=0;
	sum = y;
	sum += h * f(x,y);
	sum += (h**2/2) * f_(x,y);

	return sum;





def test_1():
	order = 2;
	y = 3.6213;
	x = 0.8;
	step_legnth = 0.2;

	def f(x, y):
		return 1+(x**2)+y;


	def f_(x,y):
		return 2*x + 1 + x**2 + y; 

	functions = [f, f_];


if __name__ == "__main__":
	test_1();


