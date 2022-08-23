#Streamlit Python Library has been imported
import streamlit

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Pandas Python Library has been imported
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let us create a pick list so they can pick the fruit the want to include .. we are prepopulating values for giving example to customer.
streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index),['Avacado','Strawberries'])

#Display the table on the page
streamlit.dataframe(my_fruit_list)
