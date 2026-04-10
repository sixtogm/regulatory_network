import sys

print(sys.argv)

#Funcionalidades del programa

input_file= sys.argv[1]
input_format= sys.argv[2]
output_file= sys.argv[3]

open(sys.argv[1], "r").readlines()