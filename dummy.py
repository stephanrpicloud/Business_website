from streamlit_option_menu import option_menu
import streamlit as st
import base64

# Page configuration
st.set_page_config(page_title="SUNDARAM MEDICAL DEVICES",
                   page_icon='',
                   layout="wide")

# Add custom CSS for background image
@st.cache_resource
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg_and_style(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# Set background and header style
set_png_as_page_bg_and_style("pages/BG.jpg")

# Title
st.markdown(
    """
    <h1 style='text-align: center; color: black; font-size: 50px;'> Sundaram Medical Devices </h1>
    <h3 style='text-align: center; color: black; font-size: 30px;'> Your Health is Our Concern </h3>
    """,
    unsafe_allow_html=True
)

# Navigation menu
selected = option_menu(
    menu_title=None,
    options=["About us", "Our Products", "Contact"],
    icons=['info-circle', 'box-seam', 'envelope'],
    menu_icon=None,
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "background-color": "rgba(255, 255, 255, 0.2)",  # Light transparent background
            "padding": "10px",
            "border-radius": "15px",  # Smooth round edges
        },
        "nav-link": {
            "font-size": "20px",
            "color": "black",
            "background-color": "transparent",
            "border-radius": "20px",
        },
        "nav-link-selected": {
            "background-color": "#4CAF50",
            "color": "white",
            "border-radius": "20px",
            "box-shadow": "0px 0px 0px 3px rgba(255, 255, 255, 0.2)",
        },
    }
)

# About Us Section
if selected == "About us":
    cl1, cl2, cl3 = st.columns([1, 8, 1])
    with cl2:
        st.markdown(
            """
            <h2 style='font-size: 36px;'>A Few Words About Us</h2>
            <p style='font-size: 20px;'>Sundaram Surgical Group of Companies was established in the year 1987 by <b>Mr. R. Gnanaguru</b>.</p>
            <p style='font-size: 20px;'>We are manufacturers of <b>Surgical Dressings</b>, <b>Industrial Fabrics</b>, and <b>Cotton Fabrics</b> with over 35 years of experience.</p>
            <p style='font-size: 20px;'>We are a well-known company for surgical dressing items and other product lines.</p>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <h2 style='font-size: 36px;'>Our Infrastructure</h2>
            <p style='font-size: 20px;'>We own a spacious factory at Chatrapatti in Rajapalayam, Tamil Nadu, covering an area of <b>40,000 sq. ft.</b>.</p>
            <p style='font-size: 20px;'>Our products include:</p>
            <ul style='font-size: 20px;'>
                <li>Absorbent Gauze</li>
                <li>Bandage Cloth</li>
                <li>Roller Bandages</li>
                <li>Gauze Swabs</li>
                <li>Lap Sponges</li>
                <li>Gamjee Roll & Pad</li>
            </ul>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <h2 style='font-size: 36px;'>Our Commitment</h2>
            <p style='font-size: 20px;'>Our products are known for their:</p>
            <ul style='font-size: 20px;'>
                <li><b>Hygiene</b></li>
                <li><b>Safety</b></li>
                <li><b>Durability</b></li>
                <li><b>Reliability</b></li>
            </ul>
            """,
            unsafe_allow_html=True
        )

# Products Section
if selected == "Our Products":
    st.markdown(
        """
        <h1 style='text-align: center; color: black; font-size: 40px;'>Our Products</h1>
        <h2 style='text-align: center; font-size: 30px;'>Absorbent Gauze</h2>
        """,
        unsafe_allow_html=True,
    )
    cl1, cl2, cl3 = st.columns([1, 8, 1])
    with cl2:
        st.markdown(
            """
            <p style='font-size: 20px;'>With the support of our competent professionals, we offer a range of <b>Absorbent Gauze</b> developed from premium quality materials.</p>
            """,
            unsafe_allow_html=True,
        )
        st.image("pages/ABSORBENT GAUZE 1.png", caption="Absorbent Gauze", use_container_width=True)

# Contact Section
if selected == "Contact":
    st.markdown(
        """
        <h1 style='text-align: center; color: black; font-size: 40px;'>Contact Us</h1>
        """,
        unsafe_allow_html=True
    )
    cl1, cl2, cl3 = st.columns([1, 8, 1])
    with cl2:
        st.markdown(
            """
            <div style="font-size: 20px;">
                <b>Mfg. by :</b><br>
                <b>SUNDARAM MEDICAL DEVICES</b><br>
                8/162, J4, Meenakshiyapuram Main Road, Sankarapandiyapuram,<br>
                Chatrapatti - 626 102.<br>
                Via. Rajapalayam<br>
                <b>Contact :</b> 94431 57914<br>
                <b>E-mail :</b> sundarammedicaldevices@gmail.com<br>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Contact form
        contact_form = """
        <form action="https://formsubmit.co/sundarammedicaldevices@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# Ensure local CSS is used for contact form styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("contact form style/style.css")