from tkinter import*
from PIL import ImageTk,Image
import tkinter.font as tkFont
from turtle import Turtle,Screen, mainloop
import random, time
import random

def Humidity(): 
	def update_gauge():
		newvalue = random.randint(low_r,hi_r)
		cnvs.itemconfig(id_text,text = str(newvalue) + " %")
		# Rescale value to angle range (0%=120deg, 100%=30 deg)
		angle = 120 * (hi_r - newvalue)/(hi_r - low_r) + 30
		cnvs.itemconfig(id_needle,start = angle)
		root.after(3000, update_gauge)
	
		
	# Create Canvas objects    
	
	canvas_width = 400
	canvas_height =300
	
	root = Tk()
	root.title("Humidity") 
	cnvs = Canvas(root, width=canvas_width, height=canvas_height)
	cnvs.grid(row=2, column=1)
	
	coord = 10, 50, 350, 350 #define the size of the gauge
	low_r = 0 # chart low range
	hi_r = 100 # chart hi range
	
	# Create a background arc with a number of range lines
	numpies = 8
	for i in range(numpies):
		cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
	
	# add hi/low bands
	cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
	cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
	cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
	# add needle/value pointer
	id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
	
	# Add some labels
	cnvs.create_text(180,15,font="Times 20 italic bold", text="Humidity")
	cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
	cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
	id_text = cnvs.create_text(170,210,font="Times 15 bold")
	root.after(3000, update_gauge)
	root.mainloop()
	
def Temp(): 
	def update_gauge():
		newvalue = random.randint(low_r,hi_r)
		cnvs.itemconfig(id_text,text = str(newvalue) + " %")
		# Rescale value to angle range (0%=120deg, 100%=30 deg)
		angle = 120 * (hi_r - newvalue)/(hi_r - low_r) + 30
		cnvs.itemconfig(id_needle,start = angle)
		root.after(3000, update_gauge)
	
		
	# Create Canvas objects    
	
	canvas_width = 400
	canvas_height =300
	
	root = Tk()
	root.title("Humidity") 
	cnvs = Canvas(root, width=canvas_width, height=canvas_height)
	cnvs.grid(row=2, column=1)
	
	coord = 10, 50, 350, 350 #define the size of the gauge
	low_r = 0 # chart low range
	hi_r = 100 # chart hi range
	
	# Create a background arc with a number of range lines
	numpies = 8
	for i in range(numpies):
		cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
	
	# add hi/low bands
	cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
	cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
	cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
	# add needle/value pointer
	id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
	
	# Add some labels
	cnvs.create_text(180,15,font="Times 20 italic bold", text="Temperature")
	cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
	cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
	id_text = cnvs.create_text(170,210,font="Times 15 bold")
	root.after(3000, update_gauge)
	root.mainloop()
	
def Day():
	day_w=Toplevel()
	day_w.geometry("300x300")
	day_w.configure(bg="DarkSlateGray4")
	day_w.title("Day")
	day_img=PhotoImage(file="sun.png")
	day_img=day_img.subsample(2,2)
	day_l=Label(day_w,image=day_img,bg="DarkSlateGray4")
	day_l.pack()
	day_w.update()
	day_w.mainloop()
	
def Welcome():
	root = Tk()
	root.title("Nuclear Reactor")
	root.configure(background ='steel blue')
	root.geometry("300x200")
	#creating a font object
	fontObj = tkFont.Font(size=28)
	# Creating a Label Widget
	myLabel = Label(root,text="Nuclear Reactor",font = fontObj)
	img = ImageTk.PhotoImage(Image.open("volcano.png"))
	panel = Label(root, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")
	# Creating 3 buttons for Temperature,Day,Humidity
	hum = Button(root, text="Humidity",background = 'pink3',height = 2, width = 13,padx=55, bd=2,command = Humidity).place(x=200, y=100)
	temp = Button(root, text="Temperature",background = 'LightSkyBlue1',height = 2, width = 13,padx=55, bd=2,command = Temp).place(x=450, y=100)
	day = Button(root, text="Day",background = 'pale green',height = 2, width = 13,padx=55, bd=2,command = Day).place(x=700, y=100)
	
	myLabel.pack()
	root.mainloop()
	
	
