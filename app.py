import streamlit as st
import pandas as pd
from func import * 
import time
from streamlit import state

st.title("What is your next Pokémon?")
st.subheader("Type your favorite pokémon below and I will predict your next Ash's Pikachu!")
st.image("ash-pikachu-unova.png", use_column_width=True)
fav_poke = st.selectbox("Type your favorite pokémon", get_pokedex())
if fav_poke != "":
    st.image(get_poke_image(fav_poke), width=300)
    st.write(catch_phrase(fav_poke))
    with st.spinner("Predicting your next pokémon..."):
        time.sleep(3)
    st.markdown("## **Your next pokémon is:**")
    st.image(get_poke_image("Lucario"), width=300)
    st.markdown("## Lucario!!")
    st.write("But how did I know that? I'm a machine! And I used a clustering algorithm to predict your next pokémon.")
    st.write("Can I convince you that I'm correct? Let's see!")
       
    st.title("How did I do it:")
    
    
