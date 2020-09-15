import numpy as np
import matplotlib.pyplot as plt
import cmath
import streamlit as st

def quadratic_eq(coeff_a, coeff_b, coeff_c, start_x, end_x, num_steps):

	a = coeff_a
	b = coeff_b
	c = coeff_c

	x = np.linspace(start_x, end_x, num_steps)

	#print(x)



	y = a*x**2 + b*x + c


	#print(y)


	fig, ax = plt.subplots()
	plt.title("Quadratic equation")
	st.markdown("by Rohini Das")
	plt.xlabel("X")

	plt.ylabel("Y")


	plt.plot([start_x, end_x], [0, 0], '--', label='x axis') #x axis

	margin = 5

	min_y = min(y)
	max_y = max(y)

	if max_y < 0 :
		max_y = 0 

	if min_y > 0 :
		min_y = 0

	plt.plot([0, 0], [min_y - margin, max_y + margin],'--', label='y axis') #y axis

	if a != 0.0 : #axis of symmetry 
		plt.plot([-b/(2.0*a), -b/(2.0*a)], [min(y), max(y)], ':', label='axis of symmetry')
		#print(-b/2.0*a)

	ax.plot(x, y, label='equation') #plotting the equation

	ax.legend()










	solution1 = 0
	solution2 = 0
	solution_exists = 0


	delta = (b**2) - (4*a*c)

	if delta > 0 and a != 0.0 :
		solution1 = (-b - cmath.sqrt(delta))/(2*a) 
		solution2 = (-b + cmath.sqrt(delta))/(2*a)
		solution_exists = 1
	else :
		solution_exists = 0 



		#print(solution1)
		#print(solution2)
    	
	return fig, solution1, solution2, solution_exists

if __name__ == '__main__':
 
 	st.title("Quadratic equation")
 	st.markdown("Plot the quadratic equation from the given below axis for the following equation:")
 	st.markdown("ax^2 + b*x + c")

 	st.sidebar.markdown("Controls")


 	coeff_a = st.sidebar.number_input("Insert coeff_a", value=1.0, step= 1.0)
 	coeff_b = st.sidebar.number_input("Insert coeff_b", value=2.0, step= 1.0)
 	coeff_c = st.sidebar.number_input("Insert coeff_c", value=4.0, step= 1.0)
 	start_x = st.sidebar.number_input('Insert a starting range', value=-10, step= 10) 
 	end_x = st.sidebar.number_input('Insert a end range', value=10, step= 10)
 	#num_steps = st.sidebar.number_input('No. of points', value=10, step= 10, min_value= 3)
 	num_steps = st.sidebar.slider('No. of points', min_value=10, max_value= 100, value=10, step=10)

 	





 	fig, solution1, solution2, solution_exists = quadratic_eq(coeff_a, coeff_b, coeff_c, start_x, end_x, num_steps)



 	st.pyplot()

 	st.markdown("**Solutions:**")
 	#print(solution1)
 	#print(solution2)
 	if solution_exists == 1 :

 		md_results1 = f"**{solution1:.2f}** "
 		md_results2 = f"**{solution2:.2f}** "

 		st.markdown(md_results1)
 		st.markdown(md_results2)

 	else :

 		st.markdown("Real valued Solutions do not exist!")
