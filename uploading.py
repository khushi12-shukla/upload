import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))

def main():
    access_token = 'sl.BFtczYg_HT9Ee09psVTMY69qer7oKrEsEsJq3uNbDooLgOHOs3XbW_EEfphTImlH98FupVORRFZUzddC7AJkU2G2QPIjj293n5bSZ4O6aU_az5XaVZB8QCp8C3aRE5pQT9--JGk'
    transferData = TransferData(access_token)

    file_from = str(input("write the path name to upload it to our secure online soure"))
    file_to = input("enter the name of the file you want to upload your file in the source")

    transferData.upload_file(file_from,file_to)
    print("Your file has been successfully uploaded")