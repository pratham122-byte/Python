
import numpy as np
morning_temps=np.array([23,25,21,22,24,26,27])
evening_temps=np.array([30,28,29,31,27,26,25])
temp_diff=evening_temps - morning_temps
day_with_max_diff=np.argmax(temp_diff)
print("day with maximum temperature variation is day",day_with_max_diff + 1)