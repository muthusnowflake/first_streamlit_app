
#Streamlit Python Library has been imported

import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Pandas Python Library has been imported
import pandas
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let us create a pick list so they can pick the fruit the want to include .. we are prepopulating values for giving example to customer.
#streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the table on the page
#streamlit.dataframe(my_fruit_list)
#streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        streamlit.write('The user entered ', fruit_choice)

#import requests
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 

#import streamlit
#streamlit.stop()
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)
#dont execute past this till we troubleshoot
