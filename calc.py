#!/usr/bin/env python3
import numpy as np
import os
NULL = ''
version = 0.2
action = True

if __name__ == '__main__':
	os.system("clear")
	print("\t\t\tWelcome to Chiken Calc\t\t\t")
	print("Version: ", version)
	print("Autor: Denis Mustafin")
	print("GitHub url: https://github.com/DenisCompany/CaclPy/edit/master/calc.py\n\n\n")
	print("For cancel to press on 'ctrl' + 'c'")
	action = True
	while True:
		# Обработка ввода 
		try :
			first_num = float(input("Please input first number ->"))
			second_num = float(input("Please input second number ->"))
			sing = input("This's calculat supports the following action ->\n +, -,*, /, mod, div, pow, gcd, lcm\n")
		except KeyboardInterrupt:
			# os.system("clear")
			print("\n")
			break
		except ValueError: 
			print("Repeat your entry again")
			continue
		# Произведение операции
		try :
			if (sing != 'gcd' and sing != 'lcm' ): 
				act = ("first_num " + sing + " second_num").replace("mod", "%").replace("div", "//").replace("pow", "**")
				if ("%" in act or "//" in act or "/" in act) and act == 0.0: print("Деление на 0!")
			if   sing=="gcd": 
				print(np.gcd(int(first_num), int(second_num))); continue 
			elif sing=="lcm": print(np.lcm(int(first_num), int(second_num))); continue 
			else: print(eval(eval("act")))	
		except SyntaxError:
			print("Maybe you didn't write the action correctly or you did choose function, what haven't in menu\nPlease again")
