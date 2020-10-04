#Fit exponential curve to data
# x - x value
# a - y-intercept
# b	- gradient
# c	- y-asymptote
#Returns y value
def exponential(x, a, b, c):

	y = a * np.exp(-b * x) + c
	return y

#Fit curve
# guess - guess for exponential parameters
# xdata - x values
# ydata - y values
# spike - 0 - no spike, 1 - spike
#Returns coefficients, -1 if not found
def fit_curve(guess, xdata, ydata, spike):

	global R_SQUARED; global R_SQUARED_S;

	result = -1

	try:

		popt, pcov = curve_fit(exponential, xdata, ydata, guess)
		#print('DECAY', popt)

		#Calculate r squared
		residuals = ydata - exponential(xdata, popt[0], popt[1], popt[2])
		ss_res = np.sum(residuals**2)
		ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
		r_squared = 1 - (ss_res / ss_tot)
		R_SQUARED += r_squared

		if spike == 1:
			R_SQUARED_S += r_squared

		result = popt

	except RuntimeError as e:

		pass

	return result

#-------------------------------------

exp_guess = [[1,1,1], [-1,1,1], [-1,-1,1], [-1,-1,-1]]

popt = -1; def_pos = 0

while type(popt) == int:
	
	popt = fit_curve(exp_guess[def_pos], xdata, ydata, spike)
	def_pos += 1

	if def_pos == len(exp_guess):

		print('No exponential decay')

		pylab.plot(xdata, ydata, 'o', label='data')
		pylab.show()

		break

