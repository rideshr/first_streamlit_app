import streamlit;
import pandas as pd;

streamlit.title("Spideyyy..!!! Mannnn");
streamlit.header("Spideyyy..!!! Mannnn");
streamlit.text("Spideyyy..!!! Mannnn");

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(my_fruit_list);
