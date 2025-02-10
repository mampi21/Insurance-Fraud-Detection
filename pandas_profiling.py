!pip install ydata-profiling
import pandas as pd
import ydata_profiling
from ydata_profiling import ProfileReport
import os
os._exit(00)
df="[Dataset]_Module8_(Insurance).csv"
df=pd.read_csv(df)
profile=ProfileReport(df, title="Insurance Dataset", html={'style' : {'full_width':True}})
profile.to_file(output_file='Insurance.html')
profile.to_notebook_iframe()
