import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

#df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

#df['EdLevel'] = df['EdLevel'].apply(clean_education) 

@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country_encoded", "EdLevel_encoded", "YearsCodePro", "Employment_encoded", "ConvertedComp"]]
    df.rename(columns={
        "Country_encoded": "Country",
        "EdLevel_encoded": "EdLevel",
        "Employment_encoded": "Employment",
        "ConvertedComp": "Salary"
    }, inplace=True)
    return df

df = load_data()

def show_explore_page():
    st.title("explore software engineer salaries")
    st.write(
    """
    stack overflow deeloper survey 2020
    """
    )
    
    data = df["Country"].value_counts()
    
    fig1, ax1 = plt.subplots()
    #ax1.pie(data,labels= data.index,autopct = "%1.1f%", shadow = True,startangle=90)
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)

    ax1.axis("equal")
    st.write("""£££ number of data from diffrent countries""")
    st.pyplot(fig1)
     
    st.write("""mean salaray based on country""")
    #data = df.groupby(["Country"])["Salary".mean().sort_values(ascending= True)]
    data = df.groupby("Country")["Salary"].mean().sort_values(ascending=True)

    st.bar_chart(data)
    
    st.write("""mean salaray based on experience""")
    #data = df.groupby(["Country"])["Salary".mean().sort_values(ascending= True)]
    data = df.groupby("YearsCodePro")["Salary"].mean().sort_values(ascending=True)

    st.line_chart(data)
    

        
    
    
    
    
