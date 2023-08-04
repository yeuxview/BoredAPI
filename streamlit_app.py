import streamlit as st
from utils import Bored_APIConnection

# Create the Bored API connection
bored_conn = st.experimental_connection("bored", type=Bored_APIConnection)

# Streamlit app
def main():
    st.title("🥱BoredAPI Connection with Streamlit")

    st.markdown(
        """
        Bored? 
        
        Query the BoredAPI and get something to do.

        Yes, thats it.
        """
    )

    selected_option = st.selectbox("What would you like to do?", ["Select here.", "Random Activity!", "Customize Activity"])

    if(selected_option == 'Random Activity!'):
        if(st.button("Fetch Activities!")):
            response = bored_conn.query_any_activity()
            st.write("Here's your activity:")
            st.title(response)

    elif(selected_option == "Customize Activity"):
        accessibility = st.slider(
        'Select a range of accessibility (0 being most accessible, 1 being least)',
            0.0, 1.0, (0.0, 1.0))

        prices = st.slider(
        'Select a range of prices (0 being free, 1 being expensive)',
            0.0, 1.0, (0.0, 1.0))

        types = st.multiselect(
            'Select types of activities that you want:',
            ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

        participants = st.number_input(label="Participants:", value=1)
        
        if(len(types) != 0):
            if(st.button("Fetch Activities!")):
                activities = bored_conn.query_specific_activity(accessibility, prices, types, participants)
                st.write("Here's your activities:")
                for _ in activities:
                    st.title(_)


if __name__ == "__main__":
    main()
