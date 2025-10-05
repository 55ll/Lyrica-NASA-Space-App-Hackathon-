import streamlit as st

st.title("🌠 Lyrica: Meteor Impact Search")
st.write("Search for a known meteor or asteroid to see potential impact details, risks, and story insights.")

search_query = st.text_input("🔍 Enter Meteor or Asteroid Name")

if search_query:
    st.subheader(f"Results for {search_query}")
    st.write("📍 Coordinates: 45.123N, -93.456W")
    st.write("🌍 Estimated Impact Zone: Northern Hemisphere")
    st.write("💥 Expected Impact Force: Medium")
    st.write("📖 Story Insight: A cosmic traveler that reminds us how small our world can be under the vast sky.")
