###########################
#
# Ant System (AS) for TSP
#
###########################

import math
import numpy as np
import matplotlib.pyplot as plt
import random
from city_data import city_locations
number_of_cities = len(city_locations)

###############################################################
## To do: Write the initialize_pheromone_levels function:
###############################################################

def initialize_pheromone_levels(number_of_cities, tau_0):
    initialize_pheromones = [[tau_0 for i in range(number_of_cities)] for j in range(number_of_cities)]
    return initialize_pheromones


###############################################################
## To do: Write the get_visibility function:
###############################################################

def get_visibility(city_locations):
   visibility_matrix = []
   for city_i in city_locations:
      row = []
      for city_j in city_locations:
          x1_ij = (city_i[0] - city_j[0])
          x2_ij = (city_i[1] - city_j[1])
          d_ij = np.sqrt((x1_ij)**2 + (x2_ij)**2)
          if d_ij == 0:
              eta_ij = 0
          else:
            eta_ij = float(1 / d_ij)
          row.append(eta_ij)
      visibility_matrix.append(row)
   return visibility_matrix



# #################################################################
# ## To do: Write the generate_path function (Note: You may wish
# ##       to add more functions, e.g., get_node. That is allowed).
# #################################################################
def get_node(index, city_data):
   return city_data[index]


def generate_path(pheromone_levels, visibility, alpha, beta):

    number_of_cities = len(pheromone_levels)
    random_start_city = np.random.randint(0,number_of_cities)
    visited_cities = [random_start_city]
    if len(visited_cities) < number_of_cities:
      while len(visited_cities) < number_of_cities:
        nominators = []
        current_city = visited_cities[-1]
        list_of_possible_cities = [i for i in range(number_of_cities) if i not in visited_cities]
        for index in list_of_possible_cities:
            if len(list_of_possible_cities) > 1:
              tau = pheromone_levels[current_city][index] 
              eta = visibility[current_city][index]
              nominator = tau**alpha * eta**beta
              nominators.append(nominator)
            else:
              nominators.append(1)
        
        denominator = sum(nominators)
        if denominator == 0:
          probabilities = [1/len(nominators) for i in range(len(nominators))]
        else:
          probabilities = [(tau_eta/denominator) for tau_eta in nominators]

        

        next_city = np.random.choice(list_of_possible_cities,p=probabilities)
        visited_cities.append(int(next_city))

    return visited_cities
       

# # # Add code here!

# ###############################################################
# ## To do: Write the get_path_length function:
# ###############################################################

def get_path_length(path, city_locations):
    path_length = 0
    i = len(path)-1
    while i >= 0:
        current_city = city_locations[path[i]]
        next_city = city_locations[path[i-1]]
        x1_ij = (current_city[0] - next_city[0])
        x2_ij = (current_city[1] - next_city[1])
        d_ij = np.sqrt((x1_ij)**2 + (x2_ij)**2)
        path_length += d_ij
        i -= 1
    return path_length        

# # Add code here!

# # ###############################################################
# # ## To do: Write the compute_delta_pheromone_levels function:
# # ###############################################################

def compute_delta_pheromone_levels(path_collection, path_length_collection):
   n = len(path_collection[0])
   delta_tau = np.zeros((n,n))
   for length,path in zip(path_length_collection,path_collection):
        for i in range(0,len(path)):
          delta_tau[path[i]][path[(i+1) % len(path)]] += 1/length
    # print(delta_tau)
   return delta_tau
    

# # # Add code here!

# # # ###############################################################
# # # ## To do: Write the update_pheromone_levels function:
# # # ###############################################################

def update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho):
    pheromone_levels = (1-rho)*np.array(pheromone_levels) + delta_pheromone_levels
    return pheromone_levels
# # Add code here!

# # ##################################################
# # #  Plots the cities (nodes):
# # ##################################################

def plot_cities(plt, city_locations):
  x = []
  y = []
  for city_index in range(len(city_locations)):
    x.append(city_locations[city_index][0])
    y.append(city_locations[city_index][1])
  plt.scatter(x,y,zorder=1,color='red')

def plot_path(plt, path):

  connections_x = []
  connections_y = []
  for index in path:
    location_x = city_locations[index][0]
    connections_x.append(location_x)
    location_y = city_locations[index][1]
    connections_y.append(location_y)
  start_location_x = city_locations[path[0]][0]
  start_location_y = city_locations[path[0]][1]
  connections_x.append(start_location_x)
  connections_y.append(start_location_y)
  plt.plot(connections_x,connections_y,color='blue',zorder=0)

# # #####################################
# # # Main program:
# # #####################################

# # ###########################
# # # Data:
# # ###########################
from city_data import city_locations
number_of_cities = len(city_locations)

# # ###########################
# # # Parameters:
# # ###########################
number_of_ants = 50 ## Changes allowed.
alpha = 1.0         ## Changes allowed.
beta = 5.0          ## Changes allowed.
rho = 0.5           ## Changes allowed.
tau_0 = 0.1         ## Changes allowed.

target_path_length = 99.9999999

# #################################
# # Initialization:
# #################################

# ## To do: Add plot initialization here


pheromone_levels = initialize_pheromone_levels(number_of_cities, tau_0)
visibility = get_visibility(city_locations)

# # #################################
# # # Main loop:
# # #################################

iteration_index = 0
minimum_path_length = math.inf
path_length = math.inf


while (minimum_path_length > target_path_length):
  iteration_index += 1
  path_collection = []
  path_length_collection = []
  for ant_index in range(number_of_ants):  
    # Generate paths:
    path = generate_path(pheromone_levels, visibility, alpha, beta) # Uncomment after writing the function
    path_length = get_path_length(path, city_locations) # Uncomment after writing the function
    if (path_length < minimum_path_length):
      minimum_path_length = path_length
      print(minimum_path_length)
      # To do: Add code for plotting here
      plt.cla()
      plot_cities(plt,city_locations)
      plot_path(plt,path)
      plt.pause(2)
      plot_range = 20
      plt.xlim(0,plot_range)
      plt.ylim(0,plot_range)
      ax = plt.gca()
      ax.set_aspect('equal', adjustable='box')
      plot_cities(plt, city_locations)
      plot_path(plt, path)
      # Prepare plot
      plt.show(block=False)
      plt.ion()

      


      # print(delta_pheromone_levels)
      # print(pheromone_levels)
    path_collection.append(path)
    path_length_collection.append(path_length)

  # Update pheromone levels:
  delta_pheromone_levels = compute_delta_pheromone_levels(path_collection,path_length_collection) # Uncomment after writing the function
  pheromone_levels = update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho) # Uncomment after writing the function

input(f'Press return to exit')