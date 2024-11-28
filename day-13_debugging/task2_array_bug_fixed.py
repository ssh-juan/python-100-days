#FIXED: Changed the randint range from (1,6) to (0,5)
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

#The error occurs due to the 'randint' function. It selects until number 6, when actually there's not array 6 in 'dice_images' list.
#Lists start counting from 0