import streamlit;
import pandas as pd;
import snowflake.connector;
import requests;
from urllib.error import URLError;

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

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information. ")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice);
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json());
    streamlit.dataframe(fruityvice_normalized);
except URLError as e:
  streamlit.error();

streamlit.stop();

# import snowflake.connector;

streamlit.header("The Fruit load list contains: ")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list");
    return my_cur.fetchall();

if streamlit.button('Get Fruit Load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list();
  streamlit.dataframe(my_data_rows);

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return 'Thanks for adding ' + new_fruit;
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Get Fruit Load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit);
  streamlit.text(back_from_function);



