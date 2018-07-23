goal = int(input("Goal in minutes: ")) * 60
play_period = int(input("Play Period: "))
pause_period = int(input("Pause Period: "))

total_time = goal/play_period

total_time_min = (int(total_time) * (play_period + pause_period) + play_period * (total_time - int(total_time)))/60
total_time_sec = int((total_time_min - int(total_time_min)) * 60)

print("Total Time: ", int(total_time_min), ":", str(total_time_sec) + '0' if total_time_sec < 10 else total_time_sec, sep="")
