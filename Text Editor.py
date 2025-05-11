


from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window=Tk()
window.title("Codingals Text Editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def openfile():
  filepath=askopenfilename(
       filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
  if  not filepath:
        return
  txt_edit.delete(1.0,END)
  with open(filepath,"r")as input_file:
    text=input_file.read()
    txt_edit.insert(END,text)
  window.title("Condingals file wditor"+filepath)
  
def savefile():
  savefile=asksaveasfilename(
    defaultextension=.txt
     filetypes=[("Text Files","*.txt"),("All Files","*.*")]
  )
  if  not savefile:
      return
  txt_edit.delete(1.0,END)
  with open(savefile,"w")as input_file:
  text=input_file.write()
  txt_edit.insert(END,text)
  window.title("Condingals file editor"+savefile)
txt_ox=Text(window)
fr_button=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="Open",command=openfile)
btn_save=Button(fr_button,text="Save",command=savefile)
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_button.grid(row=0,column=0,sticky="ns")
txt_button.grid(row=0,column=1,sticky="nsew")