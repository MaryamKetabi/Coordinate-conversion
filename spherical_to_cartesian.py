import numpy as np

def spherical_to_cartesian(r, a, b):
    x = r * np.sin(a) * np.cos(b)
    y = r * np.sin(a) * np.sin(b)
    z = r * np.cos(a)
    return x, y, z

particle_list = []

n = int(input("Numbers of particles?"))

for i in range(n):

  print(f"Enter the components for particle {i+1}:")
  r = float(input("r = "))
  a = float(input("a = "))
  b = float(input("b = "))

  x, y, z = spherical_to_cartesian(r, a, b)

  particle = np.array([x, y, z])

  particle_list.append(particle)

for i, particle in enumerate(particle_list):
    print(f"Particle {i+1}: x = {particle[0]}, y = {particle[1]}, z = {particle[2]}")
