# input
time_black = int(input("Enter the time the black player thought: "))
time_white = int(input("Enter the time the white player thought: "))
human_time = 0

# determine which is human
if time_black > time_white:
    human_time = time_black
elif time_black < time_white:
    human_time = time_white
ss = "00"
mm = "00"
hh = "00"
ss = int(human_time * 0.001) # 1 millisecond = 0.001 seconds

if ss > 60:
    mm = int(ss / 60)
    ss = ss % 60
    if mm > 60:
        hh = int(mm / 60)
        mm = mm % 60

def format(time):
    time = "0" + str(time)
    return time

if 0 < int(ss) < 10:
    ss = format(ss)
if 0 < int(mm) < 10:
    mm = format(mm)
if 0 < int(hh) < 10:
    hh = format(hh)
print(f"The time the human player has spent thinking is: {hh}:{mm}:{ss}")