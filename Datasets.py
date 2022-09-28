import pandas as pd
import statistics as st
x = pd.read_csv(r'C:\Users\nexus\.conda\envs\pyenv_1\Lib\site-packages\statsmodels\datasets\sunspots\sunspots.csv')
print(x)

mean = x['Sun Activity'].mean()
mean_str = "The mean value of sunspots activity is: "

median = x['Sun Activity'].median()
median_str = "The median of the sunspot activity is: "

mode = x['Sun Activity']
mode_str = "The mode of the sunspot activity is: "

standard_deviation = x['Sun Activity']
standard_deviation_str = "The standard deviation of the sunspot activity is: "

varience = x['Sun Activity']
varience_str = "The variation of the sunspot activity is: "

max_value = x['Sun Activity'].max()
min_value = x['Sun Activity'].min()
range_str = "The range of the sunspot activity is: "
range = max_value - min_value

Dup_Rows = x[x.duplicated()]

print(f"{mean_str}{str(mean)}")
print(f"{median_str}{str(median)}")
print(f"{mode_str}{st.mode(mode)}")
print(f"{standard_deviation_str}{str(st.stdev(standard_deviation))}")
print(f"{varience_str}{str(st.variance(varience))}")
print(f"{range_str}{range}")
print("\nDuplicate Rows : \n {}".format(Dup_Rows))
