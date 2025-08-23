import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import base64
import time
import datetime

st.set_page_config(page_title="EV Revolution", page_icon="🔋", layout="wide", initial_sidebar_state="collapsed")

# Function to convert video to base64
@st.cache_data
def get_video_base64(video_path):
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    return base64.b64encode(video_bytes).decode()

# Hide sidebar and style tabs
st.markdown("""
<style>
    .css-1d391kg {display: none}
    .css-1rs6os {display: none}
    .css-17eq0hr {display: none}
    
    /* Force viewport height */
    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh !important;
        overflow: hidden !important;
    }
    
    /* Reduce main container padding */
    .main .block-container {
        padding: 0.2rem 0.5rem !important;
        max-width: 100% !important;
        height: 95vh !important;
        overflow-y: auto !important;
    }
    
    /* Reduce all element spacing */
    .element-container {
        margin-bottom: 0.1rem !important;
    }
    
    /* Reduce headings */
    h1, h2, h3 {
        margin-top: 0.2rem !important;
        margin-bottom: 0.2rem !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
        margin-bottom: 0.2rem !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border: 2px solid;
    }
    
    .stTabs [data-baseweb="tab"] button,
    .stTabs [data-baseweb="tab"] button div,
    .stTabs [data-baseweb="tab"] button p,
    .stTabs [data-baseweb="tab"] * {
        font-size: 16px !important;
        font-weight: normal !important;
    }
    
    .stTabs [data-baseweb="tab"]:nth-child(1) {
        background-color: #FF9900;
        border-color: #FF9900;
        color: white;
    }
    
    .stTabs [data-baseweb="tab"]:nth-child(2) {
        background-color: #F5F5F5;
        border-color: #F5F5F5;
        color: #333;
    }
    
    .stTabs [data-baseweb="tab"]:nth-child(3) {
        background-color: #F5F5F5;
        border-color: #F5F5F5;
        color: #333;
    }
    
    .stTabs [data-baseweb="tab"]:nth-child(4) {
        background-color: #F5F5F5;
        border-color: #F5F5F5;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# Create tabs with colored backgrounds
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Amazon EV", "EV Analytics", "EVBot"])

with tab1:
    # Get video as base64
    try:
        video_base64 = get_video_base64("vecteezy_roadside-charging-station-with-an-ev-car-and-natural_49116874_956.mov.mp4")
        
        # Rectangle container with video background and title
        st.markdown(f"""
        <div style="position: relative; width: 100%; height: 400px; border-radius: 15px; overflow: hidden; margin-bottom: 30px;">
            <video autoplay muted loop playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; z-index: 10;">
                <h1 style="color: white; font-size: 3rem; margin-bottom: 15px; text-shadow: 3px 3px 6px rgba(0,0,0,0.9); font-weight: bold;">The Evolution of EV</h1>
                <p style="color: white; font-size: 1.3rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.9);">Powering a sustainable tomorrow</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback if video file not found
        st.markdown("""
        <div style="position: relative; width: 100%; height: 400px; border-radius: 15px; overflow: hidden; margin-bottom: 30px; background: linear-gradient(135deg, #FF9900, #FF6600);">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; z-index: 10;">
                <h1 style="color: white; font-size: 3rem; margin-bottom: 15px; text-shadow: 3px 3px 6px rgba(0,0,0,0.9); font-weight: bold;">The Evolution of EV</h1>
                <p style="color: white; font-size: 1.3rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.9);">powering a sustainable tomorrow</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.warning("Video file not found. Showing gradient background instead.")
    
    # Welcome content - Section 1
    st.markdown("## Welcome to the Future of Motion: Where Electric Dreams Take Flight!")
    
    # Welcome content - Section 2
    st.markdown("""
    Step into a world where innovation meets sustainability, where the whisper of electric motors harmonizes with nature's breath. Our interactive journey through the electric vehicle revolution isn't just about transportation—it's about transformation. Picture cities where children draw blue skies without grey clouds, where the morning commute sounds like gentle breeze, and where every journey writes a new chapter in Earth's recovery story.
    """)
    
    # Welcome content - Section 3
    st.markdown("""
    But here's what makes this tale extraordinary: The electric vehicle isn't a modern invention born in sleek Silicon Valley laboratories. It's a phoenix rising from the pages of history, a brilliant idea that waited nearly two centuries for humanity to catch up with its potential. From humble beginnings in the 1830s to today's cutting-edge marvels, this is perhaps technology's greatest comeback story—a renaissance powered by human ingenuity and planetary purpose.
    """)
    
    # Two containers - left with content, right with image (2:1 ratio)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="background-color: #F5F5F5; padding: 20px; border-radius: 15px; color: #333;">
            <h3 style="color: #333; margin-bottom: 10px; font-size: 32px;"> 🤯 Did you know EVs are 200 years old?!</h3>
            <p style="margin-bottom: 8px;">
            Hold onto your charging cables! The first electric vehicle was not born in Silicon Valley or some futuristic lab, Nope!
            It rolled onto the scene way back in 1828 - that's almost 200 years ago!
            </p>
            <p style="margin-bottom: 8px;">
            Hungarian genius Ányos Jedlik started the spark in 1828 with his electric motor and model car. Then Scottish inventor Robert Anderson really got things rolling between 1832-1839 with his crude electric carriage - talk about being current with the times!😉
            </p>
            <p style="margin-bottom: 8px;">
            But here's the shocking truth: these early EVs were powered by non-rechargeable batteries. Imagine buying a new "battery pack" every time your car died! No wonder it took us TWO CENTURIES to get our act together and realize they were onto something electrifying! Better late than never, right? 
            </p><p style="margin-bottom: 0px;">Sometimes the best ideas just need time to... recharge!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://cdn.cnn.com/cnn/interactive/2019/07/business/electric-car-timeline/media/1884.jpg", 
                 use_container_width=True)
    
    # Amazon dark blue container
    st.markdown("""
    <div style="background-color: #232F3E; padding: 30px; border-radius: 15px; color: white; margin-top: 30px;">
        <p style="margin: 0; font-size: 16px; line-height: 1.8;">
        <strong style="color: #FF9900;">What happened next:</strong> The early 1900s brought cheap gasoline and Ford's assembly line, pushing EVs aside for over a century. But as our planet demanded change, electric vehicles returned with advanced lithium-ion batteries, smart charging, and sleek designs—not just matching gas cars, but surpassing them. Today's electric revolution reimagines our entire relationship with transportation, energy, and our planet. Exciting right!!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # EV Benefits section with flex containers
    st.markdown("""
    <div style="margin: 20px 0;">
        <h2 style="color: #333; margin-bottom: 20px;">Why Electric Vehicles Are Winning Hearts (And Wallets)</h2>
        <div style="display: flex; gap: 20px; justify-content: space-between;">
            <!-- For Our Planet Container -->
            <div style="
                background-color: #FF9900;
                padding: 20px;
                border-radius: 10px;
                flex: 1;
                color: white;
                box-shadow: -8px 0 15px rgba(255, 255, 255, 0.3), 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #ffffff;">🌍 For Our Planet</h3>
                <p style="margin-bottom: 10px; font-size: 18px;">Environmental game-changer we waited for</p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 10px;">• Zero tailpipe emissions - cleaner air in our cities</li>
                    <li style="margin-bottom: 10px;">• 30-50% lower carbon footprint over vehicle lifetime</li>
                    <li style="margin-bottom: 10px;">• As electricity grids get greener, EVs get even cleaner</li>
                    <li style="margin-bottom: 10px;">• No more oil spills contaminating our environment</li>
                </ul>
            </div>
            <!-- For Your Wallet Container -->
            <div style="
                background-color: #F0F0F0;
                padding: 20px;
                border-radius: 10px;
                flex: 1;
                color: #333;
                box-shadow: -8px 0 15px rgba(255, 255, 255, 0.8), 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #333;">💰 For Your Wallet</h3>
                <p style="margin-bottom: 10px; font-size: 18px;">   Smart economics that make cents (and dollars!)</p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 10px;">• Up to 60% savings on fuel costs vs gasoline</li>
                    <li style="margin-bottom: 10px;">• Fewer moving parts + fewer maintenance costs</li>
                    <li style="margin-bottom: 10px;">• Tax incentives and rebates sweeten the deal</li>
                    <li style="margin-bottom: 10px;">• Better resale value as demand continues growing</li>
                </ul>
            </div>
            <!-- For Our Independence Container -->
            <div style="
                background-color: #404040;
                padding: 20px;
                border-radius: 10px;
                flex: 1;
                color: white;
                box-shadow: -16px 0 15px rgba(255, 255, 255, 0.2), 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #ffffff;">🔸 For Our Independence</h3>
                <p style="margin-bottom: 10px; font-size: 18px;">   Breaking free from fossil fuel dependency</p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 10px;">• Power your car with home-grown renewable energy</li>
                    <li style="margin-bottom: 10px;">• No more worrying about global supply and prices</li>
                    <li style="margin-bottom: 10px;">• Supporting local energy production and jobs</li>
                    <li style="margin-bottom: 10px;">• Vehicle-to-grid tech turns your car into a power source</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Climate crisis heading and banner
    st.markdown("## The Climate Crisis: Why EVs Matter")
    
    def co2_counter():
        # Base CO2 emissions per year (source: Global Carbon Project)
        annual_emissions = 36.8  # billion tonnes CO2 (2023 data)
        emissions_per_second = annual_emissions * 1000000000 / (365 * 24 * 60 * 60)
        
        # Get start of year
        start_of_year = datetime.datetime(2024, 1, 1)
        current_time = datetime.datetime.now()
        seconds_elapsed = (current_time - start_of_year).total_seconds()
        
        emissions = seconds_elapsed * emissions_per_second
        
        st.markdown(f"""
        <div style="background-color: #232F3E; padding: 30px; border-radius: 15px; color: white; margin-top: 30px; text-align: center;">
            <p style="color: #FF9900; font-size: 32px; margin: 0 0 15px 0;">Global CO2 Emissions Counter</p>
            <p style="color: #FF4B4B; font-size: 24px; margin: 0 0 10px 0;">{emissions:,.0f}</p>
            <p style="color: white; font-size: 16px; margin: 0;">Tonnes of CO2 emitted since Jan 1, 2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    co2_counter()
    
    # CO2 emissions plot
    @st.cache_data
    def load_emissions_data():
        url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
        df = pd.read_csv(url)
        return df

    def plot_global_emissions():
        df = load_emissions_data()
        
        # Filter and prepare data
        global_emissions = df[df['country'] == 'World'].copy()
        
        fig = px.area(global_emissions, 
                      x='year', 
                      y='co2',
                      title='Global CO2 Emissions Over Time',
                      labels={'co2': 'CO2 Emissions (billion tonnes)',
                             'year': 'Year'},
                      color_discrete_sequence=['#FF9900'])
        
        fig.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    plot_global_emissions()
    
    # Transport emissions containers (2:1 ratio)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        def transport_emissions_visual():
            # Sample data from IEA
            transport_data = {
                'Mode': ['Road', 'Aviation', 'Shipping', 'Rail', 'Other'],
                'Percentage': [74.5, 11.5, 10.5, 1, 2.5]
            }
            
            df = pd.DataFrame(transport_data)
            
            fig = px.pie(df, 
                         values='Percentage', 
                         names='Mode',
                         title='Global Transport CO2 Emissions by Mode',
                         color_discrete_sequence=['#FF9900', '#FF6600', '#CC5500', '#994400', '#663300'])
            
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=400)
            
            st.plotly_chart(fig, use_container_width=True)
        
        transport_emissions_visual()
    
    with col2:
        st.markdown("""
        <div style="background-color: #232F3E; padding: 25px; border-radius: 15px; color: white; height: 400px; display: flex; flex-direction: column; justify-content: center;">
            <h3 style="color: #FF9900; font-size: 22px; font-weight: bold; margin-bottom: 20px;">Understanding the necessity of EVs</h3>
            <p style="color: white; font-size: 16px; line-height: 1.6; margin: 0;">
            Road transport dominates with 74.5% of all transportation emissions. This massive share makes it the single biggest opportunity for climate impact.
            <br><br>
            Electric vehicles directly target this largest emission source, offering immediate and scalable solutions. Every EV on the road reduces the 74.5% slice, making transportation cleaner for everyone.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color:#232F3E; padding:30px; border-radius:15px; margin:30px 0;">
        <p style="color:white; font-size:16px; line-height:1.7; margin-bottom:20px;">
        Now that we've uncovered the profound importance of electric vehicles and their pivotal role in shaping a sustainable future, we're ready to accelerate into the heart of this revolution. The story doesn't end here—it's just getting started.
        </p><p style="color:white; font-size:16px; line-height:1.7; margin-bottom:20px;">
        In the pages that follow, we'll paint a vivid picture of the EV landscape as it stands today. You'll see millions of electric vehicles silently cruising streets worldwide, their presence growing louder in the global conversation on climate action. We'll map out the thousands of charging stations lighting up our highways, forming the vital arteries of this new transportation ecosystem.
But numbers alone don't capture the full electric spirit. 
We'll zoom in on Amazon's bold strides in sustainability, showcasing how our electric fleets are reimagining delivery in cities across the globe. And for those curious about the road ahead, our AI-powered tools await, ready to predict trends, calculate impacts, and even help you find your perfect electric match.</p>
        <p style="color:white; font-size:16px; line-height:1.7; margin:0;">
        This isn't just a presentation—it's an invitation. An invitation to explore, to engage, and to envision the electric future we're building together. Whether you're an EV enthusiast, a sustainability champion, or simply curious about the technology shaping our world, there's a spark here for everyone.
Ready to plug in and power up your understanding? Let's journey further into the electric revolution—where innovation meets impact, and every mile driven is a mile towards a cleaner, brighter future. Because in this story, everyone has a part to play—including you.
        </p>
    </div>
    """, unsafe_allow_html=True)





with tab2:
    st.markdown("""
    <div style="background-color: #232F3E; padding: 15px; border-radius: 15px; color: white; margin: 10px 0;">
        <h2 style="color: #FF9900; margin-bottom: 5px;">Amazon's Journey to Sustainable Delivery</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline section
    timeline_data = [
        {"year": "2019", "event": "Amazon co-founds The Climate Pledge, committing to net-zero carbon by 2040"},
        {"year": "2020", "event": "Orders 100,000 custom electric delivery vehicles from Rivian"},
        {"year": "2022", "event": "Rolls out over 3,000 electric delivery vans across 100+ U.S. cities"},
        {"year": "2025", "event": "Expands to 25,000+ electric vehicles in its delivery fleet, 10k+ deployed in India"},
        {"year": "2030", "event": "Goal: 100,000 electric delivery vehicles, preventing 4M metric tons of carbon annually"}]

    # Create two columns for timeline and image
    timeline_col, image_col = st.columns([2, 1])

    with timeline_col:
        for i, item in enumerate(timeline_data):
            col_left, col_right = st.columns([1,10], gap="large")

            with col_left:
                st.markdown(f"""
                <div style="background-color:#FF9900; color:#232F3E; padding:10px; border-radius:5px; width:120px; height:50px;
                display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:18px;">
                    {item["year"]}
                </div>
                """, unsafe_allow_html=True)

            with col_right:
                st.markdown(f"""
                <div style="background-color:#F5F5F5; padding:12px; border-radius:6px; border-left:5px solid #FF9900; margin-bottom: 8px; margin-left: 15px;">
                    <p style="margin:0;">{item["event"]}</p>
                </div>
                """, unsafe_allow_html=True)

    with image_col:
        st.image("https://assets.aboutamazon.com/0c/4d/f53aae614cb4b38609b59a6f8df7/hero-001-amazon-rivian-sustainability-amazon-rivian-acam-19372-final-copy.JPG", 
                 use_container_width=True, 
                 caption="Amazon's Electric Delivery Fleet")
    
    # Amazon's EV Impact section in dark blue container
    st.markdown("""
    <div style="background-color: #232F3E; padding: 30px; border-radius: 15px; color: white; margin: 30px 0;">
        <h2 style="color: #FF9900; margin-bottom: 20px; text-align: center;">Amazon's EV Impact at a Glance</h2>
        <div style="display: flex; gap: 30px;">
            <div style="flex: 1;">
                <h3 style="color: #FF9900; margin-bottom: 5px;">Environmental Leadership:</h3>
                <div style="width: 100%; height: 3px; background-color: #FF9900; margin-bottom: 15px;"></div>
                <ul style="line-height: 1.8; color: white;">
                    <li>Amazon's electric fleet will save millions of gallons of fuel annually</li>
                    <li>Custom-designed vehicles with 360-degree visibility and advanced safety features</li>
                    <li>Part of Amazon's Climate Pledge to reach net-zero carbon emissions by 2040</li>
                    <li>Electric delivery vehicles operate in 500+ cities worldwide</li>
                </ul>
            </div>
            <div style="flex: 1;">
                <h3 style="color: #FF9900; margin-bottom: 5px;">Innovation & Infrastructure:</h3>
                <div style="width: 100%; height: 3px; background-color: #FF9900; margin-bottom: 15px;"></div>
                <ul style="line-height: 1.8; color: white;">
                    <li>Installing thousands of charging stations at delivery stations globally</li>
                    <li>Developing custom routing software to optimize EV delivery efficiency</li>
                    <li>Investing in renewable energy projects to power EV charging infrastructure</li>
                    <li>Partnering with utilities to add renewable capacity to the grid</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Amazon Carbon Footprint Chart
    st.markdown('<h3 style="font-size: 26px; text-align: center;">Amazon\'s Carbon Footprint (MMT CO₂e*)</h3>', unsafe_allow_html=True)
    
    # Data
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    direct_emissions = [39.91, 45.75, 55.36, 49.02, 47.40, 50.32]
    indirect_electricity = [5.50, 5.27, 4.07, 3.06, 2.76, 2.80]
    indirect_other = [5.76, 9.62, 12.11, 13.02, 14.22, 15.13]
    carbon_intensity = [122.8, 102.7, 100.8, 85.7, 75.6, 72.6]

    # Create DataFrame
    df_carbon = pd.DataFrame({
        'Year': years,
        'Direct Emissions': direct_emissions,
        'Indirect Emissions from Purchased Electricity': indirect_electricity,
        'Indirect Emissions from Other Sources': indirect_other,
        'Carbon intensity': carbon_intensity
    })

    # Create stacked bar chart
    fig = go.Figure()

    # Add bars in orange shades
    fig.add_trace(go.Bar(x=df_carbon['Year'], y=df_carbon['Direct Emissions'], name='Direct Emissions', marker_color='#FF9900'))
    fig.add_trace(go.Bar(x=df_carbon['Year'], y=df_carbon['Indirect Emissions from Purchased Electricity'], name='Indirect Emissions from Purchased Electricity', marker_color='#FFB84D'))
    fig.add_trace(go.Bar(x=df_carbon['Year'], y=df_carbon['Indirect Emissions from Other Sources'], name='Indirect Emissions from Other Sources', marker_color='#FF6600'))

    # Add carbon intensity line
    fig.add_trace(go.Scatter(x=df_carbon['Year'], y=df_carbon['Carbon intensity'], name='Carbon intensity (gCO₂e/$GMS)', mode='lines+markers', line=dict(color='#CC5500', width=3), marker=dict(size=8)))

    # Update layout
    fig.update_layout(
        barmode='stack',
        xaxis_title='Year',
        yaxis_title='MMT CO₂e',
        legend_title_text='',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        margin=dict(l=40, r=40, t=60, b=40),
        height=600,
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # Add value labels on bars
    for i, year in enumerate(df_carbon['Year']):
        total = df_carbon.iloc[i, 1:4].sum()
        fig.add_annotation(x=year, y=total, text=f"{total:.2f}", showarrow=False, yshift=10)

    # Update axes
    fig.update_xaxes(tickvals=df_carbon['Year'], ticktext=[str(year) for year in df_carbon['Year']])
    fig.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.1)')

    # Display the chart with margins
    st.markdown('<div style="margin: 0 20px;">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)

    # Add footnotes
    st.markdown("""
    <div style="text-align: center; font-size: 12px; color: #666; margin-top: 10px;">
    *Million metric tons carbon dioxide equivalent.
    </div>
    """, unsafe_allow_html=True)
    
    # Line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Add Amazon year review image with margins
    st.markdown('<div style="margin: 0 20px;">', unsafe_allow_html=True)
    st.image("amazonyearreview.png", use_container_width=True)

    # Did You Know container
    st.markdown("""
    <div style="background-color: #232F3E; padding: 20px; border-radius: 15px; color: white; margin: 10px 0; text-align: center;">
        <h3 style="color: #FF9900; margin-bottom: 0px;">Did You Know?</h3>
        <p style="color: white; font-size: 16px; line-height: 1; margin: 0;">
        Our Amazon's cute electric delivery vans can travel up to 150 miles on a single charge, making them ideal for last-mile deliveries in urban areas.
        </p>
    </div>
    """, unsafe_allow_html=True)



with tab3:
    st.header("EVfi Analytics Dashboard - Tableau")

    # Embed Tableau Public dashboard with scrolling enabled
    tableau_url = "https://public.tableau.com/views/EVsImpactOnSustainability/EVDASHBOARD"

    st.markdown(f"""
    <div style="width: 100%; height: 900px;">
        <iframe src="{tableau_url}?:embed=yes&:showVizHome=no&:toolbar=no&:tabs=no&:device=desktop"
                width="100%" height="900" frameborder="0"></iframe>
    </div>
    """, unsafe_allow_html=True)

    



with tab4:
    st.markdown("""
    <div style="background-color:#232F3E; color:white; padding:25px; border-radius:15px; margin-bottom:25px; text-align:center;">
        <h2 style="color:#FF9900; margin-bottom:15px;">🤖 Meet Our GenAI Friend: Sparky ⚡</h2>
        <p style="font-size:18px; margin:0;">Your intelligent EV companion ready to answer all your electric vehicle questions!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize chatbot components
    @st.cache_resource
    def init_chatbot():
        try:
            import os
            from dotenv import load_dotenv
            from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
            from langchain.prompts import PromptTemplate
            from langchain.chains.question_answering import load_qa_chain
            from langchain_community.document_loaders import PyPDFLoader
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            from langchain.schema import Document
            import google.generativeai as genai
            import numpy as np

            load_dotenv()
            
            GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
            
            if not GOOGLE_API_KEY:
                st.error("Missing GOOGLE_API_KEY in .env file")
                return None, None
            
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            genai.configure(api_key=GOOGLE_API_KEY)
            
            return embeddings, []
        except Exception as e:
            st.error(f"Error initializing chatbot: {str(e)}")
            return None, None
    
    @st.cache_data
    def process_knowledge_base():
        try:
            from langchain_community.document_loaders import PyPDFLoader
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            
            loader = PyPDFLoader("Vizcon_EV.pdf")
            documents = loader.load()
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(documents)
            
            embeddings, _ = init_chatbot()
            if not embeddings:
                return 0, []
            
            # Store embeddings in memory instead of Pinecone
            doc_embeddings = []
            for doc in texts:
                embedding = embeddings.embed_query(doc.page_content)
                doc_embeddings.append({
                    'text': doc.page_content,
                    'embedding': embedding
                })
            
            return len(texts), doc_embeddings
        except Exception as e:
            st.error(f"Error loading knowledge base: {str(e)}")
            return 0, []
    
    def get_response(query):
        try:
            from langchain.prompts import PromptTemplate
            from langchain.chains.question_answering import load_qa_chain
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain.schema import Document
            import numpy as np
            
            embeddings, _ = init_chatbot()
            if not embeddings:
                return "Sorry, I'm having technical difficulties. Please try again!"
            
            # Get stored embeddings
            _, doc_embeddings = process_knowledge_base()
            if not doc_embeddings:
                return "I don't have information loaded. Please try again!"
            
            # Get query embedding
            query_embedding = embeddings.embed_query(query)
            
            # Calculate similarities
            similarities = []
            for doc_data in doc_embeddings:
                similarity = np.dot(query_embedding, doc_data['embedding']) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(doc_data['embedding'])
                )
                similarities.append((similarity, doc_data['text']))
            
            # Get top 3 most similar documents
            similarities.sort(reverse=True)
            top_contexts = [text for _, text in similarities[:3]]
            
            if top_contexts:
                combined_context = "\n\n".join(top_contexts)
                
                prompt = PromptTemplate(
                    template="You are Sparky, a friendly EV expert. Answer based on the context:\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:",
                    input_variables=["context", "question"]
                )
                model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
                chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
                
                doc = Document(page_content=combined_context)
                response = chain.invoke({"input_documents": [doc], "question": query})
                return response['output_text']
            else:
                return "I don't have information about that topic. Try asking about electric vehicles, or sustainability!"
        except Exception as e:
            return f"Sorry, I'm having technical difficulties: {str(e)}"
    
    # Initialize knowledge base
    if 'kb_loaded' not in st.session_state:
        with st.spinner("🔋 Sparky is powering up..."):
            chunks, doc_embeddings = process_knowledge_base()
            if chunks > 0:
                st.session_state.kb_loaded = True
                st.session_state.doc_embeddings = doc_embeddings
                st.success("⚡ Sparky is ready to help!")
            else:
                st.error("❌ Sparky needs maintenance. Please try again later.")
    
    # Chat interface
    if 'ev_messages' not in st.session_state:
        st.session_state.ev_messages = [
            {"role": "assistant", "content": "Hi there! I'm Sparky ⚡, your friendly EV expert! Ask me anything about electric vehicles,I'll help :)"}
        ]
    
    # Display chat messages with Amazon styling
    for message in st.session_state.ev_messages:
        if message["role"] == "assistant":
            st.markdown(f"""
            <div style="display: flex; margin: 10px 0;">
                <div style="background-color:#FF9900; color:white; padding:15px; border-radius:15px; max-width:80%; margin-right:20px;">
                    <strong>⚡ Sparky:</strong><br>{message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="display: flex; justify-content: flex-end; margin: 10px 0;">
                <div style="background-color:#F5F5F5; color:#232F3E; padding:15px; border-radius:15px; max-width:80%; margin-left:20px;">
                    <strong>You:</strong><br>{message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Ask Sparky about EVs..."):
        # Add user message
        st.session_state.ev_messages.append({"role": "user", "content": prompt})
        
        # Get and add response
        with st.spinner("⚡ Sparky is thinking..."):
            response = get_response(prompt)
            st.session_state.ev_messages.append({"role": "assistant", "content": response})
        
        st.rerun()
    
    # Disclaimer
    st.markdown("""
    <div style="background-color:#F5F5F5; padding:15px; border-radius:10px; margin-top:20px; border-left:4px solid #FF9900;">
        <p style="color:#555; margin:0; font-size:14px;">
        <strong>ℹ️ Note:</strong> This bot is specifically designed to tell you about Electric Vehicles (EVs). 
        If you have any EV model in mind, ask Sparky about it!
        </p>
    </div>
    """, unsafe_allow_html=True)





st.markdown("---")
st.caption("© 2025 EV Revolution Dashboard - Pranali/Juilee")
