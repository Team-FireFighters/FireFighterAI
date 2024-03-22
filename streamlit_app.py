import streamlit as st

def main():
    st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
    st.title("Fire Detection App")
    st.markdown(
        """
        Welcome to the Fire Detection App! This app helps in early detection of fires in prone regions 
        by utilizing  the satellite imagery and live camera feeds. Follow the steps below to use the app effectively:
        """
    )

    st.markdown(
        """
        ### Steps to Use the App:
        1. **Satellite Image Analysis:**
           - Navigate to the 'Satellite Image' page from the sidebar.
           - Upload a satellite image of a fire-prone region.
           - The app will process the image and detect if there are any fires present.

        2. **Fire Detection Model:**
           - Go to the 'Fire Detection Model' page from the sidebar.
           - Use the uploaded satellite image to run through the fire detection model.
           - The model will determine if there are any fire instances in the image.

        3. **Live Camera Feed Analysis:**
           - Proceed to the 'Live Camera Feed' page from the sidebar.
           - Access the live camera feed of the region.
           - The app will analyze the live feed for any signs of fire using the same model.
           - If fire is detected, the app will inform local authorities automatically.

        Please proceed to the respective pages to utilize the functionalities of the app.
        """
    )

if __name__ == "__main__":
    main()
