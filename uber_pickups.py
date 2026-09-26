import requests
import streamlit as st

st.title('Pokemon')
#===============================================================
BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon(name_or_id: str, timeout: float = 6) -> dict:
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    r = requests.get(f"{BASE_URL}/{str(name_or_id).strip().lower()}", timeout=timeout)
    r.raise_for_status()
    return r.json()
#===============================================================

pokemon = st.text_input("Enter pokemon name/id")
res = fetch_pokemon(pokemon)

if st.button("Search"):
    st.write("Id: ", res["id"])
    st.write("Name: ", res["name"])
    st.write("Wieght: ", res["weight"])
    st.write("Height: ", res["height"])
    st.write("Ability: ", res["abilities"][0]["ability"]["name"])

    if len(res["types"]) == 1:
        st.write("Types: ", res["types"][0]["type"]["name"])
    else:
        st.write("Types: ", res["types"][0]["type"]["name"], " & ", res["types"][1]["type"]["name"])

    #Base stats
    hp, atk, defe, Satk, Sdefe, sp = st.columns(6)

    with hp:
        st.write("Hp")
        st.write(res["stats"][0]["base_stat"])

    with atk:
        st.write("Attack")
        st.write(res["stats"][1]["base_stat"])

    with defe:
        st.write("Defense")
        st.write(res["stats"][2]["base_stat"])

    with Satk:
        st.write("Special attack")
        st.write(res["stats"][3]["base_stat"])

    with Sdefe:
        st.write("Special defense")
        st.write(res["stats"][4]["base_stat"])

    with sp:
        st.write("Speed")
        st.write(res["stats"][5]["base_stat"])
