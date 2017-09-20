import csv
import openpyxl
import os
import shelve


###
# Start up page - selection of plane type utilities
###
def get_plane_types(self):
    os.chdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes'))
    # DEBUG print(os.getcwd())
    return [x for x in os.listdir() 
            if os.path.isdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes', x))]

def set_plane_type(self, plane):
    os.chdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes\\', plane))
    # DEBUG print(os.getcwd())

    
###
# Plane N selection page utilities
###

#plane that is selected is then navigated to 
def set_plane_n(self, n_num):
    os.chdir(os.path.join(n_num))
    
def collect_planes_n(self):
    # DEBUG print(os.getcwd())
    return os.listdir()


###
# Final Submission Page utilities 
###

# goes to the previous directory 
def roll_back_plane(self):
    os.chdir("..")

#gets a list of the A&Ps from the binary file 
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
def read_logbook(self):
    #readin from the copy of the logbook
    print("Preparing for edit of logbook entry file")
    wb = openpyxl.load_workbook('.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')

#may be combined with read_logbook    
def edit_logbook(self):
    print("editing logbook")
    
def submit(self): #executed when form is submitted.
    print("hi")
    
