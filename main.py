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
    <h1 style='text-align: center; color: black;'> Sundaram Medical Devices </h1>
    <h3 style='text-align: center; color: black;'> Your Health is Our Concern </h3>
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
            "font-size": "18px",
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
        # Header
        st.markdown(
            "<h1 style='text-align: center; font-size: 36px;'>A Few Words About Us</h1>", 
            unsafe_allow_html=True
        )
        
        # About Us
        st.markdown(
            """
            <p style='font-size: 20px;'>
            Sundaram Surgical Group of Companies was established in the year 1987 by <b>Mr. R. Gnanaguru</b>.<br>
            We are manufacturers of <b>Surgical Dressings</b>, <b>Industrial Fabrics</b>, and <b>Cotton Fabrics</b> with over 35 years of experience.<br>
            As per the Central Government's Order, we follow the Medical Devices Rules and operate under the name Sundaram Medical Devices.<br>
            We are a well-known company for surgical dressing items and other product lines.
            </p>
            """, 
            unsafe_allow_html=True
        )

        # Infrastructure
        st.markdown(
            "<h2 style='font-size: 28px;'>Our Infrastructure</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style='font-size: 20px;'>
            We own a spacious factory at Chatrapatti in Rajapalayam, Tamil Nadu, covering an area of <b>40,000 sq. ft.</b>.<br>
            We have incorporated world-class production methodologies, ensuring efficient production.<br>
            Our manufacturing unit has a production capacity of <b>1,000,000 meters</b>.<br>
            Our products include:
            </p>
            <ul style='font-size: 25px;'>
                <li>Absorbent Gauze</li>
                <li>Bandage Cloth</li>
                <li>Roller Bandages</li>
                <li>Gauze Swabs</li>
                <li>Cut Gauze</li>
                <li>Lap Sponges</li>
                <li>Gauze Roll</li>
                <li>Gamjee Roll & Pad</li>
                <li>Combine Dressing Pad</li>
                <li>4-Ply Roll</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )

        # Team
        st.markdown(
            "<h2 style='font-size: 28px;'>Our Team</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style='font-size: 20px;'>
            Our team comprises Management & Administration Professionals, Quality Analysts, Sales Executives, Weavers, and other Workmen.<br>
            With their constant efforts, we manufacture high-quality products using 100% pure cotton raw materials for medical industries.
            </p>
            """, 
            unsafe_allow_html=True
        )

        # Process
        st.markdown(
            "<h2 style='font-size: 28px;'>Our Process</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style='font-size: 20px;'>
            We procure premium quality cotton yarns from reliable vendors and spinning mills.<br>
            The material undergoes several processes, including:
            </p>
            <ul style='font-size: 20px;'>
                <li><b>Warping & Sizing</b> using advanced warp-knitted machines for efficient processing.</li>
                <li><b>Weaving</b> for both industrial fabrics and medical gauzes.</li>
                <li><b>Bleaching</b> as per the Pharmacopoeia Standard, ensuring the cloth remains untouched by hand throughout.</li>
                <li><b>Drying</b> to achieve the desired finished product.</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )

        # Innovation & Quality
        st.markdown(
            "<h2 style='font-size: 28px;'>Innovation & Quality</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style='font-size: 20px;'>
            We continuously implement the latest technologies and methodologies to create innovative, durable, and safe products.<br>
            Backed by a full-fledged R&D unit, our comprehensive product collection meets the needs of:
            </p>
            <ul style='font-size: 20px;'>
                <li>Healthcare</li>
                <li>Industries</li>
                <li>Wholesale Sellers</li>
            </ul>
            """, 
            unsafe_allow_html=True
        )

        # Commitment
        st.markdown(
            "<h2 style='font-size: 28px;'>Our Commitment</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style='font-size: 20px;'>
            Our products are well-known for their:
            </p>
            <ul style='font-size: 20px;'>
                <li><b>Hygiene</b></li>
                <li><b>Safety</b></li>
                <li><b>Durability</b></li>
                <li><b>Reliability</b></li>
            </ul>
            """, 
            unsafe_allow_html=True
        )

if selected == "Our Products":

    # Helper function for spacing
    def add_spacing(height):
        st.markdown(f"<div style='height: {height}px;'></div>", unsafe_allow_html=True)

    # Header for each product
    def render_product_header(title):
        st.markdown(f"<h1 style='text-align: center; color: black; font-size: 36px;'>{title}</h1>", unsafe_allow_html=True)
        add_spacing(50)

    # First Product: ABSORBENT GAUZE
    render_product_header("ABSORBENT GAUZE")

    cl1, cl2, cl3 = st.columns([1, 8, 1])
    with cl2:
        col1, col2, col3 = st.columns(3)
        with col3:
            st.image("pages/ABSORBENT GAUZE 1.png", caption="Absorbent Gauze", use_container_width=True)
        with col2:
            st.image("pages/ABSORBENT GAUZE 2.png", caption="Bandage Cloth", use_container_width=True)
        with col1:
            st.markdown(
                """
                <p style='font-size: 20px;'>
                With the support of our competent professionals, we are instrumental in offering a vast range of 
                <b>Absorbent Gauze</b> that is developed from premium quality materials.
                </p>
                """, unsafe_allow_html=True
            )
            st.markdown("**Applications**", unsafe_allow_html=True)
            st.markdown(
                """
                <ul style='font-size: 20px;'>
                    <li>For wound care, wound cleaning, and dressing.</li>
                </ul>
                """, unsafe_allow_html=True
            )
            st.markdown("**Sizes** (Sterile / Non Sterile):", unsafe_allow_html=True)
            st.markdown(
                """
                <p style='font-size: 20px;'>
                - Width: 80 cm / 90 cm / 100 cm / 120 cm / 130 cm<br>
                - Length: 10 mtr / 16 mtr / 18 mtr / 20 mtr / 100 mtr / 2000-3000 mtr (Jumbo Roll)
                </p>
                """, unsafe_allow_html=True
            )
            st.markdown("**Product Details:**", unsafe_allow_html=True)
            st.markdown(
                """
                <ul style='font-size: 20px;'>
                    <li>Simple to use</li>
                    <li>Hygienically processed</li>
                    <li>Soft texture</li>
                    <li>High performance</li>
                    <li>Affordable rates</li>
                    <li>Highly durable</li>
                </ul>
                """, unsafe_allow_html=True
            )

    add_spacing(50)

    # Second Product: GAUZE SWABS
    render_product_header("GAUZE SWABS")

    cl1, cl2, cl3 = st.columns([1, 8, 1])
    with cl2:
        col1, col2, col3 = st.columns([6, 1, 8])
        with col1:
            st.image("pages/SWABS (STERILIE 5 PCS) .png", caption="Gauze Swab", use_container_width=True)
        with col3:
            add_spacing(80)
            st.markdown(
                """
                <p style='font-size: 20px;'>
                The <b>gauze swab</b> offered by us is a sponge of <b>8 ply</b> that contains 8 layers of highly absorbent cotton gauze.
                It is appreciated for its high tending capacity and faster rate of absorption.
                </p>
                """, unsafe_allow_html=True
            )
            st.markdown("**Features**", unsafe_allow_html=True)
            st.markdown(
                """
                <ul style='font-size: 20px;'>
                    <li>Made by 100% absorbent cotton cloth.</li>
                    <li>Bleached to a good white.</li>
                    <li>Highly absorbent and highly volume retention.</li>
                    <li>Clean, odourless, free from weaving defects.</li>
                </ul>
                """, unsafe_allow_html=True
            )

    add_spacing(50)

    # Continue adding remaining products in the same style
    # For each product:
    # 1. Use `render_product_header("Product Name")` for the title.
    # 2. Use consistent spacing, image placement, and styled text using HTML.

    # Example for one more product:
    render_product_header("ROLLER BANDAGE")
    
    cl1, cl2, cl3 = st.columns([1, 8, 1])
    with cl2:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("pages/ROLLER BANDAGE 1.png", caption="ROLLER BANDAGE", use_container_width=True)
        with col2:
            add_spacing(190)
            st.image("pages/ROLLER BANDAGE 2.png", caption="ROLLER BANDAGE", use_container_width=True)
        with col3:
            st.image("pages/ROLLER BANDAGE 3.png", caption="ROLLER BANDAGE", use_container_width=True)

            st.markdown("### Product Description:", unsafe_allow_html=True)
            st.markdown(
                """
                <p style='font-size: 20px;'>
                Owing to our huge proficiency in this domain, we are affianced in offering a broad range of <b>Rolled Gauze / Bandage</b>.
                </p>
                """, unsafe_allow_html=True
            )
            st.markdown("### Rolled Gauze / Bandage:", unsafe_allow_html=True)
            st.markdown(
                """
                <ul style='font-size: 20px;'>
                    <li>Hygienically developed with high precision</li>
                    <li>Reasonable rates</li>
                    <li>Safely packed</li>
                    <li>Longer shelf life</li>
                </ul>
                """, unsafe_allow_html=True
            )
            st.markdown("### Product Details:", unsafe_allow_html=True)
            st.markdown(
                """
                <ul style='font-size: 20px;'>
                    <li>Safe to use</li>
                    <li>Light weight</li>
                    <li>Highly effective</li>
                </ul>
                """, unsafe_allow_html=True
            )

    # Add download button for catalogue at the end
    catalogue_pdf = "Catalouge.pdf"
    with open(catalogue_pdf, "rb") as file:
        pdf_data = file.read()

    add_spacing(200)

    st.download_button(
        label="Download Catalogue",
        data=pdf_data,
        file_name="Catalouge.pdf",
        mime="application/pdf",
    )

if selected == "Contact":
    st.markdown(
        """
        <h1 style='text-align: center; color: black;'>Contact Us</h1>
        """,
        unsafe_allow_html=True,
    )

    cl1, cl2, cl3 = st.columns([1, 5, 1])  # Adjust column widths for alignment
    with cl2:
        col1,col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div style="font-family: Serif; font-size: 18px; line-height: 1.8;">
                    <b>Mfg. by :</b> <br>
                    <b>SUNDARAM MEDICAL DEVICES</b> <br>
                    8/162, J4, Meenakshiyapuram Main Road, <br>
                    Sankarapandiyapuram, Chatrapatti - 626 102. <br>
                    Via. Rajapalayam <br>
                    <b>Contact :</b> 94431 57914 <br>
                    <b>E-mail :</b> sundarammedicaldevices@gmail.com <br>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-family: Serif; font-size: 18px; line-height: 1.8;">
                    <b>Contact Person :</b> G. Muthu <br>
                    <b>Customer Care :</b> 94431 57914 <br>
                    <b>Office :</b> 04563 - 257 302, 258 302, 257 805 <br>
                    <b>Mob :</b> 94431 57914, 94431 57302
                </div>
                """,
                unsafe_allow_html=True,
            )

    cl1, cl2, cl3 = st.columns([1, 5, 1])

    with cl2:
        st.header(":mailbox: Get In Touch With Us!")


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

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("contact form style/syle.css")        