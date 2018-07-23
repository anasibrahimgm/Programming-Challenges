def double_digits(y):
	return '0' + str(y) if y < 10 else y

def time_format(seconds):
	minutes = int(seconds/60)
	return '({}:{})'.format(double_digits(minutes), double_digits(int(seconds - minutes * 60)))

goal = int(input("Goal in minutes: ")) * 60
play_period = int(input("Play Period: "))
pause_period = int(input("Pause Period: "))

print("*******************")

total_time = goal/play_period
num_doubles = goal/(play_period * 2)
ratio = pause_period/play_period

rem_time = goal - int(num_doubles) * (play_period * 2)

total_work_out = int(num_doubles) * 2 * (play_period + pause_period)

print('{}x {}+{}'.format(int(num_doubles) * 2, play_period, pause_period) + time_format(total_work_out))

if rem_time:
	x = int(rem_time/2)
	total_work_out += rem_time
	z = '2x {}'.format(x)

	if rem_time > play_period:
		total_work_out += x * ratio * 2
		z += '+{}'.format(int(x * ratio))

	print(z+ time_format(total_work_out))