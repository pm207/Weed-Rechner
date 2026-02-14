import streamlit as st
import string

st.set_page_config(page_title="Who get's the Weed? 🍃", layout="centered")

st.title("Who get's the Weed? 🍃")

if "personen_index" not in st.session_state:
    st.session_state.personen_index = 1

if "betraege" not in st.session_state:
    st.session_state.betraege = [0.0]

gesamt_essen = st.number_input("Gesamtmenge (g):", min_value=0.0, step=1.0)

st.subheader("Einzahlungen")

for i in range(st.session_state.personen_index):
    buchstabe = string.ascii_uppercase[i]
    name = f"Kiffer {buchstabe} zahlt:"
    st.session_state.betraege[i] = st.number_input(
        name,
        min_value=0.0,
        step=10.0,
        key=f"person_{i}"
    )

col1, col2 = st.columns(2)

with col1:
    if st.button("Person hinzufügen"):
        st.session_state.personen_index += 1
        st.session_state.betraege.append(0.0)
        st.rerun()

with col2:
    if st.button("Berechnen"):
        gesamtbetrag = sum(st.session_state.betraege)

        if gesamtbetrag == 0:
            st.warning("Niemand hat gezahlt")
        else:
            st.subheader("Ergebnis")
            for i, betrag in enumerate(st.session_state.betraege):
                anteil = (betrag / gesamtbetrag) * gesamt_essen
                buchstabe = string.ascii_uppercase[i]
                wert_formatiert = f"{anteil:.2f}".replace(".", ",")
                st.success(f"Kiffer {buchstabe}: {wert_formatiert} g")
#tsuki
