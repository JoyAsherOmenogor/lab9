import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

# Constants
API_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(pokemon_name):
    try:
        response = requests.get(API_BASE_URL + pokemon_name.lower())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if not poke_name:
        messagebox.showwarning("Input Error", "Please enter a Pokemon name.")
        return

    poke_info = get_pokemon_info(poke_name)

    if poke_info:
        # Populate the Info frame
        label_name_value.config(text=f"Name: {poke_info['name'].capitalize()}")
        label_height_value.config(text=f"Height: {poke_info['height']} dm")
        label_weight_value.config(text=f"Weight: {poke_info['weight']} hg")
        label_types_value.config(text=f"Type(s): {', '.join(type_info['type']['name'] for type_info in poke_info['types'])}")

        # Populate the Stats frame
        special_attack_bar["value"] = poke_info['stats'][3]['base_stat']
        special_defense_bar["value"] = poke_info['stats'][4]['base_stat']
        speed_bar["value"] = poke_info['stats'][0]['base_stat']

    else:
        messagebox.showerror("Error", f"Failed to retrieve Pokémon information for {poke_name.capitalize()}.")

# Create the main window
root = tk.Tk()
root.title("Pokemon Information")
root.geometry("400x250")

# Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

frame_info = ttk.LabelFrame(root, text="Info")
frame_info.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

frame_stats = ttk.LabelFrame(root, text="Stats")
frame_stats.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Input widgets
label_name = ttk.Label(frame_input, text="Enter Pokemon Name:")
label_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

enter_name = ttk.Entry(frame_input)
enter_name.insert(0, 'mew')
enter_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")

button_get_info = ttk.Button(frame_input, text="Get Info", command=handle_button_get_info)
button_get_info.grid(row=0, column=2, padx=5, pady=5, sticky="e")

# Info frame widgets
label_name_value = ttk.Label(frame_info, text="")
label_name_value.grid(row=0, column=0, padx=5, pady=2, sticky="w")

label_height_value = ttk.Label(frame_info, text="")
label_height_value.grid(row=1, column=0, padx=5, pady=2, sticky="w")

label_weight_value = ttk.Label(frame_info, text="")
label_weight_value.grid(row=2, column=0, padx=5, pady=2, sticky="w")

label_types_value = ttk.Label(frame_info, text="")
label_types_value.grid(row=3, column=0, padx=5, pady=2, sticky="w")

# Stats frame widgets
special_attack_bar = ttk.Progressbar(frame_stats, length=100, mode="determinate")
special_attack_bar.grid(row=0, column=0, padx=5, pady=2, sticky="w")

special_defense_bar = ttk.Progressbar(frame_stats, length=100, mode="determinate")
special_defense_bar.grid(row=1, column=0, padx=5, pady=2, sticky="w")

speed_bar = ttk.Progressbar(frame_stats, length=100, mode="determinate")
speed_bar.grid(row=2, column=0, padx=5, pady=2, sticky="w")

# Set column weights for responsive resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
frame_info.columnconfigure(0, weight=1)
frame_stats.columnconfigure(0, weight=1)

# Start the main event loop
root.mainloop()
