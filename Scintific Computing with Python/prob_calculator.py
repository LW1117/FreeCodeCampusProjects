import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.items = kwargs
    self.contents = []
    for item, count in self.items.items():
       self.contents.extend([item] * count)
    
  # Function to choose balls from existing list of balls 
  def draw(self, no_of_balls):
    drwan_balls = random.sample(self.contents, min(no_of_balls, len(self.contents)))
    for ball in drwan_balls:
      self.contents.remove(ball)
    return drwan_balls

# Function to to run experiments n times to check probablity 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for _x in range(num_experiments):
    temp_hat = copy.deepcopy(hat)
    drawned_balls = temp_hat.draw(num_balls_drawn)
    flag = True
    for ball, index in expected_balls.items():
      if drawned_balls.count(ball) < index:
        flag = False
        break
    if flag:
      count += 1
  probablity = count  / num_experiments
  return probablity

    
hat = Hat(black=6, red=4, green=3)
print(hat.contents)
print(hat.draw(5))
# probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)