
import mouse
import time
from datetime import datetime, timedelta
from tkinter import *
import threading

# Configure TkInter
root = Tk()
root.geometry("600x250")
root.title("Anty-Away in Teams") 
timeset = Label(root, text="How long script should works (in minutes): ", font=('calibre',10,'bold'))
timeset.pack()
running = True
time_work_var = StringVar()
time_work_entry = Entry(root, textvariable=time_work_var, font=('calibre',10,'normal'))
time_work_entry.pack()
time_work = time_work_var.get()
# Configure scrollbar in interface
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)


def start():
    threading.Thread(target=counting).start()
    time.sleep(0.5)
    threading.Thread(target=timing).start()

def stop():
    global running
    running = False
    root.quit()
    
def counting():
    while running:
        global now_time2, current_time
        now_time2 = datetime.now()
        current_time = now_time2.strftime("%H:%M:%S")
        time.sleep(2)

#loop don't let us 'be away in teams'
def timing():
    if running:
        eula = Text(root, yscrollcommand=scroll.set)
        eula.pack()
        now_time=datetime.now()
        now_time_format = now_time.strftime("%H:%M:%S")
        min_left = 2
        time_work = time_work_var.get()
        n = int(time_work)  #ilosc czasu jaki ma dzialać skrypt
        final_time=now_time + timedelta(minutes=n)

        # Update textbox 'eula' in window
        print("-----------------------------------------")
        eula.insert(END, "------------------------------------------------------------\n")
        eula.insert(END, f"Script started at: {now_time_format}.\nTime left: {final_time-now_time} minutes\n")
        print("Script started at: {}".format(now_time.strftime("%H:%M:%S")))
        print("Time left : " ,final_time-now_time,"minutes")

        time_by1 =  now_time + timedelta(minutes=min_left)
        time_by1_format = time_by1.strftime("%H:%M:%S")

        while running:
            final_time_format = final_time.strftime("%H:%M:%S")
            min_before_end = final_time - timedelta(minutes=0.2)
            min_before_end_format = min_before_end.strftime("%H:%M:%S")
            time.sleep(3)
            if current_time >= time_by1_format:
                min_left += 2
                mouse.move("420", "500") 
                mouse.click("left")
                mouse.move("200", "400")
                mouse.click("left")

                # Set time variable and uptade the exsisting one
                print("Time left : " ,final_time-now_time2,"minutes")
                time_by1 =  now_time + timedelta(minutes=min_left)
                time_by1_format = time_by1.strftime("%H:%M:%S")
                left_time_format = str(final_time - now_time2) 

                # Update textbox 'eula' in window
                eula.insert(END, f"Duration: {left_time_format[:-7]} minutes. Script will finish at {final_time_format}.\n")
                scroll.config(command=eula.yview)

            if current_time >= min_before_end_format:
                # Update textbox 'eula' in window
                print("Script finished at:",datetime.now())
                eula.insert(END, f"Script finished at: {current_time}.\n")
    
                running == False
                break
                    
                    

            

startButton = Button(root, text="Run Script", command=start).pack()
stopButton = Button(root, text="Stop", command=stop).pack() 

# root.after(1000, timing) 

root.mainloop()