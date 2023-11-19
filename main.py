import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The best company")

st.write("Fusce nisl massa, imperdiet sed pharetra non, rhoncus fringilla augue. Maecenas porttitor tincidunt massa, ac pretium orci condimentum in. In rutrum diam ac lectus imperdiet accumsan. Donec ac felis id felis rutrum cursus nec at nunc. Vivamus et molestie tortor. Phasellus et lorem vulputate augue feugiat condimentum. Maecenas sit amet pretium felis. Praesent pulvinar pulvinar magna, tincidunt egestas nulla. Sed feugiat leo orci. In hac habitasse platea dictumst. Donec at sapien at ipsum scelerisque ornare. Praesent sagittis egestas feugiat. Morbi nec pellentesque nulla, tempor rhoncus augue. Morbi ut neque ac risus facilisis facilisis eget eu sapien. Cras dictum sapien tempor ex blandit, quis consequat tortor sodales. ")

st.subheader("Our team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(str(row['first name'].capitalize()) + " " + row['last name'].capitalize())
        st.write(row['role'])
        st.image('images/{}'.format(row['image']))

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(str(row['first name'].capitalize()) + " " + row['last name'].capitalize())
        st.write(row['role'])
        st.image('images/{}'.format(row['image']))

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(str(row['first name'].capitalize()) + " " + row['last name'].capitalize())
        st.write(row['role'])
        st.image('images/{}'.format(row['image']))
