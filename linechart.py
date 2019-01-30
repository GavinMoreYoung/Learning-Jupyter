import pandas
import matplotlib.pyplot as plt
baby_name = ['Alice','Charles','Diane','Edward']
number_births = [96, 155, 66, 272]
dataset = list(zip(baby_name,number_births))
df = pandas.DataFrame(data = dataset, columns=['Name', 'Number'])
df['Number'].plot()
plt.show()
