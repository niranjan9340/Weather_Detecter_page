import streamlit as st
import plotly.express as px
from backend import get_data

#  Add titile, text input, slider, select_box and subheader:
header = st.header("Weather Forcasr For Next Few Days")
place = st.text_input("Place:")
days = st.slider("Days",1,5)
option = st.selectbox("select data to view:", options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}.")

if place:
    # Get temperature and sky data :
    filtered_data= get_data(place,days) # getting data from backend

    if option == "Temperature": # checking for the select_box (option) with tha Temperature:
        # Create a temperature plot:
        temperature= [dict['main']['temp'] for dict in filtered_data] # Extracting the temeratures from filtered data
        dates = [dict["dt_txt"]for dict in filtered_data] # Extracting dates from the filtered data.
        figure = px.line(x=dates, y=temperature , labels={"x": "DATES", "y":"Temprature (c)"}) # creating the figure
        st.plotly_chart(figure) # ploting the figure in streamlit.

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds":"images/cloud.png",
                  "Rain":"images/rain.png", "Snow":"images/snow.png"
                  } # we have created dictionary of each sky condition with right spelling so we dont have to create path manually 16 time. and we used this dictionary in the list comprihension to create image path for each condition.
        sky_condition = [dict['weather'][0]['main'] for dict in filtered_data] # Extracting sky condition in list form
        print(sky_condition) # printing it to see if the spelling is right or wrong
        dates = [dict["dt_txt"] for dict in filtered_data] # extracting dates to put it in the image caption
        image_paths = [images[condition] for condition in sky_condition] # creating image path because we need the image path for all the condition so if there are 8 condition we need to display the 8 images.
        st.image(image_paths,width=115,caption=dates)
