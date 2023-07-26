import random

import streamlit as st


def suggest_restaurant():
    st.title("Taiwanese Restaurant Suggester")
    st.write("Discover local food restaurants in Taiwan!")

    # List of restaurant options
    restaurants = [
        "Din Tai Fung",
        "Hakka Delights",
        "Fresh Seafood House",
        "Taipei Dumpling",
        "Night Market",
    ]

    # Suggest a random restaurant when the button is clicked
    if st.button("Suggest Restaurant"):
        suggested_restaurant = random.choice(restaurants)
        st.subheader("Suggested Restaurant:")
        st.write(f"**{suggested_restaurant}**")


if __name__ == "__main__":
    suggest_restaurant()
