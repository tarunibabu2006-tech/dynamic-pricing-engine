import streamlit as st

st.title("Dynamic Pricing Engine")

demand = st.slider("Demand", 0, 100)
competitor_price = st.number_input("Competitor Price")

if st.button("Predict Price"):
    # Ensure dynamic_price function is available, or redefine it here if needed
    # For this example, assuming dynamic_price is defined elsewhere or will be included
    def dynamic_price(demand, competitor_price, base_price):
        if demand > 80:
            return base_price * 1.2
        elif demand < 30:
            return base_price * 0.8
        else:
            return (base_price + competitor_price) / 2
            
    price = dynamic_price(demand, competitor_price, 100)
    st.write("Suggested Price:", price)
