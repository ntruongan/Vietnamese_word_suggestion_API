# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:36:19 2021

@author: ntruo
"""


from tkinter import Label, Text, Tk
import requests
KERAS_REST_API_URL = "http://127.0.0.1:5000/predict"

class MyWindow:
    def __init__(self, window):
        # self.model = models
        self.window = window
        self.lbl_input = Label(window, text="INPUT")
        self.txt_input = Text(window)
        self.txt_input.bind('<<Modified>>', self.load_api)
        self.lbl_input.place(x = 0,y = 100)
        self.txt_input.place(x = 150,y = 000)
        
        self.lbl_output = Label(window, text="Prediction", bg="orange", fg="red")
        self.txt_output = Text(window)
        self.lbl_output.place(x = 560,y = 600)
        
             
    def load_api(self, value=None):
        """
        Call API to predcit next word
        """
        flag = self.txt_input.edit_modified()
        if flag:    
            input_ =  self.txt_input.get("1.0","end")
            payload = {"input_": input_}
            r = requests.post(KERAS_REST_API_URL, files=payload).json()
            self.lbl_output.config(text=r["predictions"])
            self.txt_input.edit_modified(False)

            
    def command(self):
        pass
   
def main():
    window=Tk()
    mywin=MyWindow(window)
    window.title('Word prediction')
    window.geometry("1120x650")
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    main()
