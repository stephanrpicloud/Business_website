from streamlit_option_menu import option_menu 
import streamlit as st 
import base64
import os

# Configure dynamic port for hosting platforms
if "PORT" in os.environ:
    port = int(os.environ.get("PORT"))
    os.environ["STREAMLIT_SERVER_PORT"] = str(port)  # Set the port for Streamlit


# Page configuration
st.set_page_config(page_title="SUNDARAM MEDICAL DEVICES",
                   page_icon='🩺',
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
set_png_as_page_bg_and_style(os.path.join(os.getcwd(), "pages/BG.jpg"))


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
            <ul style='font-size: 20px;'>
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
    #1st ABSORBENT GAUZE

    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> ABSORBENT GAUZE </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    with cl2:
        col1, col2, col3 = st.columns(3)
    with col3:
        st.image(os.path.join(os.getcwd(), "pages/ABSORBENT GAUZE 1.png"), caption="Absorbent Gauze", use_container_width=True)
    with col2:
        st.image(os.path.join(os.getcwd(), "pages/ABSORBENT GAUZE 2.png"), caption="Bandage Cloth", use_container_width=True)
    with col1:
        st.write(
            """
            With the support of our competent professionals, we are instrumental in offering a vast range of **Absorbent Gauze** that is developed from premium quality materials.
            """
        )

        st.markdown("**Applications**")
        st.write(
            """
            - For wound care, wound cleaning, and dressing.
            """
        )

        st.markdown("**Sizes** (Sterile / Non Sterile):")
        st.write(
            """
            - Width: 80 cm / 90 cm / 100 cm / 120 cm / 130 cm  
            - Length: 10 mtr / 16 mtr / 18 mtr / 20 mtr / 100 mtr / 2000-3000 mtr (Jumbo Roll)
            """
        )

        st.markdown("**Product Details:**")
        st.write(
            """
            - Simple to use  
            - Hygienically processed  
            - Soft texture  
            - High performance  
            - Affordable rates  
            - Highly durable  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #2nd SWABS (STERILIE 5 PCS)

    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> GAUZE SWABS </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    with cl2:
        col1, col2, col3 = st.columns([6,1,8])
    with col1:
        st.image(os.path.join(os.getcwd(), "pages/SWABS (STERILIE 5 PCS) .png"), caption="Gauze Swab",use_container_width=True)
    with col3:
        
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

        st.write(
            """
            The **gauze swab** offered by us is a sponge of **8 ply** that contains 8 layers of highly absorbent cotton gauze. 
            It is appreciated for its high tending capacity and faster rate of absorption.
            """
        )

        st.markdown("**Features**")
        st.write(
            """
            - Made by 100% absorbent cotton cloth.  
            - Bleached to a good white.  
            - Highly absorbent and highly volume retention.  
            - Clean, Odourless, Free from weaving defects.
            """
        )
    
    #3rd STERILE

    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> STERILE </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    with cl2:
        col1, col2, col3 = st.columns(3)
    with col2:
        st.image(os.path.join(os.getcwd(), "pages/STERILE.png"), caption="Absorbent Gauze", use_container_width=True)
    with col3:
        st.image(os.path.join(os.getcwd(), "pages/STERILE 2.png"), caption="Bandage Cloth", use_container_width=True)
    with col1:
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        st.markdown("**Applications**")
        
        st.write(
            """
            - For wound care, wound cleaning and dressing.
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #4th ROLLER BANDAGE
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> ROLLER BANDAGE </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    with cl2:
        col1, col2, col3 = st.columns(3)
    with col1:
        st.image(os.path.join(os.getcwd(), "pages/ROLLER BANDAGE 1.png"), caption="ROLLER BANDAGE", use_container_width=True)
    with col2:
        st.markdown("<div style='height: 190px;'></div>", unsafe_allow_html=True)
        st.image(os.path.join(os.getcwd(), "pages/ROLLER BANDAGE 2.png"), caption="ROLLER BANDAGE", use_container_width=True)
    with col1:
        st.image(os.path.join(os.getcwd(), "pages/ROLLER BANDAGE 3.png"), caption="ROLLER BANDAGE", use_container_width=True)
    with col3:
        
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        st.markdown("### Product Description:")
        st.write(
            """
            Owing to our huge proficiency in this domain, we are affianced in offering a broad range of **Rolled Gauze / Bandage**.
            """
        )

        st.markdown("### Rolled Gauze / Bandage:")
        st.write(
            """
            - Hygienically developed with high precision  
            - Reasonable rates  
            - Safely packed  
            - Longer shelf life  
            """
        )

        st.markdown("### Product Details:")
        st.write(
            """
            - Safe to use  
            - Light weight  
            - Highly effective  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    #5th ABDOMINAL PAD / MOPPING PAD (NON STERILE & STERILE 5 PCS)
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> ABDOMINAL PAD / MOPPING PAD </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2 = st.columns(2)
    
    with col2:
        
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        st.image(os.path.join(os.getcwd(), "pages/ABDOMINAL PAD : MOPPING PAD.png"), caption="ABDOMINAL PAD / MOPPING PAD", use_container_width=True)
    
    with col1:
        # Description Section
        st.markdown("### Product Description:")
        st.write(
            """
            Being an esteemed organization, we are engrossed in offering a wide range of **Abdominal Gauze Swab** 
            that is available as per the clients' requirements.
            """
        )

        # Product Details Section
        st.markdown("### Product Details:")
        st.write(
            """
            - **Highly absorbent**  
            - **Hygienic**  
            - **Longer shelf life**  
            - **Safe to use**  
            - **Purity**  
            - **Smooth texture**  
            """
        )

        # Applications Section
        st.markdown("### Applications:")
        st.write(
            """
            - For bleeding control during operation/surgery.
            """
        )

        # Sizes Section
        st.markdown("### Sizes (Sterile / Non Sterile):")
        st.write(
            """
            - 25 cm X 25 cm / 6 ply / 8 ply / 12 ply  
            - 25 cm X 40 cm / 6 ply / 8 ply / 12 ply  
            - 30 cm X 30 cm / 6 ply / 8 ply / 12 ply  
            """
        )

        # Specifications Section
        st.markdown("### Specifications:")
        st.write(
            """
            - High absorbency and high retention.  
            - Made up of 100% cotton bleached to good white.  
            - Sturdy cotton loop at one corner for easy location and retrieval during surgery.  
            - Interlocked edges to avoid open/loose threads.  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #6th CANNULA FIXATOR
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> CANNULA FIXATOR </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2 = st.columns(2)
    
    with col1:

        #st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/CANNULA FIXATOR.png"), caption="CANNULA FIXATOR", use_container_width=True)
    
    with col2:
        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - Low allergy grid pattern adhesive.  
            - Porous adhesive to allow skin breathing.  
            - Easy & painless removal.  
            - Non-irritating material towards skin.  
            - Available in standard sizes suitable for each type of patient.  
            """
        )

        # Relifix Benefits Section
        st.markdown("### Relifix:")
        st.write(
            """
            - Fixed without contaminating the infusion site.  
            - Fixes the cannula and prevents pain.  
            - Prevents infusion-related phlebitis.  
            """
        )

        # Additional Features Section
        st.markdown("### Additional Features:")
        st.write(
            """
            - Safe to use  
            - Superior finish  
            - Soft texture  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)    
    
    #7th DRESSING PAD / COMBINE DRESSING PAD
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> DRESSING PAD / COMBINE DRESSING PAD </h1>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2 = st.columns(2)
    
    with col2:

        #st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/DRESSING PAD : COMBINE DRESSING PAD.png"), caption="DRESSING PAD / COMBINE DRESSING PAD", use_container_width=True)
    
    with col1:
        # Product Description
        st.markdown("### Product Description:")
        st.write(
            """
            Combine Dressing Pads are sterilized, ready-to-use surgical dressing pads available in different sizes.  
            They consist of absorbent cotton wool I.P wrapped in a highly absorbent viscose layer.  
            Soft and comfortable wound dressing designed for exudating wounds.
            """
        )

        # Specifications
        st.markdown("### Specifications:")
        st.write(
            """
            - Sterile and ready to use for all surgery.  
            - Excellent post-operative care with a high level of absorbency and retention of fluids.  
            - Minimal dressing changes reduce patient trauma.  
            - Soft and conforming to the contours of the body; anti-allergic and non-irritating to the skin.  
            - Individually packed in tamper-proof wraps.  
            - Available sizes: 10cm × 10cm & 10cm × 20cm.  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    #8th ELASTIC ADHESIVE BANDAGE & CREPE BANDAGE
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> ELASTIC ADHESIVE BANDAGE & CREPE BANDAGE PAD </h1>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2 = st.columns(2)
    
    with col1:

        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/ELASTIC ADHESIVE BANDAGE & CREPE BANDAGE.png"), caption="ELASTIC ADHESIVE BANDAGE & CREPE BANDAGE", use_container_width=True)
    
    with col2:
        # Characteristics Section
        st.markdown("### Characteristics:")
        st.write(
            """
            - Better elasticity allows free muscle and joint movement.  
            - Better aesthetic touch due to interlocking.  
            - Easy & painless removal.  
            """
        )

        # Applications Section
        st.markdown("### Applications:")
        st.write(
            """
            - Provides great support, immobilization, and pressure, where required.  
            """
        )

        # Packing Section
        st.markdown("### Packing:")
        st.write(
            """
            - 10 cm x 4/6 mtr (Stretched).  
            - 8 cm x 4/6 mtr (Stretched).  
            - 6 cm x 4/6 mtr (Stretched).  
            - 10 cm x 1 mtr (Stretched).  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #9th GAMJEE ROLL / PAD
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> GAMJEE ROLL / PAD </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2,col3 = st.columns(3)
    
    with col3:

        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/GAMJEE ROLL : PAD.png"), caption="GAMJEE ROLL / PAD", use_container_width=True)
    
    with col2:

        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/GAMJEE ROLL : PAD 2.png"), caption="GAMJEE ROLL / PAD", use_container_width=True)
    
    with col1:
        
        #st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - Highly absorbent and insulated.  
            - Also applied over the dressing to hold the bandaging point.  
            - Promotes the healing of wounds.  
            - Skin-friendly.  
            """
        )

        # Characteristics Section
        st.markdown("### Characteristics:")
        st.write(
            """
            - Made from superior cotton.  
            - Absorption rate faster (less than 10 seconds).  
            - Better tending capacity.  
            - Less allegiance to healing tissue.  
            """
        )

        # Applications Section
        st.markdown("### Applications:")
        st.write(
            """
            - For swabbing and cleaning wounds.  
            - For dressing low exudate wounds.  
            """
        )

        # Product Packing Section
        st.markdown("### Product Packing:")
        st.write(
            """
            - 10 cm X 3 mtr.  
            - 15 cm X 3 mtr.  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #10th SOFT ROLL / ORTHO CAST PADDING
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> SOFT ROLL / ORTHO CAST PADDING </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2, col3 = st.columns(3)
    
    with col1:

        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/SOFT ROLL : ORTHO CAST PADDING.png"), caption="SOFT ROLL / ORTHO CAST PADDING", use_container_width=True)
    
    with col2:

        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/SOFT ROLL : ORTHO CAST PADDING 2.png"), caption="SOFT ROLL / ORTHO CAST PADDING", use_container_width=True)
    
    with col3:
        
        #st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - Uniform thickness throughout the width and length.  
            - Acts as a cushion and provides maximum protection in the plaster.  
            - Permeable to air. Avoids chances of skin irritation and maceration.  
            - Gives excellent skin tolerance and easy body movements.  
            - Perfectly conforms to your body contours (curves).  
            - Reduces chances of pressure sores in your body.  
            """
        )

        # Applications Section
        st.markdown("### Applications:")
        st.write(
            """
            - Used before application of any type of bandages to protect the skin.  
            - Can be used as a leg roll, long sponges, etc.  
            - For sensitive and tender skin. Protects bony prominence.  
            - Used where swelling is expected.  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    #11th ABSORBENT COTTON WOOL / ZIG ZAG COTTON
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> SOFT ABSORBENT COTTON WOOL / ZIG ZAG COTTON </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2, col3 = st.columns(3)
    
    with col3:

        st.markdown("<div style='height: 250px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/ABSORBENT COTTON WOOL 1.png"), caption="ABSORBENT COTTON WOOL / ZIG ZAG COTTON", width = 500 )
    
    with col2:

        #st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/ABSORBENT COTTON WOOL 2.png"), caption="ABSORBENT COTTON WOOL / ZIG ZAG COTTON", width = 250 )
    
    with col1:
        
        #st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

        # Product Description
        st.markdown("### Product Description:")
        st.write(
            """
            We are a reputed entity in the industry, actively engaged in offering an optimum quality range of **Absorbent Cotton Wool I.P.**
            """
        )

        # Details Section
        st.markdown("### Detail:")
        st.write(
            """
            - This cotton wool is not sterilized, so it needs to be sterilized before use.
            """
        )

        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - High fluid absorbency  
            - Fine finish  
            - Optimum softness  
            - Smooth texture  
            - Light weight  
            - High absorbent, pure white cotton  
            - Premium quality  
            - **Caution:** To be sterilized before use  
            """
        )

        # Specifications Section
        st.markdown("### Specifications:")
        st.write(
            """
            - Gross / Nett weight: 25 g / 50 g / 100 g / 200 g / 300 g / 400 g / 500 g  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)


    #12th COTTON BALL
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> COTTON BALL </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2 = st.columns(2)
    
    with col1:

        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/COTTON BALL.png"), caption="COTTON BALL", width = 500 )
    
    with col2:
        
        #st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

        # Product Description
        st.markdown("### Product Description:")
        st.write(
            """
            With our in-depth knowledge of this domain, we are actively engaged in manufacturing and supplying an excellent quality range of **Zig Zag Cotton Wool.**
            """
        )

        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - Softness  
            - Light weight  
            - Free from dirt  
            - **Size:** 200 g / 400 g / 500 g  
            """
        )

        # Use Section
        st.markdown("### Use:")
        st.write(
            """
            - Used in hospitals and healthcare services for dressing cuts and wounds.  
            - Soft & absorbent.  
            - Neutral pH.  
            - H₂O₂ bleached for extra whiteness.  
            - Multipurpose.  
            """
        )

        # Size Section
        st.markdown("### Size:")
        st.write(
            """
            - 50 Pcs. Per Packet  
            - 100 Pcs. Per Packet  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #13th EXAMINATION GLOVES
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> EXAMINATION GLOVES </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2 = st.columns(2)
    
    with col2:

        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/EXAMINATION GLOVES.png"), caption="EXAMINATION GLOVES", width = 500 )
    
    with col1:
        
        #st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

        # Type Section
        st.markdown("### Type:")
        st.write(
            """
            - Disposable
            """
        )

        # Material Section
        st.markdown("### Material:")
        st.write(
            """
            - Made from latex rubber
            """
        )

        # Color Section
        st.markdown("### Color:")
        st.write(
            """
            - Creamy white
            """
        )

        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - Smooth surface pattern  
            - Greater sensitivity  
            """
        )

        # Application Section
        st.markdown("### Application:")
        st.write(
            """
            - Suitable for pharmaceuticals, packaging laboratories, etc.  
            """
        )

        # Available Size Section
        st.markdown("### Available Sizes:")
        st.write(
            """
            - Small
            - Medium
            - Large  
            """
        )
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #14th DIALYSIS KIT / DRESSING KIT
    
    st.markdown(
    """
    <h1 style='text-align: center; color: black;'> DIALYSIS KIT / DRESSING KIT </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    cl1,cl2,cl3 = st.columns([1,8,1])
    
    with cl2:
        col1, col2, col3 = st.columns(3)
    
    with col1:

        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/DIALYSIS KIT : DRESSING KIT.png"), caption="DIALYSIS KIT / DRESSING KIT", use_container_width= True)
    
    with col2:

        st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)
        
        st.image(os.path.join(os.getcwd(), "pages/DIALYSIS KIT : DRESSING KIT 2.png"), caption="DIALYSIS KIT / DRESSING KIT", use_container_width = True )

    with col3:

        # Product Description
        st.markdown("### Product Description:")
        st.write(
            """
            With the experience of many years behind us, we offer our valued client base with **Hospital Kits** like Dressing Kit, Dialysis Kit, HIV Kit, etc.  
            These kits are used to protect doctors from viral infections transmitted from infected patients, as well as to shield them from any contagious diseases.  
            The kits are quality-tested to ensure high-quality products are delivered to the customers.  

            Widely used in:
            - Hospitals  
            - Nursing homes  
            - Clinics  

            The product is packed using high-quality packaging material to ensure its safe delivery to the customer’s end.
            """
        )

        # Features Section
        st.markdown("### Features:")
        st.write(
            """
            - Sterilized  
            - Skin-friendly  
            - High quality  
            - Reliable  
            - Affordable price  
            """
        )

    # File path to your PDF
    catalogue_pdf = "Catalouge.pdf"

    # Read the PDF file in binary mode
    with open(catalogue_pdf, "rb") as file:
        pdf_data = file.read()

    # Add a download button
    cl1,cl2,cl3 = st.columns([1,8,1])
    with cl2:

        st.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

        st.download_button(
            label="Download Catalogue",
            data=pdf_data,
            file_name="Catalouge.pdf",
            mime="application/pdf"
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
        st.markdown(
            """
            <div style="font-family: Serif; font-size: 18px; line-height: 1.8;">
                <b>Mfg. by :</b> <br>
                <b>SUNDARAM MEDICAL DEVICES</b> <br>
                8/162, J4, Meenakshiyapuram Main Road, <br>
                Sankarapandiyapuram, Chatrapatti - 626 102. <br>
                Via. Rajapalayam <br>
                <b>Contact Person :</b> G. Muthu <br>
                <b>Contact :</b> 94431 57914 <br>
                <b>E-mail :</b> sundarammedicaldevices@gmail.com <br>
            </div>
            """,
            unsafe_allow_html=True,
        )
            
    cl1, cl2, cl3 = st.columns([1, 5, 1])

    with cl2:
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
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


        local_css(os.path.join(os.getcwd(), "contact form style", "style.css"))