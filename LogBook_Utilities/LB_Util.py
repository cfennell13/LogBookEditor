import os
import shelve
from nt import getcwd


###
# Start up page - selection of plane type utilities
###
def get_plane_types(self):
    os.chdir(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes'))
    # DEBUG print(os.getcwd())
    
    #gets all of the files and directories in the given path and checks if it is a directory
    #only directories will be included in the types of planes
    return [x for x in os.listdir() 
            if os.path.isdir(os.path.join('.', x))]

def set_plane_type(self, plane):
    os.chdir(os.path.join('.', plane))
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
    '''
    gets all of the files and directories in the given path and checks if it is a directory
    only directories will be included in the types of planes
    '''
    return [x for x in os.listdir() 
            if os.path.isdir(os.path.join('.', x))]


###
# Final Submission Page utilities 
###

# goes to the previous directory 
def roll_back_plane(self):
    os.chdir("..")


def get_aplist(self):
    #gets a list of the A&Ps from the binary file 
    #Dictionary example as follows:
    '''
        mechanics: 
        Martin Lewis : A&P#
        Pierce Smith : A&P#
        etc. 
    '''
    
    print("Retrieving A&P list from shelf file")
    shelfFile = shelve.open(os.path.join('C:\\Users\\courtney.fennell\\Documents\\planes' , 'LogBookEditor_data'))  
    AP_list = shelfFile['mechanics']
    shelfFile.close()
    return AP_list
    
def create_new_logbook(self, selected_mech, tach_time):
    '''
    reads the new logbook template to initiate changes  
    '''

    from openpyxl import load_workbook
    from openpyxl.drawing.image import Image

    '''
    create a copy of the existing logbook 
    '''
    print("Preparing for edit of logbook entry file")
    wb = load_workbook('C:\\Users\\courtney.fennell\\Documents\\GitHub\\LogBookEditor\\MASTER_TEMPLATE.xlsx')
    sheet = wb.active
    
    
    '''
    Add the pictures to the excel doc
    #after MUCH trial and error, I still have no idea how size works but
    #this is what looks like a good size for the PEA logo
    '''
    print(os.getcwd()) #C:\Users\courtney.fennell\Documents\planes\Cessna 172\N123FF
    #this directory is the parent directory of the whole plane directories
    #this directory SHOULD contain the logo of the maintenance company
    #get the parent's parent directory
    company_logo = os.path.dirname(os.path.abspath('..')) 
    #get the logo.png
    company_logo = os.path.join(company_logo, 'logo.png')
    
    x=70
    my_png = Image(company_logo, size=(2*x, x))
    sheet.add_image(my_png, 'B2')  
    img = Image(company_logo, size=(2*x, x))
    sheet.add_image(img, 'B25')
    img = Image(company_logo, size=(2*x, x))
    sheet.add_image(img, 'B48')
    
    '''
    Set the mechanic on the excel doc
    '''
    AP_list = self.get_aplist()
    sheet["A21"]
    
    
    "Certificate #A&P" + selected_mech
    
    #set the tach time on the logbook
    sheet['I2'] = round(int(tach_time),1) # want 1 decimal point
    
    #create entries
    sheet['B10'] = "Airframe LOGBOOK ENTRY"
    sheet['B32'] = "Engine LOGBOOK ENTRY"
    sheet['B55'] = "Propeller LOGBOOK ENTRY"
    wb.save("newFILE_template.xlsx")
    
    '''
    Fix the formatting on the excel sheet so it matches the original file
    '''
    #currently in the plane's specific directory. need to backout and get the vb script 
    #or specify a full path to the file
    #os.system.subprocess.call(['cscript.exe', 'C:\\Users\\user\\FixFormatting.vbs', sheet])
    
def submit(self, selected_mech, tach_time): 
    '''
    executed when form is submitted.
    '''
    create_new_logbook(self, selected_mech, tach_time)
    return 0;

