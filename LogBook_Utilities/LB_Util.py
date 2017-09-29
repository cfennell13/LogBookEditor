import csv
import openpyxl

import os
import shelve
from openpyxl import cell


###
# Start up page - selection of plane type utilities
###
def get_plane_types(self):
    os.chdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes'))
    # DEBUG print(os.getcwd())
    
    #gets all of the files and directories in the given path and checks if it is a directory
    #only directories will be included in the types of planes
    return [x for x in os.listdir() 
            if os.path.isdir(os.path.join('.\\', x))]

def set_plane_type(self, plane):
    os.chdir(os.path.join('.\\', plane))
    # DEBUG print(os.getcwd())

    
###
# Plane N selection page utilities
###

#plane that is selected is then navigated to 
def roll_back_plane_type(self):
    os.chdir("..")
    
def set_plane_n(self, n_num):
    os.chdir(os.path.join(n_num))
    
def collect_planes_n(self):
    # DEBUG print(os.getcwd())
    #gets all of the files and directories in the given path and checks if it is a directory
    #only directories will be included in the types of planes
    return [x for x in os.listdir() 
            if os.path.isdir(os.path.join('.\\', x))]


###
# Final Submission Page utilities 
###

# goes to the previous directory 
def roll_back_plane(self):
    os.chdir("..")

#gets a list of the A&Ps from the binary file 
#Dictionary example as follows:
'''
mechanics: 
    Martin Lewis : A&P#
    Pierce Smith : A&P#
    etc. 
'''
def get_aplist(self):
    print("Retrieving A&P list from shelf file")
    shelfFile = shelve.open(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes' , 'LogBookEditor_data'))  
    AP_list = shelfFile['mechanics']
    shelfFile.close()
    return AP_list

#creates a copy of the logbook for editing    
def copy_logbook(self):
    #make a copy of the logbook template to work off of
    print("Copying logbook entry file")

#reads the new logbook template to initiate changes      
def read_logbook():
    import openpyxl
    from openpyxl import load_workbook
    from openpyxl import Workbook
    from openpyxl.drawing.image import Image
    
    #readin from the copy of the logbook
    print("Preparing for edit of logbook entry file")
    wb = openpyxl.load_workbook('C:\\Users\\courtney.fennell\\Documents\\GitHub\\LogBookEditor\\MASTER_TEMPLATE.xlsx')
    sheet = wb.active
    
    
    png_loc = r'C:\\Users\\courtney.fennell\\Documents\\GitHub\\LogBookEditor\\PEA_logo.png'
    #after MUCH trial and error, I still have no idea how size works but
    #this is what looks like a good size for the PEA logo
    x=70
    my_png = Image(png_loc, size=(2*x, x))
    sheet.add_image(my_png, 'B2')  
    img = Image(png_loc, size=(x, 2*x))
    sheet.add_image(img, 'B24')
    img = Image(png_loc, size=(40, 40))
    sheet.add_image(img, 'B44')
    
    sheet['A10'] = "LOGBOOK ENTRY"
    wb.save("newFILE_template.xlsx")

#may be combined with read_logbook    
def edit_logbook(self):
    print("editing logbook")
    
def submit(self): #executed when form is submitted.
    read_logbook()
    
