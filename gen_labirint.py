# -*- coding: utf-8 -*-

# Генерим лабиринтичек

M = []

SIZE = [10, 10]

N_K = [1, 1] # начальная координата

def create_mass():
  for i in range(0, SIZE[0]):
    M.append([])
    for j in range(0, SIZE[1]):
      M[i].append(0)

  M[N_K[0]] [N_K[1]] = 2
  #print M

def steni_krai():
  for i in range(0, SIZE[0]):
    for j in range(0, SIZE[1]):
      if i == 0 or j == 0 or i == SIZE[0]-1 or j == SIZE[1]-1:
        M[i][j] = 1

def gen_p(): #генерирование главного пути
  t_k = N_K # текущая координата
  print "V = ", M[t_k[0]-1][t_k[1]]
  print "L = ", M[t_k[0]][t_k[1]-1]
  print "N = ", M[t_k[0]+1][t_k[1]]
  print "L = ", M[t_k[0]][t_k[1]+1]

create_mass()
steni_krai()
gen_p()

for i in range(0, SIZE[0]):
  print M[i]
