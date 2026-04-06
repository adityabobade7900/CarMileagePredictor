import streamlit as st
import pandas as pd
import pickle

# ── Load model and encoders ──────────────────────────────────
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

# ── Page config ──────────────────────────────────────────────
st.set_page_config(page_title="Car Mileage Predictor", page_icon="🚗")

st.title("🚗 Car Mileage Predictor")
st.markdown("Enter your car specs to predict fuel efficiency.")
st.markdown("---")

# ── User inputs ──────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    engine_cc = st.number_input("Engine CC",
                                min_value=500, max_value=8000,
                                value=1500, step=100)

    horsepower = st.number_input("Horsepower (HP)",
                                 min_value=50, max_value=1000,
                                 value=150, step=10)

    fuel_type = st.selectbox("Fuel Type",
                             options=['Petrol', 'Premium', 'Diesel', 'Flex/Other'])

with col2:
    transmission = st.selectbox("Transmission",
                                options=['AUTOMATIC', 'MANUAL', 'DIRECT_DRIVE'])

    driven_wheels = st.selectbox("Driven Wheels",
                                 options=['front wheel drive', 'rear wheel drive',
                                          'all wheel drive', 'four wheel drive'])

    vehicle_size = st.selectbox("Vehicle Size",
                                options=['Compact', 'Midsize', 'Large'])

vehicle_style = st.selectbox("Vehicle Style",
                             options=['Sedan', '4dr SUV', 'Coupe', 'Convertible',
                                      '4dr Hatchback', 'Crew Cab Pickup',
                                      'Extended Cab Pickup', 'Wagon',
                                      '2dr Hatchback', 'Passenger Minivan',
                                      'Regular Cab Pickup', '2dr SUV'])

st.markdown("---")

# ── Prediction ───────────────────────────────────────────────
if st.button("⚡ Predict Mileage", use_container_width=True):

    def safe_encode(encoder, value):
        if value in encoder.classes_:
            return encoder.transform([value])[0]
        return 0

    input_data = pd.DataFrame([{
        'Engine_CC':  engine_cc,
        'Engine HP':  horsepower,
        'fuel_enc':   safe_encode(encoders['fuel'],  fuel_type),
        'trans_enc':  safe_encode(encoders['trans'], transmission),
        'drive_enc':  safe_encode(encoders['drive'], driven_wheels),
        'size_enc':   safe_encode(encoders['size'],  vehicle_size),
        'style_enc':  safe_encode(encoders['style'], vehicle_style),
    }])

    prediction = model.predict(input_data)[0]
    kml = prediction * 0.425144

    # Colour code result
    if prediction >= 30:
        color = "green"
        label = "Excellent Fuel Efficiency 🟢"
    elif prediction >= 20:
        color = "orange"
        label = "Average Fuel Efficiency 🟡"
    else:
        color = "red"
        label = "Low Fuel Efficiency 🔴"

    st.markdown(f"""
    <div style='
        border-left: 5px solid {color};
        padding: 20px;
        border-radius: 10px;
        background-color: #1e1e1e;
        text-align: center;
    '>
        <h2 style='color: {color};'>Predicted Mileage: {prediction:.1f} MPG</h2>
        <p style='color: #aaa;'>{label}</p>
        <p style='color: #aaa;'>🇮🇳 Approx: {kml:.1f} km/litre</p>
    </div>
    """, unsafe_allow_html=True)

st.caption("Model: Random Forest | R² = 0.9586 | MAE = 0.61 MPG")
