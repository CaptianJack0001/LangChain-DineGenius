from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openai_key

import os
os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain({'cuisine': cuisine})

    return response
# Define the custom post-processing function
def post_process_restaurant_name_and_menu(restaurant_name, menu_items, cuisine):
    if cuisine == "Indian":
        # Apply specific post-processing for Indian cuisine
        # Add a prefix to the restaurant name
        restaurant_name = "Saffron Spice " + restaurant_name
        # Adjust menu items for Indian cuisine (example: replace "tacos" with "samosas")
        menu_items = [item.replace("tacos", "samosas") for item in menu_items]
        # Add any other adjustments to menu items if needed

    elif cuisine == "Italian":
        # Apply specific post-processing for Italian cuisine
        # Add a suffix to the restaurant name
        restaurant_name = restaurant_name + " Bella Vita"
        # Add any other adjustments to menu items if needed
        # Example: Replace "burritos" with "pizza"
        menu_items = [item.replace("burritos", "pizza") for item in menu_items]

    elif cuisine == "Mexican":
        # Apply specific post-processing for Mexican cuisine
        # Add a prefix to the restaurant name
        restaurant_name = "El Mariachi " + restaurant_name
        # Add any other adjustments to menu items if needed
        # Example: Replace "pasta" with "enchiladas"
        menu_items = [item.replace("pasta", "enchiladas") for item in menu_items]

    elif cuisine == "Arabic":
        # Apply specific post-processing for Arabic cuisine
        # Add a suffix to the restaurant name
        restaurant_name = restaurant_name + " Al Jazeera"
        # Add any other adjustments to menu items if needed
        # Example: Replace "hamburger" with "shawarma"
        menu_items = [item.replace("hamburger", "shawarma") for item in menu_items]

    elif cuisine == "American":
        # Apply specific post-processing for American cuisine
        # Add a prefix to the restaurant name
        restaurant_name = "All-American " + restaurant_name
        # Add any other adjustments to menu items if needed
        # Example: Replace "sushi" with "hamburger"
        menu_items = [item.replace("sushi", "hamburger") for item in menu_items]

    elif cuisine == "French":
        # Apply specific post-processing for French cuisine
        # Add a prefix to the restaurant name
        restaurant_name = "Le Petit " + restaurant_name
        # Add any other adjustments to menu items if needed
        # Example: Replace "tacos" with "croissants"
        menu_items = [item.replace("tacos", "croissants") for item in menu_items]

    elif cuisine == "Malaysian":
        # Apply specific post-processing for Malaysian cuisine
        # Add a suffix to the restaurant name
        restaurant_name = restaurant_name + " Boleh"
        # Add any other adjustments to menu items if needed
        # Example: Replace "steak" with "nasi lemak"
        menu_items = [item.replace("steak", "nasi lemak") for item in menu_items]

    elif cuisine == "Japanese":
        # Apply specific post-processing for Japanese cuisine
        # Add a suffix to the restaurant name
        restaurant_name = restaurant_name + " Sushiya"
        # Add any other adjustments to menu items if needed
        # Example: Replace "burritos" with "sushi rolls"
        menu_items = [item.replace("burritos", "sushi rolls") for item in menu_items]

    # Add more cuisine-specific post-processing as needed for other cuisines
    # ...

    # Return the refined restaurant name and menu items
    return restaurant_name, menu_items

if __name__== "__main__":
  generate_restaurant_name_and_items("Indians")
