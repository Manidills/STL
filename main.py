import streamlit as st
import folium
from streamlit_folium import folium_static

# Set page configuration
st.set_page_config(page_title="Shanthi Transport & Logistics", page_icon="🚛", layout="wide")

# Increase font size for better readability
st.markdown("""
<style>
body {
    font-size: 60px;
}
</style>
""", unsafe_allow_html=True)

# Create columns for the logo and navigation
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://i.postimg.cc/52HShHb0/temp-Image-Rw-Qy-HQ.avif", width=250)

with col2:
    new_title = '<p style="font-family:cursive; color:#bfff00; font-size: 70px;">Shanthi Transport & Logistics</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    section = st.radio("Navigate to", ["Home", "Vision & Mission", "Business Locations", "Milestones", "Contact Us"], horizontal=True)

# Display content based on navigation choice
if section == "Home":
    st.markdown("## Welcome to Shanthi Transport & Logistics")
    st.markdown("""
    Shanthi Transport & Logistics (STL) is a leading logistics company committed to providing reliable and efficient transportation and logistics solutions across Tamil Nadu.
    With over seven years of experience, STL has established a vast network of operations that spans multiple companies, ensuring seamless connectivity and timely delivery of goods to various destinations.
    """)
    
    st.markdown("""
    Shanthi Transport & Logistics (STL) is a trusted name in logistics, known for its vast network and efficient service delivery across Tamil Nadu. 
    Our strong presence in major markets, including Trichy, Thanjavur, Thiruvarur, and Nagapattinam, ensures that we can meet the logistics needs of our clients promptly and effectively.
    """)


    st.markdown('<h2 style="color:#4CAF50;">Our Services</h2>', unsafe_allow_html=True)

    st.markdown("""
    At Shanthi Transport & Logistics, we offer a range of services to meet the diverse needs of our clients. Our focus is on enhancing efficiency, reducing costs, improving customer experience, and promoting sustainability in our logistics operations.

    ### Enhance Efficiency:
    - Utilize technology to optimize route planning, real-time tracking, and automated scheduling.
    - Implement advanced logistics management systems for seamless operations.

    ### Cost Reduction:
    - Minimize operational costs through automation and digital management tools.
    - Streamline processes to reduce overheads and improve profit margins.

    ### Customer Experience:
    - Offer a user-friendly platform for clients to manage and track shipments easily.
    - Provide 24/7 customer support to address any queries and concerns.

    ### Sustainability:
    - Implement eco-friendly practices and solutions within our logistics operations.
    - Invest in fuel-efficient vehicles and explore electric vehicle options for greener logistics.

    ### D2R Operations:
    - **Order Placements**: Seamless integration with clients' systems for efficient order placement.
    - **Order Processing**: Fast and accurate order processing to meet tight deadlines.
    - **Delivery Routing**: Optimized routing to ensure timely deliveries.
    - **Delivery Execution**: Professional execution of deliveries, ensuring customer satisfaction.

    With over 150 trucks running across Tamil Nadu, STL is equipped to handle large-scale logistics operations with precision and reliability.
    """)

    st.markdown("""
    ### Our Commitment:
    Shanthi Transport & Logistics has been a trusted name in logistics for seven years, delivering efficient, reliable, and cost-effective transport solutions. As part of our growth strategy, we continue to innovate and adapt to meet the evolving needs of our customers and the industry.
    """)



    st.markdown('<h2 style="color:#FF5733;">Our Clients</h2>', unsafe_allow_html=True)
    st.markdown("""
    We take pride in serving some of the most respected names in the industry. Our clients include:

    - <span style="color:#FF5733;">**Naga Pvt. Ltd.**</span>: Trusted partner for comprehensive logistics solutions.
    - <span style="color:#337AB7;">**Flipkart Internet Private Limited**</span>: Delivering excellence in e-commerce logistics.
    - <span style="color:#8E44AD;">**The Shadow Fax Corporation**</span>: Partnered for efficient logistics solutions.
    - <span style="color:#F39C12;">**B2C and B2B Logistic Solutions**</span>: Providing end-to-end logistics services for various businesses.
    """, unsafe_allow_html=True)

elif section == "Vision & Mission":
    with st.expander("Read more about our Vision & Mission"):
        st.markdown("## Vision & Mission")
        st.markdown("""
        ### Vision:
        Our vision is to make Shanthi Transport & Logistics the foremost choice for logistics services in the nation, offering unmatched solutions and exceptional delivery experiences. We aim to lead the industry by setting new standards in service quality, efficiency, and customer satisfaction.

        ### Mission:
        - To set the standard for quality in the logistics field through consistent demonstration of dependability, integrity, collaboration, innovation, and commitment to our stakeholders.
        - To explore the final leg of the delivery process, from the distribution center to the end customer, focusing on efficiency and customer satisfaction.
        - To continuously innovate and adapt to meet the evolving needs of our customers and the logistics industry.

        ### Core Values:
        - **Dependability**: We are committed to delivering on our promises and ensuring that our clients' goods reach their destinations safely and on time.
        - **Integrity**: We operate with transparency and honesty in all our dealings.
        - **Collaboration**: We believe in the power of teamwork and work closely with our clients to achieve shared goals.
        - **Innovation**: We embrace new technologies and ideas to stay ahead in the logistics industry.
        - **Commitment**: We are dedicated to providing the highest level of service to our clients.
        """)

elif section == "Business Locations":
    st.markdown("## Business Locations")

    # Map displaying business locations
    map_cities = folium.Map(location=[10.7905, 78.7047], zoom_start=8, control_scale=True)
    cities = {
        "Trichy": [10.7905, 78.7047],
        "Thanjavur": [10.7867, 79.1378],
        "Thiruvarur": [10.7731, 79.6361],
        "Nagapattinam": [10.7654, 79.8420],
        "Mayiladuthurai": [11.1034, 79.6552],
        "Kumbakonam": [10.9601, 79.3883],
    }

    for city, coords in cities.items():
        folium.Marker(location=coords, popup=city).add_to(map_cities)

    folium_static(map_cities, height=600)

    with st.expander("See detailed business locations"):
        st.markdown("""
        ### Locations Served:
        - **Naga Pvt. Ltd.**: Preambular, Trichy, Thanjavur, Thiruvarur, Nagapattinam, Mayiladuthurai
        - **Shadowbox**: Trichy
        - **Flipkart**: Kumbakonam
        - **Xpressbees**: Trichy
        - **Elasticrun**: Mayiladuthurai

        Our widespread network allows us to efficiently serve our clients across these key locations in Tamil Nadu.
        """)

elif section == "Milestones":
    st.markdown("## Milestones")
    with st.expander("View our milestones"):
        st.markdown("""
        Over the years, Shanthi Transport & Logistics has achieved several milestones, including:

        - **2017**: Established operations in Tamil Nadu with 10 trucks.
        - **2019**: Expanded the fleet to 50 trucks and partnered with major clients.
        - **2021**: Reached the milestone of 100 trucks and launched advanced logistics management systems.
        - **2023**: Achieved 150 trucks in operation and expanded services to new markets.
        """)

elif section == "Contact Us":
    st.markdown("## Contact Us")
    st.markdown("""
    Reach out to us for any inquiries or logistics solutions:

    - **Email**: shanthitransport.trichy@gmail.com
    - **Phone**: +91 9876543210
    - **Address**: 123 Logistics Street, Trichy, Tamil Nadu, India
    """)

    with st.expander("Send us a message"):
        st.text_area("Your message", height=100)
        if st.button("Send"):
            st.success("Your message has been sent!")

