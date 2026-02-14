import streamlit as st

st.set_page_config(page_title="Who get's the Weed? 🍃", layout="centered")

st.title("Who get's the Weed? 🍃")

if "personen_index" not in st.session_state:
    st.session_state.personen_index = 1

if "betraege" not in st.session_state:
    st.session_state.betraege = [0.0]

gesamt_essen = st.number_input("Gesamtmenge (g):", min_value=0.0, step=0.1)

st.subheader("Einzahlungen")

for i in range(st.session_state.personen_index):
    name = "Kiffer Nr. 1 zahlt:" if i == 0 else f"Kiffer Nr. {i+1} zahlt:"
    st.session_state.betraege[i] = st.number_input(
        name,
        min_value=0.0,
        step=0.1,
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
                name = "Billy" if i == 0 else f"Kiffer Nr. {i+1}"
                st.success(f"{name}: {anteil:.1f} g")


