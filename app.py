# Import libraries
import streamlit as st
import eda, predict

# bagian dalam sidebar
with st.sidebar:
    st.write('# Page Navigation')

    # Toggle choose menu
    page = st.selectbox('Choose Page', ('EDA', 'Prediction'))

    # Test
    st.write('Current Page:', page)

    st.write('## About')
    
    st.markdown(
    """
    <p style="text-align: justify;">
    This dashboard helps the FMCG International marketing team predict customer responses for the next marketing campaign.
    </p>
    """,
    unsafe_allow_html=True)

# bagian luar sidebar
if page == 'EDA':
    eda.run()
else:
    predict.run()