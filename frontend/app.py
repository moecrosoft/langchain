import streamlit as st
import requests 

BACKEND = 'http://backend:8000'

st.set_page_config(page_title='Incident AI', layout='centered')

st.title('💻 Debug Assistant AI')
st.caption('Analyse system errors and get root cause + fix')

query = st.text_area('Describe your issue')

if st.button('Analyse'):
    if query.strip() == '':
        st.warning('Please enter an issue')
    else:
        with st.spinner('Analysing...'):
            res = requests.post(
                f'{BACKEND}/analyse',
                json={'query': query}
            )

            if res.status_code == 200:

                data = res.json()
                
                st.markdown('## 🧠 Root Cause')
                st.info(data.get('root_cause',''))

                st.markdown('## 🛠 Fix Steps')
                for step in data.get('fix_steps', []):
                    st.success(step)

                st.markdown('## 🛡 Prevention')
                for p in data.get('prevention', []):
                    st.warning(p)
        
            else:
                st.error('Something went wrong')
                
            