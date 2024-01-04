import PySimpleGUI as sg
import plotly.express as px
from backend import get_data

layout = [
    [sg.Text("Place:"), sg.InputText(key="place")],
    [sg.Text("Days:"), sg.Slider(range=(1, 5), orientation="h", key="days")],
    [sg.Text("Select data to view:"), sg.Combo(["Temperature", "Sky"], key="option")],
    [sg.Button("Submit")],
    [sg.Graph(canvas_size=(800, 400), graph_bottom_left=(0, 0), graph_top_right=(800, 400), background_color='white', key='graph')],
]

window = sg.Window("Weather Forecast For Next Few Days", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    place = values["place"]
    days = int(values["days"])
    option = values["option"]

    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict['main']['temp'] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "DATES", "y": "Temperature (°C)"})
            figure.update_layout(showlegend=False)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png",
            }
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            window['graph'].Erase()

            for i, (image_path, date) in enumerate(zip(image_paths, dates)):
                x_position = i * 150
                window['graph'].DrawImage(image_path, location=(x_position, 0))

window.close()
