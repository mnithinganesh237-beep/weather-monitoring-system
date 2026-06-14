import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API Key

def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        result = (
            f"City: {data['name']}\n"
            f"Temperature: {data['main']['temp']} °C\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Weather: {data['weather'][0]['description']}\n"
            f"Wind Speed: {data['wind']['speed']} m/s"
        )
    else:
        result = "City not found!"

    result_label.config(text=result)

# Create Window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Heading
title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# City Input
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Button
search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

# Result Area
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run App
root.mainloop()