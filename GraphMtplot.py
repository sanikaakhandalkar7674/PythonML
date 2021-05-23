###3d plot
###pie chart
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

plt.show()




#Bar graph
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["DS", "SW ENGG", "DigitalMarketing", "CyberSecurity"])
y = np.array([250000, 100000, 150000, 300000])

plt.bar(x, y, color = "red")
plt.show()



###pie chart
import matplotlib.pyplot as plt

# Data to plot
labels = 'Death', 'Recovery', 'Symtommatic', 'Asymtomatic'
numbers = [100, 250, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(numbers, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()



####scatter
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()



####histogram
import matplotlib.pyplot as plt

age_villagers = [20,39,45,60,
                 23,25,28,30,
                 45,40,35,48,
                 50,55,57,60,
                 3,5,6,9,10,
                 15,12,18,19]


plt.style.use('ggplot')
plt.hist(age_villagers, bins=10)
plt.show()




import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1

plt.figure(num = 3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1,
         color='red',
         linewidth=1.0,
         linestyle='--'
        )

plt.show()