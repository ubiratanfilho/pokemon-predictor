import pandas as pd
import streamlit as st

df = pd.read_csv("data/pokemon.csv")

def get_pokedex(df=df, sorted_=True):
    if sorted_:
        pokedex = df.name.unique().tolist()
        pokedex.sort()
        pokedex.insert(0, "")
        return pokedex
    
def get_poke_image(name, df=df):
    poke_id = df[df.name == name].index[0]+1
    image_path = "data/pokemon_images/{}.png".format(poke_id)
    return image_path

def catch_phrase(name):
    return "So %s is your fav? Let's see your next pokémon!" %name

