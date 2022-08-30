#Streamlit Python Library has been imported

import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Pandas Python Library has been imported
import pandas
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())

#dont execute past this till we troubleshoot
streamlit.stop()

import snowflake.connector


#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("The fruit load contains")
#streamlit.text(my_data_row)
#streamlit.dataframe (my_data_row)
streamlit.dataframe(my_data_rows)
fruit_choice1 = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', fruit_choice1)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
