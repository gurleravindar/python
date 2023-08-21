from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H")

current_time_int = int(current_time)


if((current_time_int  >= 0 and current_time_int < 6) or (current_time_int >= 18 and current_time_int <= 24)):
    print("Night")
elif(current_time_int >=6 and current_time_int <18):
    print('Day')