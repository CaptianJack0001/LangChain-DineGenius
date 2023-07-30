import streamlit as st
import langchain_helper
# Define the custom post-processing function



#Function to get user input for custom cuisine
def get_custom_cuisine_input():
    custom_cuisine = st.sidebar.text_input("Enter a Custom Cuisine")
    return custom_cuisine.strip() if custom_cuisine else None

st.title("Restaurant Name Generator")

# List of predefined cuisines
predefined_cuisines = ("Indian", "Italian", "Mexican", "Arabic", "American", "French", "Malaysian", "Japanese")

# Get user input for cuisine selection
cuisine = st.sidebar.selectbox("Pick a Cuisine", predefined_cuisines)

if not cuisine:
    # If the user did not select any cuisine from the predefined list,
    # ask for custom cuisine input
    cuisine = get_custom_cuisine_input()

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    refined_name, refined_menu_items = langchain_helper.post_process_restaurant_name_and_menu(response['restaurant_name'], response['menu_items'].strip().split(","), cuisine)

    st.header(refined_name)
    st.write("**Menu Items:**")
    for item in refined_menu_items:
        st.write("-", item)
