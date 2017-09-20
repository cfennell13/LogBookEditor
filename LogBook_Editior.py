import tkinter as tk
from LogBook_Utilities.LB_Util import *

LARGE_FONT= ("Verdana", 12)
plane_list_btn = []
n_list =[]

class Logbook_Editor(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Planes_Page, N_Page, Mech_Tac_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Planes_Page)

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

     
class Planes_Page(tk.Frame):
    from LogBook_Utilities.LB_Util import set_plane
    def execute_things(self, index, n, controller):
        self.select(index, n)
        controller.show_frame(N_Page)
    def select(self, index, plane):
        # This line would be where you insert the letter in the textbox
        for i in range(len(plane_list_btn)):
            plane_list_btn[i].config(state="normal")
        plane_list_btn[index].config(state="disabled")
        print(plane)
        self.set_plane(plane)
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        self.bind("<<ShowFrame>>", self.on_show_frame(controller))

    def on_show_frame(self, controller):
        print("planes_page")
        #pull all of the planes from the directories
        all_planes = collect_plane_types(self)
        
        
        for index in range(len(all_planes)): 
            
            n=all_planes[index]
        
            btn = tk.Button(self, text=all_planes[index],
                            command=lambda index=index, n=n: self.execute_things(index, n, controller) )
        
            # Add the button to the window
            btn.pack()
        
            # Add a reference to the button to 'buttons'
            plane_list_btn.append(btn)


class N_Page(tk.Frame):
    from LogBook_Utilities.LB_Util import chdir_plane_n
    def select(self, index, plane,n_list):
        # This line would be where you insert the letter in the textbox
        for i in range(len(n_list)):
            n_list[i].config(state="normal")
        n_list[index].config(state="disabled")
        print(plane)
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="N Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        
        self.bind("<<ShowFrame>>", lambda _: self.on_show_frame(controller))

    def on_show_frame(self, controller):
        
        for widget in tk.Frame.winfo_children(self):
            widget.destroy()
            n_list = []
        label = tk.Label(self, text="N Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)    
        
       
        all_planes = collect_planes(self)
       
        for index in range(len(all_planes)): 
            
            print("all_planes: n_list:", len(all_planes), len(n_list))
            n=all_planes[index]
            print("index", index)
        
            button = tk.Button(self, text=all_planes[index],
                            command=lambda index=index, n=n: self.select(index, n, n_list))
        
            # Add the button to the window
            button.pack()
        
            # Add a reference to the button to 'buttons'
            n_list.insert(index, button)
        
        prev_button = tk.Button(self, text="Prev",
                            command=lambda: controller.show_frame(Planes_Page))
        prev_button.pack()
        n_list.insert(len(all_planes) +1, prev_button)
        next_button = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(Mech_Tac_Page))
        next_button.pack()
        n_list.insert(len(all_planes) +2,next_button)

class Mech_Tac_Page(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Mech Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        self.bind("<<ShowFrame>>",lambda _: self.on_show_frame())

    def on_show_frame(self):
        print("mech+tac_page")
        Mech_list = get_aplist(self)
        print(Mech_list)
        optionList = []
        for key in Mech_list: 
            optionList.append(key)
        self.dropVar=tk.StringVar()
        self.dropVar.set("Yes") # default choice
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *optionList)   
            
        next_button = tk.Button(self, text="Submit",
                            command=lambda: edit_logbook(self))
        next_button.pack()
        
        

app = Logbook_Editor()
app.mainloop()