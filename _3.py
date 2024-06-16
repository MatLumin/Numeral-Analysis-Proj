from typing import *;
from floating_point_error_fixer import cut_floating_point_to_precision;



def calc_k1(h, x, y, f, k0):
	return h * f(x,y); 


def calc_k2(h, x, y, f, k1):
	h_div_2 = h/2;
	k1_div_2 = k1/2;
	return h * f(x+h_div_2,y+k1_div_2);


def calc_k3(h, x, y, f, k2):
	h_div_2 = h/2;
	k2_div_1 = k2/2;
	return h * f(x+h_div_2, y+k2_div_1);


def calc_k4(h, x, y, f, k3):
	return h*f(x+h, y+k3)


def dpg(n, h, previous_y, previous_x, current_x, current_y, k1, k2, k3, k4):
	msg:str=f"""
=====================
n={n}
h={h}
previous_y={previous_y}
previous_x={previous_x}
k1={k1}
k2={k2}
k3={k3}
k4={k4}
current_x={current_x}
current_y={current_y}

	""";
	print(msg);



def runge_kutta_4th(target_x:float, y:float, x:float, h:float, f:Callable[[float, float], float])->float:
	n:int = 1;
	current_x:float=0.0;
	current_y:float=0.0;
	previous_x:float =x;
	previous_y:float =y;
	while True:
		current_x = x + (h * n);

		k1:float = calc_k1(h, previous_x, previous_y, f, 1);
		k2:float = calc_k2(h, previous_x, previous_y, f, k1);
		k3:float = calc_k3(h, previous_x, previous_y, f, k2);
		k4:float = calc_k4(h, previous_x, previous_y, f, k3);


		current_y += previous_y;
		current_y += (1/6) * sum([k1,2*k2,2*k3,k4]);
		current_y = cut_floating_point_to_precision(current_y);


		dpg(n, h, previous_y, previous_x, current_x, current_y, k1, k2, k3, k4);
		if (current_x >= target_x):
			print(f"found the f({target_x}) = {current_y}");
			return current_y;


		previous_x = current_x;
		privious_y = current_y;
		n += 1;


if __name__ == "__main__":
	runge_kutta_4th(
		target_x=0.1,
		y=1,
		x=0,
		h=0.1,
		f=lambda y,x : x+y
		)