import streamlit as st
st.set_page_config(page_title='Joker')
st.header("Catagories")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Joker")
  st.image("./joker-the-dark-knight-heath-ledger-movies-wallpaper.jpg", caption="Joker", width=300,use_column_width=True)
  st.write("Legendary Joker")
with col2:
  st.subheader("Joker and Batman")
  st.image("./HD-wallpaper-batman-joker-film-knight.jpg", caption="Batman", width=300,use_column_width=True)
  st.write("Legendary Batman")
