import plotly as pk
import csv
import plotly.figure_factory as pd
import pandas as pf
import statistics as st

df=pf.read_csv("sp.csv")
read=df["reading score"].to_list()
write=df["writing score"].to_list()

r_mean= st.mean(read)
print("Read mean: ",r_mean)

w_mean= st.mean(write)
print("Write mean: ",w_mean)

r_median= st.median(read)
print("Read median: ",r_median)

w_median= st.median(write)
print("Write median: ",w_median)

r_mode= st.mode(read)
print("Read mode: ",r_mode)
 
w_mode= st.mode(write)
print("Write mode: ",w_mode)

r_hd= st.stdev(read)
print("Read dev:  ",r_hd)

w_hd= st.stdev(write)
print("Write dev:  ",w_hd)