import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

added_dice = []

for i in range(0,1000):
    dice1  =random.randint(1,6)
    dice2  =random.randint(1,6)
    added_dice.append(dice1 + dice2)

mean = sum(added_dice)/len(added_dice)
mode = statistics.mode(added_dice)
median = statistics.median(added_dice)
standerd_devation = statistics.stdev(added_dice)

fig = ff.create_distplot([added_dice], ["Results"], show_hist = False)
fig.show()

print("Mean is", mean)
print("Mode is", mode)
print("Median is", median)
print("The devation is", standerd_devation)