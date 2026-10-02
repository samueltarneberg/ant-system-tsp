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
   n = len(city_locations)
   eta_list = []
   for city_i in city_locations:
      row = []
      for city_j in city_locations:
          x1_ij = (city_i[0] - city_j[0])
          x2_ij = (city_i[1] - city_j[1])
          d_ij = np.abs((x1_ij)**2 - (x2_ij)**2)
          if d_ij == 0:
              eta_ij = 0
          else:
            eta_ij = float(1 / d_ij)
          row.append(eta_ij)
      eta_list.append(row)
   return eta_list

tau_0 = 0.1      
pheromone_levels = initialize_pheromone_levels(number_of_cities, tau_0)
visibility = get_visibility(city_locations)
print(visibility)
# print(pheromone_levels)
# Add code here!



# #################################################################
# ## To do: Write the generate_path function (Note: You may wish
# ##       to add more functions, e.g., get_node. That is allowed).
# #################################################################

def generate_path(pheromone_levels, visibility, alpha, beta):
    # p = probability for selecting path e_ij
    a = [[12],[1]]
    n_i = sum(isinstance(item, list) for item in a) 
    n_j = len(pheromone_levels[0])
    r = np.random.rand()

    r_i = np.random.randint(0,n_i)
    r_j = np.random.randint(0,n_j)

    p = (pheromone_levels[r_i][r_j]**alpha) * (visibility[r_i][r_j]**beta) 
    print(n_i,n_j)
    # return path
generate_path(pheromone_levels,visibility,0,0)

#     generate e_ij -> e_mn

# # # Add code here!

# ###############################################################
# ## To do: Write the get_path_length function:
# ###############################################################

def get_path_length(path, city_locations):
  #  generate every single path in a matrix:
      i, j = path
      paths_matrix = []
      for city_i in city_locations:
        row = []
        for city_j in city_locations:
            x1_ij = (city_i[0] - city_j[0])
            x2_ij = (city_i[1] - city_j[1])
            d_ij = np.abs((x1_ij)**2 - (x2_ij)**2)
            row.append(d_ij)
        paths_matrix.append(row)
      return paths_matrix[i][j]
path=[3,3]
print(get_path_length(path,city_locations))
            
        
      
        

# Add code here!

# ###############################################################
# ## To do: Write the compute_delta_pheromone_levels function:
# ###############################################################

# def compute_delta_pheromone_levels(path_collection, path_length_collection):

# # # Add code here!

# # ###############################################################
# # ## To do: Write the update_pheromone_levels function:
# # ###############################################################

# def update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho):

# # # Add code here!

# ##################################################
# #  Plots the cities (nodes):
# ##################################################

# # Add plot code here (can be more than one function)

# #####################################
# # Main program:
# #####################################

# ###########################
# # Data:
# ###########################
# from city_data import city_locations
# number_of_cities = len(city_locations)

# ###########################
# # Parameters:
# ###########################
# number_of_ants = 50 ## Changes allowed.
# alpha = 1.0         ## Changes allowed.
# beta = 5.0          ## Changes allowed.
# rho = 0.5           ## Changes allowed.
# tau_0 = 0.1         ## Changes allowed.

# target_path_length = 99.9999999

# #################################
# # Initialization:
# #################################

# ## To do: Add plot initialization here


# pheromone_levels = initialize_pheromone_levels(number_of_cities, tau_0)
# visibility = get_visibility(city_locations)

# #################################
# # Main loop:
# #################################

# iteration_index = 0
# minimum_path_length = math.inf
# path_length = math.inf


# while (minimum_path_length > target_path_length):
#   iteration_index += 1
#   path_collection = []
#   path_length_collection = []
#   for ant_index in range(number_of_ants):  
#     # Generate paths:
#     path = generate_path(pheromone_levels, visibility, alpha, beta) # Uncomment after writing the function
#     path_length = get_path_length(path, city_locations) # Uncomment after writing the function
#     if (path_length < minimum_path_length):
#       minimum_path_length = path_length
#       print(minimum_path_length)
      
#       # To do: Add code for plotting here

#     path_collection.append(path)
#     path_length_collection.append(path_length)
#   # Update pheromone levels:
#   delta_pheromone_levels = compute_delta_pheromone_levels(path_collection,path_length_collection) # Uncomment after writing the function
#   pheromone_levels = update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho) # Uncomment after writing the function

# input(f'Press return to exit')