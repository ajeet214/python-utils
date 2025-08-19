import wordninja

s = "converttobigendian"
words = wordninja.split(s)   # ['convert', 'to', 'big', 'endian']
snake_case = "_".join(words)
print(snake_case)  # convert_to_big_endian


