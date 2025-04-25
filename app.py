
import streamlit as st

# Set page config
st.set_page_config(
    page_title="Broken Arrow Fire Forms",
    page_icon="🔥",
    layout="centered"
)

# --- Logo Display ---
st.markdown(
    "<div style='text-align: center;'><img src='BAFIRE-Patch.jpg' width='200'></div>",
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #B22222;'>Broken Arrow Fire Department</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #B22222;'>Internal Forms Hub</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Fire Forms ---
fire_forms = {
    "Carelink Referral": "https://forms.office.com/g/kQ5jmrKwEc",
    "Medical Facility Feedback": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l_Y4fc7sB_ZBmjA4xbOC63NUNE05NEsyVlFXRk9JQkZKTEZHUktIQUE1TS4u",
    "New EOP Feedback": "https://forms.office.com/Pages/ResponsePage.aspx?id=k3S3z1lJV0q1LEXuL7_5l_Y4fc7sB_ZBmjA4xbOC63NUNERSSjZVS01ZUEFPNEw0QzRHUEwxSUZYQy4u",
    "Special Training/Travel Request": "https://apps.gov.powerapps.us/play/e/default-cfb77493-4959-4a57-b52c-45ee2fbff997/a/4cb4ba1e-b237-43a9-9ab8-ab7773e07a40?tenantId=cfb77493-4959-4a57-b52c-45ee2fbff997&hint=a475ebd1-6d27-4e61-9668-0a04ddf78847&source=sharebutton&sourcetime=1745597268109"
}

st.markdown("#### 🔽 Select a form from the dropdown:")
selected_form = st.selectbox("Fire Forms", list(fire_forms.keys()))

if selected_form:
    form_url = fire_forms[selected_form]

    st.markdown(f"👉 [Click here to open **{selected_form}** in a new tab]({form_url})", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"<h4 style='color:#B22222;'>Embedded Form View:</h4>", unsafe_allow_html=True)

    st.markdown(
        f'<iframe src="{form_url}" width="100%" height="700" style="border:2px solid #B22222; border-radius:10px;"></iframe>',
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>City of Broken Arrow | Fire Department | Est. 1906</p>", unsafe_allow_html=True)
