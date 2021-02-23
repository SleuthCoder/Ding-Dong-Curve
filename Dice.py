import plotly.figure_factory as ff
import random
dice_result = []
for i in range(0,100):

    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    dice_result.append(Dice1+Dice2)
    
fig = ff.create_distplot([dice_result], ["Result"])
fig.show()
