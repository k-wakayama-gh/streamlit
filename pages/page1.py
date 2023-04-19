import streamlit as st
from PIL import Image
import pandas as pd
#import matplotlib.pyplot as plt


st.subheader('自己紹介')

st.text('これはsubheaderです\n あああ')

code = '''
import streamlit as st

st.title('テストアプリ')
'''

st.code(code, language='python')