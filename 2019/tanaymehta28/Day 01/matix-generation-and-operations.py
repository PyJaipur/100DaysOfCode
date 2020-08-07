##############################################
# Author: Tanay Mehta
# Github: https://github.com/tanaymehta28
# Twitter: https://twitter.com/Tanaymehta28
##############################################

import random

# Oh come on, if you have ever used numpy; you know what this all is about.
# I have made two classes for (1d and 2d) matrix generation.
# The other class (MatrixOps) consists of numerous matrix operations.
class oneD:
    def zeroes(n):
        array=[0 for temp_03cxfc in range(n)]
        return array
    def rand(n):
        array = [random.random() for temp_03xfc in range(n)]
        return array
class twoD:
    def zeroes(a,b):
        array = [[0 for temp_03cfg in range(a)] for temp_03cfh in range(b)]
        return array
    def rand(a,b):
        array = [[random.random() for temp_03cfg in range(a)] for temp_03cfh in range(b)]
        return array
class MatrixOps:
    def transpose(array):
        transpose_array = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]
        return transpose_array

# More coming here soon!
