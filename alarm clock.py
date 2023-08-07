import datetime
import time
import winsound
import tkinter as tk
from tkinter import ttk

def set_alarm():
    alarm_time=f"{hour_combobox.get()} :{minute_combobox.get()}:{second_combobox.get()}"
    while True:
        current_time=datetime.datetime.now ().strftime("%H:%M:%S")
        if current_time==alarm_time:
            alarm_lable.config(text="wake up!",fg="orange",font=("Arial",15,"bold"))
            winsound.playsound("sound.wav",winsound.SND_ASYNC)
            break
        time.sleep(1)

def on_submit():
    set_alarm()
       

window=tk.Tk()
window.title("alarm clock")
window.geometry("400x300")
window.resizable(False,False)
label=tk.Label(window,text="select the alarm time",font=("Arial",12))
label.pack(pady=10)
frame=tk.Frame(window)
frame.pack()

hour_combobox=ttk.Combobox(frame,values=[str(i).zfill(2) for i in range(24)],state="readonly",width=3,font=("Arial",12))
hour_combobox.current(0)
hour_combobox.pack(side="left",padx=5)
minute_combobox=ttk.Combobox ( frame,values=[str(i).zfill(2) for i in range(60)],state="readonly",width=3,font=("Arial",12) )
minute_combobox.current(0)
minute_combobox.pack(side="left",padx=5)
second_combobox=ttk.Combobox(frame,values=[str(i).zfill(2) for i in range(60)],state="readonly",width=3,font=("Arial",12))
second_combobox.current(0)
second_combobox.pack(side="left",padx=5)
submit_button=tk.Button(window,text="set Alarm",command=on_submit, font=("Arial",12))
submit_button.pack (pady=10)
alarm_lable=tk.Label(window,text="",font=("Arial",14))
alarm_lable.pack()

window.mainloop()
                                                        
                                                    
                                                       
