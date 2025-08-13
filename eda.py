# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image


def run():
    # Header
    st.title("Marketing Campaign Data Analysis")

    # Gambar cover
    gambar = Image.open('fmcg_cmp.jpg')
    st.image(gambar, use_container_width=True)

    # Background
    st.subheader("Background")
    st.markdown("""
    <div style="text-align: justify;">
    This dataset contains demographic information, purchasing behavior, and participation history of customers 
    in various marketing campaigns run by FMCG International. It includes attributes such as age, education level, 
    marital status, number of children, total spending across product categories, and previous engagement in promotional campaigns.
    </div><br>
    """, unsafe_allow_html=True)

    # Load dataset utama + preview tabel
    st.subheader("Dataset")
    data = pd.read_csv('marketing_cmp_cleaned.csv')
    st.dataframe(data, use_container_width=True)

    # Load dataset EDA
    data2 = pd.read_csv('marketing_cmp_eda.csv')

    # Pilihan visualisasi
    st.subheader("Exploratory Data Analysis")
    option = st.selectbox(
        "Select EDA Distribution:",
        ("Total Spending", "Age Distribution")
    )

    # Visualisasi & penjelasan
    if option == "Total Spending":
        st.write("#### Total Spending Distribution")
        fig = plt.figure()
        sns.histplot(data2['total_spent'], kde=True, bins=30)
        plt.title('Total Spending')
        st.pyplot(fig, use_container_width=True)
        st.markdown(
    """
    <div style="text-align: justify;">
    The histogram indicates that most customers spend less than <b>500 units</b>, with a right-skewed distribution showing a few high spenders. This suggests opportunities to boost spending among the majority while maintaining engagement with high-value customers.
    </div><br>
    """,
    unsafe_allow_html=True
)


    elif option == "Age Distribution":
        st.write("#### Age Distribution")
        fig = plt.figure()
        sns.histplot(data2['age'], kde=True, bins=30)
        plt.title('Age Distribution')
        st.pyplot(fig, use_container_width=True)
        st.markdown(
            """
    <div style="text-align: justify;">
    The histogram shows that most customers are concentrated in the <b>30–50 age range</b>, indicating a dominant middle-aged customer base. Marketing strategies can be tailored to better engage this demographic while also exploring opportunities in younger and older segments.
    </div><br>
    """,
    unsafe_allow_html=True)
        
    # Definisikan kolom produk
    product_cols = [
    'wine_prods',
    'meat_prods',
    'gold_prods',
    'fish_prods',
    'sweet_prods',
    'fruit_prods']
    # Hitung total pembelian per kategori
    product_totals = data2[product_cols].sum().sort_values(ascending=False)

# Visualisasi
    st.write("#### Total Spending per Product Category")
    fig = plt.figure(figsize=(8,5))
    sns.barplot(x=product_totals.index, y=product_totals.values, palette='viridis')
    plt.title("Total Spending per Product Category", fontsize=14, fontweight='bold')
    plt.ylabel("Total Spending")
    plt.xlabel("Product Category")
    st.pyplot(fig)

# Penjelasan
    st.markdown(
    """
    <div style="text-align: justify;">
    The bar chart shows that <b>wine products</b> contribute the largest share of total spending, followed by <b>meat products</b>. Other categories such as gold, fish, sweet, and fruit products account for significantly lower spending. 
    This highlights the importance of focusing marketing and promotional efforts on high-revenue categories while exploring strategies to increase sales in lower-performing segments.
    </div><br>
    """,
    unsafe_allow_html=True)

    # =========================
    campaign_cols = ['cmp1', 'cmp2', 'cmp3', 'cmp4', 'cmp5']
    acceptance_rate = data2[campaign_cols].mean().sort_values(ascending=False)
    st.write("### Acceptance Rate per Campaign")
    fig = plt.figure(figsize=(8,5))
    sns.barplot(x=acceptance_rate.index, y=acceptance_rate.values, palette='viridis')
    plt.title("Acceptance Rate per Campaign", fontsize=14, fontweight='bold')
    plt.ylabel("Acceptance Rate")
    plt.xlabel("Campaign")
    plt.ylim(0, 1)
    st.pyplot(fig)
    st.markdown("""
<div style="text-align: justify;">
The bar chart indicates that acceptance rates are relatively low across all campaigns, 
with <b>Campaign 4</b> showing the highest rate, followed closely by Campaign 3 and Campaign 5. 
Campaign 2 records the lowest acceptance rate, suggesting the need to evaluate and potentially redesign its approach to improve engagement.
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    run()


