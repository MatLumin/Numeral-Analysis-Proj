from decimal import *;
from typing import *;


PRECISION:Final[int] = 4;



def cut_floating_point_to_precision(value:float, precision=PRECISION)->float:
	string_form:str = str(value);
	dot_index:int = string_form.find(".");
	return eval(string_form[0:dot_index+1+precision]);