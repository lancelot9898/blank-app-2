import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# Membership plan costs and session fees
membership_plans = {
    "FlexPass": {
        "annual_cost": 300,
        "court_booking_single": 40,
        "court_booking_double": 60,
        "usta_match": 45,
        "clinic_60min": 70,
        "clinic_90min": 84,
        "workshop": 112,
        "junior_clinic": 90,  # per session for juniors (not applicable here)
        "junior_discount": 0,  # No discount in FlexPass
        "monthly_cost": 300 / 12
    },
    "Platinum": {
        "annual_cost": 9000,  # $750/month
        "court_booking_single": 0,  # Included
        "court_booking_double": 0,  # Included
        "usta_match": 0,  # Included
        "clinic_60min": 0,  # Included
        "clinic_90min": 0,  # Included
        "workshop": 0,  # Included
        "junior_clinic": 90,  # Same junior clinic cost for comparison
        "junior_discount": 0.4,  # 40% discount in Family Plan
        "monthly_cost": 750
    },
    "Platinum Family": {
        "annual_cost": 12000,  # $1000/month
        "court_booking_single": 0,
        "court_booking_double": 0,
        "usta_match": 0,
        "clinic_60min": 0,
        "clinic_90min": 0,
        "workshop": 0,
        "junior_clinic": 90,
        "junior_discount": 0.4,  # 40% discount for junior clinics in Family Plan
        "monthly_cost": 1000
    },
    "Platinum Family with Junior": {
        "annual_cost": 12000,  # $1000/month
        "court_booking_single": 0,
        "court_booking_double": 0,
        "usta_match": 0,
        "clinic_60min": 0,
        "clinic_90min": 0,
        "workshop": 0,
        "junior_clinic": 90,
        "junior_discount": 0.4,  # 40% discount for junior clinics
        "monthly_cost": 1000
    }
}

# Function to calculate the monthly cost for each plan
def calculate_cost(plan_name, selection, junior_sessions=0):
    plan = membership_plans[plan_name]
    cost = plan['monthly_cost']
    
    cost += selection['singles'] * plan['court_booking_single']
    cost += selection['doubles'] * plan['court_booking_double']
    cost += selection['usta_matches'] * plan['usta_match']
    cost += selection['60min_clinics'] * plan['clinic_60min']
    cost += selection['90min_clinics'] * plan['clinic_90min']
    cost += selection['workshops'] * plan['workshop']

    if junior_sessions > 0:
        cost += junior_sessions * plan['junior_clinic'] * (1 - plan['junior_discount'])
    
    return cost

# Streamlit User Interface
st.title("Tennis Club Membership Cost Calculator")

# Input activities for the user
st.header("Choose your activities")
singles = st.slider("Singles court bookings (per month)", 0, 20, 4)
doubles = st.slider("Doubles court bookings (per month)", 0, 20, 2)
usta_matches = st.slider("USTA matches (per month)", 0, 10, 2)
clinics_60min = st.slider("60-minute clinics (per month)", 0, 10, 2)
clinics_90min = st.slider("90-minute clinics (per month)", 0, 10, 1)
workshops = st.slider("Workshops (per month)", 0, 10, 1)
junior_sessions = st.slider("Junior clinic sessions (per month)", 0, 10, 4)

# Create selection dictionary
selection = {
    'singles': singles,
    'doubles': doubles,
    'usta_matches': usta_matches,
    '60min_clinics': clinics_60min,
    '90min_clinics': clinics_90min,
    'workshops': workshops
}

# Calculate costs for each plan
flex_cost = calculate_cost("FlexPass", selection)
platinum_cost = calculate_cost("Platinum", selection)
platinum_family_cost = calculate_cost("Platinum Family", selection)
platinum_family_with_junior_cost = calculate_cost("Platinum Family with Junior", selection, junior_sessions)

# Display the costs
st.subheader("Your Monthly Costs")
st.write(f"**FlexPass**: ${flex_cost:.2f} per month")
st.write(f"**Platinum**: ${platinum_cost:.2f} per month")
st.write(f"**Platinum Family**: ${platinum_family_cost:.2f} per month")
st.write(f"**Platinum Family with Junior**: ${platinum_family_with_junior_cost:.2f} per month (with junior sessions)")

# Determine the best option
best_option = min(flex_cost, platinum_cost, platinum_family_cost, platinum_family_with_junior_cost)
if best_option == flex_cost:
    st.success("The FlexPass is the best option for you based on your selection!")
elif best_option == platinum_cost:
    st.success("The Platinum plan is the best option for you based on your selection!")
elif best_option == platinum_family_cost:
    st.success("The Platinum Family plan is the best option for you based on your selection!")
else:
    st.success("The Platinum Family plan with Junior discount is the best option for you based on your selection!")
