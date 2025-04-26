import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Broken Arrow Fire Forms",
    page_icon="🔥",
    layout="centered"
)

# --- Centered Logo Display ---
logo = Image.open("BAFIRE-Patch.jpg")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, use_column_width=True)

st.markdown("<h1 style='text-align: center; color: #B22222;'>Broken Arrow Fire Department</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #B22222;'>Internal Forms Hub</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Fire Forms Dictionary ---
fire_forms = {
    "Lexipol Feedback Form": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l_Y4fc7sB_ZBmjA4xbOC63NUNERSSjZVS01ZUEFPNEw0QzRHUEwxSUZYQy4u",
    "Add Pay Request Form": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l4OCiLz9x-VHidJzfg7Wn_lUMVJOVjZGUEE0UkkxTEI1U0JaTDZKWkVaUyQlQCN0PWcu",
    "Carelink Navigation Form": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l_Y4fc7sB_ZBmjA4xbOC63NUMEJMTTRNTjc0MkJPNlI1MjZOSDBZNlJZVi4u",
    "Paramedic Credentialing Candidate Observation Form": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l_Y4fc7sB_ZBmjA4xbOC63NUOU9YU05URlZXNVRJWTlMMFNKSUFKUjRYQy4u",
    "Daily Shift Summary Form": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l8-0KqloRu9Fu9RcB6dQ4PZUQUQ3MjQ4Q01NN1pXUDZIWE9YQlg3Q09RSy4u",
    "Training Request Form": "https://apps.gov.powerapps.us/play/e/default-cfb77493-4959-4a57-b52c-45ee2fbff997/a/4cb4ba1e-b237-43a9-9ab8-ab7773e07a40?tenantId=cfb77493-4959-4a57-b52c-45ee2fbff997&hint=a475ebd1-6d27-4e61-9668-0a04ddf78847&sourcetime=1745690187916&pa_isFromQRCode=true&skipMobileRedirect=1",
    "Medical Facility Feedback Form": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l_Y4fc7sB_ZBmjA4xbOC63NUNE05NEsyVlFXRk9JQkZKTEZHUktIQUE1TS4u"
}

# --- Form Selection ---
st.markdown("#### 🔽 Select a form from the dropdown:")
selected_form = st.selectbox("Fire Forms", list(fire_forms.keys()))

if selected_form:
    form_url = fire_forms[selected_form]

    st.markdown(f"👉 [Click here to open **{selected_form}** in a new tab]({form_url})", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"<h4 style='color:#B22222;'>Embedded Form View:</h4>", unsafe_allow_html=True)

    # --- Centered iframe Display ---
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center;'>
            <iframe src="{form_url}" width="80%" height="700" style="border:2px solid #B22222; border-radius:10px;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>City of Broken Arrow | Fire Department | Est. 1906</p>", unsafe_allow_html=True)
