import requests
API_KEY = "e7264e2d904a4c3968452a5b62fb0808"


def get_data(place, forcast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

def draw_line_graph(canvas_elem, x_values, y_values):
    canvas_elem.erase()

    # Draw x and y axes
    canvas_elem.draw_line((50, 10), (50, 290), color="black")
    canvas_elem.draw_line((50, 290), (380, 290), color="black")

    # Draw data points and connect with lines
    for i in range(len(x_values) - 1):
        try:
            x1, y1 = 50 + int(x_values[i]) * 35, 290 - int(y_values[i]) * 2
            x2, y2 = 50 + int(x_values[i + 1]) * 35, 290 - int(y_values[i + 1]) * 2
            canvas_elem.draw_line((x1, y1), (x2, y2), color="blue")
        except ValueError:
            sg.popup_error("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    get_data("Sagar",2)
