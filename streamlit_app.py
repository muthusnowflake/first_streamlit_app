
#Streamlit Python Library has been imported
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

#Display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
          streamlit.write('The user entered ', fruit_choice)
    else:
          fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
          fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
          streamlit.dataframe(fruityvice_normalized)

 except URLError as e:
    streamlit.error()



#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


#dont execute past this till we troubleshoot
streamlit.stop()
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
