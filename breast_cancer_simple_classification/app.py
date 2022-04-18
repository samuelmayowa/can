import streamlit as st
import pickle

svm = pickle.load(open('BrestCancerClassify.pkl', 'rb'))


def classify(num):
    if num == 0:
        return 'Maglignant: This is safe form of cancer type'
    elif num == 1:
        return 'Benin: This is dangerous, pls go for medication'
    else:
        return 'Unknown category of cancer'


def main():
    st.title("Welcome to Simple Breast Cancer ML Web Project")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Cancer Prediction Using ML</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities = ['SVM', 'Please choose only SVM for now']
    option = st.sidebar.selectbox(
        'Which model would you like to use?', activities)
    st.subheader(option)
    mr = st.slider('Mean Radius', 0.0, 10.0)
    mt = st.slider('Mean Texture', 0.0, 10.0)
    mp = st.slider('Mean Perimeter', 0.0, 10.0)
    ma = st.slider('Mean Area', 0.0, 10.0)
    ms = st.slider('Mean Smoothness', 0.0, 10.0)
    mc = st.slider('Mean Compactness', 0.0, 10.0)
    mcon = st.slider('Mean Concavity', 0.0, 10.0)
    mcp = st.slider('Mean Concave Points', 0.0, 10.0)
    msy = st.slider('Mean Symmetry', 0.0, 10.0)
    mfd = st.slider('Mean Fractal Dimension', 0.0, 10.0)
    re = st.slider('Radius Error', 0.0, 10.0)
    te = st.slider('Texture Error', 0.0, 10.0)
    pe = st.slider('Perimeter Error', 0.0, 10.0)
    ae = st.slider('Area Error', 0.0, 10.0)
    se = st.slider('Smoothness Error', 0.0, 10.0)
    ce = st.slider('Compactness Error', 0.0, 10.0)
    cerr = st.slider('Concave Error', 0.0, 10.0)
    cpe = st.slider('Concave Points Error', 0.0, 10.0)
    sye = st.slider('Symmetry Error', 0.0, 10.0)
    fde = st.slider('Fractal Dimension Error', 0.0, 10.0)
    wr = st.slider('Worst Radius', 0.0, 10.0)
    wt = st.slider('Worst Texture', 0.0, 10.0)
    wp = st.slider('Worst Perimeter', 0.0, 10.0)
    wa = st.slider('Worst Area', 0.0, 10.0)
    ws = st.slider('Worst Smoothness', 0.0, 10.0)
    wcom = st.slider('Worst Compactness', 0.0, 10.0)
    wc = st.slider('Worst Concavity', 0.0, 10.0)
    wcp = st.slider('Worst Concave Points', 0.0, 10.0)
    wsy = st.slider('Worst Symmetry', 0.0, 10.0)
    wfd = st.slider('Worst Fractal Dimension', 0.0, 10.0)
    inputs = [[mr, mt, mp, ma, ms, mc,
               mcon, mcp, msy, mfd, re, te, pe,
               ae, se, ce, cerr, cpe, sye, fde, wr, wt, wp, wa, ws, wcom, wc, wcp, wsy, wfd]]
    if st.button('Classify'):
        st.success(classify(svm.predict(inputs)))

if __name__ == '__main__':
    main()
