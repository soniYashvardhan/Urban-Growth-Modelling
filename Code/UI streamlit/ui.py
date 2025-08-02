import streamlit as st
import time
from PIL import Image
import pandas as pd
import numpy as np

def model():
    time.sleep(3)
    return "hi"

def app():
    st.write("MAPS")
    st.write("Parameter Maps")
    img=Image.open("major roads.png")
    st.image(img,caption="Major Roads",width=512)

    img=Image.open("metro.png")
    st.image(img,caption="Metro",width=512)

    img=Image.open("parks.png")
    st.image(img,caption="Park",width=512)

    img=Image.open("schols and uni.png")
    st.image(img,caption="Schools and uUniversity",width=512)

    img=Image.open("sweage.png")
    st.image(img,caption="Sewage Pipeline",width=512)

    st.write("Acutal Lulc")

    img=Image.open("2017actuall.png")
    st.image(img,caption="Actual 2020",width=512)

    img=Image.open("act2018.png")
    st.image(img,caption="Actual 2021",width=512)

    img=Image.open("act2019.png")
    st.image(img,caption="Actual 2022",width=512)
    
    st.write("Predicted LuLc")

    img=Image.open("2020_actuall.png")
    st.image(img,caption="Predcted 2022",width=512)
    
    img=Image.open("2020_predicted.png")
    st.image(img,caption="Predcted 2023",width=512)
    
    img=Image.open("act2021.png")
    st.image(img,caption="Predcted 2024",width=512)
    
    img=Image.open("act2022.png")
    st.image(img,caption="Predcted 2025",width=512)
    
    img=Image.open("2022perd.png")
    st.image(img,caption="Predcted 2026",width=512)
    
    img=Image.open("2023actuall.png")
    st.image(img,caption="Predcted 2027",width=512)
    
    img=Image.open("2023pred.png")
    st.image(img,caption="Predcted 2028",width=512)
    
    img=Image.open("2024pred.png")
    st.image(img,caption="Predcted 2029",width=512)
    
    img=Image.open("2025pred.png")
    st.image(img,caption="Predcted 2030",width=512)

    st.write("Trafice Recommendation")

    img=Image.open("area1.jpeg")
    st.image(img,caption="Area 1",width=512)

    img=Image.open("area2.jpeg")
    st.image(img,caption="Area 2",width=512)

    img=Image.open("area3.jpeg")
    st.image(img,caption="Area 3",width=512)

    img=Image.open("area4.jpeg")
    st.image(img,caption="Area 4",width=512)

    st.write("Water Piplines")

    img=Image.open("wateract.jpeg")
    st.image(img,caption="Actual Water Pipelines",width=512)

    img=Image.open("waterpred.jpeg")
    st.image(img,caption="Prediced Water Pipelines",width=512)
    
    # m1=['Maps','Water','Traffic']
    # ch=st.sidebar.selectbox('Menu',m1)
    # if ch=='Maps':
    #     m2=['lulc','road','park']
    #     ch1=st.selectbox("Choose Map",m2)
    #     if ch1=='lulc':
            # img=Image.open("C:\\Users\\unuiw\\OneDrive\\Desktop\\lulc.png")
            # st.image(img,caption=ch1,width=512)
    #         st.image(img,caption=ch1,width=256)
    #     elif ch1=='road':
    #         img=Image.open("C:\\Users\\unuiw\\OneDrive\\Desktop\\roads.png")
    #         st.image(img,caption=ch1)
    #     else:
    #         img=Image.open("C:\\Users\\unuiw\\OneDrive\\Desktop\\park.png")
    #         st.image(img,caption=ch1)
    # elif ch=='Water':
    #     file=st.file_uploader("Choose File")
    #     if file is not None:
    #         st.write("File Name",file.name)
    #         st.write(model())
    # else:
    #     st.write("Loading")
    #     videoFile=open("C:\\Users\\unuiw\\OneDrive\\Pictures\\Camera Roll\\WIN_20221113_00_30_44_Pro.mp4",'rb')
    #     video_bytes=videoFile.read()
    #     st.video(video_bytes)
    #     df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    #     st.dataframe(df)

if __name__=='__main__':
    app()