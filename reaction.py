from gpiozero import LED,Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

left_score = 0
right_score = 0

rounds = 3

for _ in range(rounds):
	led.on()
	sleep(uniform(5,10))
	led.off()

def pressed(button):
	global left_score, right_score
	if button.pin.number == 14:
		left_score += 1
		print(left_name + ' won this round')
	else:
		right_score += 1
		print(right_name + ' won this round')

right_button.when_pressed = pressed
left_button.when_pressed = pressed

while not (left_button.is_pressed or right_button.is_pressed):
	sleep(0.1)

right_button.when_pressed = None
left_button.when_pressed = None

print(f"{left_name}'s total score: {left_score}")
print(f"{right_name}'s total score: {right_score}")
exit()
