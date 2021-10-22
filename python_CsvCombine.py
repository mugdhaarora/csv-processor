
import pandas as pd
import os, glob
from zipfile import ZipFile
import numpy as np
import socket as sock
  
# specifying the zip folder name
dirname = os.path.dirname(__file__)
folder_name = os.path.join(dirname, 'LandingFolder/Engineering Test Files.zip')
  
# opening the zip folder
with ZipFile(folder_name, 'r') as zip:
    # printing contents of the zip folder
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall(os.path.join(dirname, 'ProcessingFolder/'))
    print('Done!')
  

# get file names
path = os.path.join(dirname, 'ProcessingFolder/')
all_files = glob.glob(path + "**/*.csv",recursive=True)

print(all_files)

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)

merged_df = pd.concat(all_df, ignore_index=True, sort=True)

merged_df.drop(['Count','Events / Second','Events per Second'], axis=1,inplace=True)

merged_df.columns = merged_df.columns.str.strip()

merged_df['file']=merged_df['file'].apply(os.path.basename)

merged_df['file']=merged_df['file'].str.replace('\d+|\s+','',regex=True)


merged_df.drop_duplicates(keep='first',inplace = True)

merged_df.rename(columns=({ 'file': 'Environment'}), inplace=True)

sorted_df=merged_df.sort_values(by=['Environment'],ascending=False)

sorted_df.to_csv( "Combined.csv",index=False)



 