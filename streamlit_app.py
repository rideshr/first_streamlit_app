import streamlit;
import pandas as pd;

streamlit.title("Spideyyy..!!! Mannnn");
streamlit.header("Spideyyy..!!! Mannnn");
streamlit.text("Spideyyy..!!! Mannnn");

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index("Fruit");


fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ["Avocado", "Strawberries"]);
fruits_to_show = my_fruit_list.loc[fruits_selected];

streamlit.dataframe(my_fruit_list);
streamlit.dataframe(fruits_to_show);

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# takes the json version of response and normalize it... 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Output it to the screen as a table...
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector;
