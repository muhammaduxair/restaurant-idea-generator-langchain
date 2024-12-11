import streamlit as st
from langchain_helpers import generate_restaurant_idea_with_menu

st.title('Restaurant Idea Generator')

cuisine = st.selectbox('Select a cuisine', ['Italian', 'Japanese', 'Mexican',
                                            'Arabic', 'Indian', 'Pakistani', 'Chinese', 'Thai', 'Vietnamese', 'Korean', 'Turkish', 'Uzbik'])

if cuisine:
    response = generate_restaurant_idea_with_menu(cuisine)

    st.write(f'### Restaurant Name: :red[{response["restaurant_name"]}]')

    st.write('**Menu Items**')

    for item in response['menu_items'].strip().split(','):
        st.write('-', item)
