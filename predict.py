# Import libraries
import streamlit as st
import pandas as pd
import pickle
import datetime

# Load model
with open('best_model.pkl', 'rb') as file_1:
    best_model = pickle.load(file_1)

def run():
    st.write("# Customer's Campaign Response")

    # batas tanggal (2012–2014)
    min_date = datetime.date(2012, 1, 1)
    max_date = datetime.date(2014, 12, 31)

    # ==== FORM 1: Biography ====
    with st.form("bio_form"):
        st.subheader("Biography")
        cid = st.text_input("Customer ID", placeholder="1234")

        edu = st.selectbox("Education", ["Basic", "Graduation", "Master", "PhD"])
        marital = st.selectbox(
            "Marital Status",
            ["Married", "Together", "Single", "Divorced", "Widow", "Other"],
        )

        income  = st.number_input("Income", min_value=0, step=1)
        kid     = st.number_input("Kid Home", min_value=0, step=1)
        teen    = st.number_input("Teen Home", min_value=0, step=1)
        recency = st.number_input("Recency", min_value=0, step=1)

        reg_date = st.date_input(
            "Registration Date",
            value=datetime.date(2013, 1, 1),
            min_value=min_date,
            max_value=max_date,
        )

        bio_submitted = st.form_submit_button("Save Bio")

    if bio_submitted:
        st.success("Biography saved.")

    # ==== FORM 2: Product + Campaign ====
    with st.form("product_form"):
        st.subheader("Product")
        wine  = st.number_input("Wine Product",  min_value=0, step=1)
        fruit = st.number_input("Fruit Product", min_value=0, step=1)
        meat  = st.number_input("Meat Product",  min_value=0, step=1)
        fish  = st.number_input("Fish Product",  min_value=0, step=1)
        sweet = st.number_input("Sweet Product", min_value=0, step=1)
        gold  = st.number_input("Gold Product",  min_value=0, step=1)

        # preview total di dalam form
        total = wine + fruit + meat + fish + sweet + gold
        st.number_input("Total Product", value=total, disabled=True)

        # Campaign & Deals
        st.subheader("Campaign and Deals")
        deals    = st.number_input("Number of Deals", min_value=0, step=1)
        web      = st.number_input("Number of Web Purchases", min_value=0, step=1)
        catalog  = st.number_input("Number of Catalog Purchases", min_value=0, step=1)
        store    = st.number_input("Number of Store Purchases", min_value=0, step=1)
        visit    = st.number_input("Number of Web Visits", min_value=0, step=1)

        # Campaign Acceptance
        st.subheader("Last Campaign Responses")
        cmp1 = st.number_input("Campaign 1 Accepted", min_value=0, max_value=1, step=1)
        cmp2 = st.number_input("Campaign 2 Accepted", min_value=0, max_value=1, step=1)
        cmp3 = st.number_input("Campaign 3 Accepted", min_value=0, max_value=1, step=1)
        cmp4 = st.number_input("Campaign 4 Accepted", min_value=0, max_value=1, step=1)
        cmp5 = st.number_input("Campaign 5 Accepted", min_value=0, max_value=1, step=1)

        submitted = st.form_submit_button("Submit All Data")

    # Susun dataframe untuk inference
    data_inf = pd.DataFrame([{
        "id": cid,
        "education": edu,
        "marital_status": marital,
        "income": income,
        "kid_home": kid,
        "teen_home": teen,
        "date_customer": reg_date,  # biarkan date; diasumsikan pipeline di model yang handle
        "recency": recency,
        "wine_prods": wine,
        "fruit_prods": fruit,
        "meat_prods": meat,
        "fish_prods": fish,
        "sweet_prods": sweet,
        "gold_prods": gold,
        "total_spent": total,
        "num_deals": deals,
        "num_web": web,
        "num_catalog": catalog,
        "num_store": store,
        "num_web_visits": visit,
        "cmp1": cmp1,
        "cmp2": cmp2,
        "cmp3": cmp3,
        "cmp4": cmp4,
        "cmp5": cmp5
    }])

    st.caption("Preview input")
    st.dataframe(data_inf, use_container_width=True)

    # Jalankan prediksi hanya saat tombol Submit ditekan
    if submitted:
        try:
            # Prediksi kelas
            result = int(best_model.predict(data_inf)[0])

            # Probabilitas (jika tersedia)
            prob = None
            if hasattr(best_model, "predict_proba"):
                prob = float(best_model.predict_proba(data_inf)[0][1]) * 100

            # Tampilkan hasil
            if result == 1:
                if prob is not None:
                    st.success(f'Customer diprediksi akan memberikan response (1) '
                               f'dengan probabilitas {prob:.2f}%')
                else:
                    st.success('Customer diprediksi akan memberikan response (1).')
            else:
                if prob is not None:
                    st.warning(f'Customer diprediksi tidak akan memberikan response (0) '
                               f'dengan probabilitas {100 - prob:.2f}%')
                else:
                    st.warning('Customer diprediksi tidak akan memberikan response (0).')

        except Exception as e:
            st.error(f"Gagal melakukan prediksi: {e}")
    else:
        st.info("Isi form dan klik **Submit All Data** untuk menjalankan prediksi.")
