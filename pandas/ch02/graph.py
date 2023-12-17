from TestData import TestData
import matplotlib.pyplot as plt

df = TestData.getData()

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
plt.show()