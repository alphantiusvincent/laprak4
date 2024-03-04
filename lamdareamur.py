celcius_to_fahrenheit = lambda C: (9/5) * C + 32
celcius_to_reamur = lambda C: 0.8 * C
input_C = 100
print("Input C =", input_C, ". Output F =", celcius_to_fahrenheit(input_C))
input_C = 80
print("Input C =", input_C, ". Output R =", celcius_to_reamur(input_C))
input_C = 0
print("Input C =", input_C, ". Output F =", celcius_to_fahrenheit(input_C))