
#Linear Regression Program
#Sharandeep Singh


import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
import math

data = pd.read_csv("sale_analysis.csv")

x = data.iloc[:,0].values  #Footfalls - Independent variable
y = data.iloc[:,1].values  #Sales - Dependent variable 

n=30
mean_x = np.mean(x)
mean_y = np.mean(y)
sum_x = np.sum(x)
sum_y = np.sum(y)

#since y = b1*x + b0
#implies b0 = y - b1*x
print("\n\t\tLinear Regression Program\n")



def regression_coefficient_b1():
    sum_meanxy =0
    sum_meanxsquared = 0
    for i in range(n):
        sum_meanxy+=((x[i]-mean_x)*(y[i]-mean_y))
        sum_meanxsquared+=((x[i]-mean_x)*(x[i]-mean_x))

    #now for b1
    b1 = sum_meanxy/sum_meanxsquared
    return b1
b1 = regression_coefficient_b1()
print(f"\tThe value of Regression Coefficient B1 is: {b1}\n")


def regression_coefficient_b0(): 
    b0 = (1/n)*(sum_y - b1*sum_x)
    return b0
b0 = regression_coefficient_b0()
print(f"\tThe value of Regression Coefficient B0 is {b0}\n")



def plotting_fit_line():
    plot.scatter(x, y, color='r', marker='o', label='Plot of Engine Capacity (in cc)(100-150) by Engine Performance (1-5)', s=30)
    predicted_y = b1*x + b0
    
    # plot.scatter(x2, y2, color='g',marker='o', label="Plot of Cubic Capacity (in cc)(130-200) by Engine Performance(3-10)", s=30)
    plot.plot(x, predicted_y, color='b', label='Regression line')
    plot.xlabel('Cubic Capacity (in cc)')
    plot.ylabel('Engine Performance (1-10)')
    plot.legend()
    plot.show()

plotting_fit_line()



def finding_sst():
    sst = 0

    for i in range(n):
        sst +=((y[i]-mean_y)*(y[i]-mean_y))
           
    return sst

sum_squares_total = finding_sst()
print(f"-\tThe Sum of Squares Total is : {sum_squares_total}\n")



def finding_ssr():
    predicted_y = []
    predicted_y= b1*x + b0
    
    ssr = 0

    for i in range(n):
        ssr +=((predicted_y[i]-mean_y)*(predicted_y[i]-mean_y))

    return ssr

sum_square_residual = finding_ssr()
print(f"-\tThe Sum of Squares of Residuals is : {sum_square_residual}\n")




def finding_sse():
    sse = 0
    predicted_y = b1*x + b0

    for i in range(n):
        sse += ((y[i]-predicted_y[i])*(y[i]-predicted_y[i]))
        
    return sse

sum_squares_error = finding_sse()
print(f"-\tThe Sum of Squares error is : {sum_squares_error}\n")




def finding_r_squared():
    r  = sum_square_residual/sum_squares_total
    return r

def finding_karl_pearsons():
    product_xy=0
    sum_squaredx = 0
    sum_squaredy = 0
    for i in range(n):
        sum_squaredx += x[i]*x[i]
        sum_squaredy += y[i]*y[i]
        product_xy += x[i]*y[i]
    
    kp = (n*product_xy - (sum_x*sum_y))/(math.sqrt((n*sum_squaredx - (sum_x*sum_x)))*(math.sqrt((n*sum_squaredy - (sum_y*sum_y)))))
    return kp
kp = finding_karl_pearsons()

R_squared = finding_r_squared()
print(f"-\tThe Value of R^2 (r-squared) is : {R_squared}")
print(f"\n-\tThe value of Karl Pearson's Coefficient = {kp}")


def finding_see():
    see = math.sqrt(sum_squares_error/n-2)
    return see
see = finding_see()
print(f"\n-\tThe Value of Standard Error of estimates: {see}")
print("\n\n\n\t\t-----------****** ********** *******-----------\n\n")
