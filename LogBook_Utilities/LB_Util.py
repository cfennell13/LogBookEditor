import csv
import openpyxl
import os
import shelve

def get_aplist(self):
    shelfFile = shelve.open(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes' , 'LogBookEditor_data'))  
    AP_list = shelfFile['mechanics']
    shelfFile.close()
    return AP_list
    
def copy_logbook(self):
    #make a copy of the logbook template to work off of
    print("Copying logbook entry file")
     
def read_logbook(self):
    #readin from the copy of the logbook
    print("Preparing for edit of logbook entry file")
    wb = openpyxl.load_workbook('.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    
def collect_plane_types(self):
    os.chdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes'))
    # DEBUG print(os.getcwd())
    return [x for x in os.listdir() 
            if os.path.isdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes', x))]
    
def set_plane(self, plane):
    os.chdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes\\', plane))
    # DEBUG print(os.getcwd())
def chdir_plane_n(self, n_num):
    os.chdir(os.path.join(n_num))

    
def collect_planes(self):
    # DEBUG print(os.getcwd())
    return os.listdir()

def edit_logbook(self):
    print("editing logbook")
  
