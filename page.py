import streamlit as st
import random

# set page config
st.set_page_config(
    page_icon=":rocket:",
    page_title="Gaming Zone",
    layout="centered",
    initial_sidebar_state="expanded")

st.title("Guess the number game")

# initilizn sesion state variable
if 'random_num' not in st.session_state:
    st.session_state.random_num = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'guess' not in st.session_state:
    st.session_state.guess = []
if 'stored_min_max' not in st.session_state:  
    st.session_state.stored_min_max = (0, 1)

# inputt for user rnge
min_value = st.number_input("Set a minimum range.", min_value=0, value=0, step=1)
max_value = st.number_input("Set a maximum range.", max_value=100, value=1, step=1)

if min_value >= max_value:
    st.error("Minimum value must be less than maximum value.")
else:
    apply_button = st.button("Apply Range")
    if apply_button:
        st.session_state.stored_min_max = (min_value, max_value) 
        st.session_state.random_num = random.randint(min_value, max_value)
        st.session_state.attempts = 0
        st.session_state.guess = []
        st.markdown(f"## Guess the number between {min_value} and {max_value}")

# Game logic
if st.session_state.random_num is not None:
    guess = st.number_input("Try your luck :ghost:",min_value=st.session_state.stored_min_max[0],max_value=st.session_state.stored_min_max[1],step=1)
    
    if st.button("Finger crossed! :clap:"):
        st.session_state.attempts += 1
        st.session_state.guess.append(guess)
        
        if guess > st.session_state.random_num:
            st.error("Nice try, rocket scientist. Lower, please. 🚀📉")
        elif guess < st.session_state.random_num:
            st.error("Digging deep? Aim higher next time. 🌱🕳️")
        else:
            st.success(f"You guessed {st.session_state.random_num} correctly in {st.session_state.attempts} attempts! Great 🎉")
            st.balloons()
            st.session_state.random_num = None  # End game

        if st.session_state.attempts >= 7 and guess != st.session_state.random_num:
            st.error(f"Game Over! The number was {st.session_state.random_num}. 🎲")
            st.session_state.random_num = None  # End game

# try again logic
if st.session_state.random_num is None and st.session_state.attempts > 0:
    if st.button("I will try again :bulb:"):
        # Reuse original stored range
        st.session_state.random_num = random.randint(st.session_state.stored_min_max[0], st.session_state.stored_min_max[1])
        st.session_state.attempts = 0
        st.session_state.guess = []

# Show previous guesses
if st.session_state.guess:
    st.write(f"Previous guesses: {st.session_state.guess}")
    st.write(f"Attempts left: {7 - st.session_state.attempts}")