import streamlit
streamlit.title('My parents Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blue berry oatmeal')
streamlit.text('🥗kale spinach & rocket smoothie')
streamlit.text('🐔Hard boiled Free-rane egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
