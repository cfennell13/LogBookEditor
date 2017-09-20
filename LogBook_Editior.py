import tkinter as tk


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
    from LogBook_Utilities.LB_Util import get_plane_types, set_plane_type
    
    def execute_things(self, index, plane, controller):
        # This line would be where you insert the letter in the textbox
        
        #disables the one plane type that was selected
        for i in range(len(plane_list_btn)):
            plane_list_btn[i].config(state="normal")
        plane_list_btn[index].config(state="disabled")
        print(plane)
        self.set_plane_type(plane)
        
        #show next page
        controller.show_frame(N_Page)
        
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        self.bind("<<ShowFrame>>", self.on_show_frame(controller))
    
    
    #loop through all of the plane types and add the buttons to the screen
    def on_show_frame(self, controller):
        print("planes_page")
        #pull all of the planes from the directories
        all_planes = self.get_plane_types()
        
        for index in range(len(all_planes)): 
            
            n=all_planes[index]
        
            btn = tk.Button(self, text=all_planes[index],
                            command=lambda index=index, n=n: self.execute_things(index, n, controller) )
        
            # Add the button to the window
            btn.pack()
        
            # Add a reference to the button to 'buttons'
            plane_list_btn.append(btn)


class N_Page(tk.Frame):
    from LogBook_Utilities.LB_Util import collect_planes_n, set_plane_n, roll_back_plane_type
    
    def next_page(self, index, n, n_list, controller):
        # This line would be where you insert the letter in the textbox
        
        for i in range(len(n_list)):
            n_list[i].config(state="normal")
        n_list[index].config(state="disabled")
        
        self.set_plane_n(n)
        
        #show next frame
        controller.show_frame(Mech_Tac_Page)
        
    def previous_page(self, controller):  
            self.roll_back_plane_type() 
            controller.show_frame(Planes_Page)
               
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
        
       
        all_planes = self.collect_planes_n()
       
        #loop through all of the planes and add the buttons to the screen
        for index in range(len(all_planes)): 
            n=all_planes[index]
            
            button = tk.Button(self, text=all_planes[index],
                            command=lambda index=index, n=n: self.next_page(index, n, n_list, controller)) 
        
            # Add the button to the window
            button.pack()
        
            # Add a reference to the button to 'buttons'
            n_list.insert(index, button)
        
        prev_button = tk.Button(self, text="Prev",
                            command=lambda: self.previous_page(controller))
        prev_button.pack()
        n_list.insert(len(all_planes) +1, prev_button)

class Mech_Tac_Page(tk.Frame):
    from LogBook_Utilities.LB_Util import roll_back_plane, get_aplist
    
    def previous_page(self, controller):  
        self.roll_back_plane() 
        controller.show_frame(N_Page)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent) 
        Mech_list = self.get_aplist()
        
        self.bind("<<ShowFrame>>",lambda _: self.on_show_frame(controller, Mech_list))

    def on_show_frame(self, controller, Mech_list):
        print("mech+tac_page")
        for widget in tk.Frame.winfo_children(self):
            widget.destroy()
            n_list = []
            
        label = tk.Label(self, text="Mech Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        optionList = []
        for key in Mech_list: 
            optionList.append(key)
        self.dropVar=tk.StringVar()
        self.dropVar.set(optionList[0]) # default choice
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *optionList)  
        self.dropMenu1.pack() 
    
        prev_button = tk.Button(self, text="Prev",
                            command=lambda: self.previous_page(controller))
        prev_button.pack()    
        next_button = tk.Button(self, text="Submit",
                            command=lambda: submit(self))
        next_button.pack()
        
        
        

app = Logbook_Editor()
app.mainloop()