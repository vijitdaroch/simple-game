import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎲",
    layout="centered"
)

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'best_score' not in st.session_state:
    st.session_state.best_score = float('inf')
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title and instructions
st.title("🎲 Number Guessing Game")
st.markdown("""
Try to guess the number between 1 and 100!
* You'll get hints after each guess
* Try to solve it in as few attempts as possible
* Beat your best score!
""")

# Game interface
with st.container():
    # Display current stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Attempts", st.session_state.attempts)
    with col2:
        best_score_display = "∞" if st.session_state.best_score == float('inf') else st.session_state.best_score
        st.metric("Best Score", best_score_display)

    # Input for guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess == st.session_state.random_number:
            st.balloons()
            st.success(f"🎉 Congratulations! You found the number in {st.session_state.attempts} attempts!")
            
            # Update best score
            if st.session_state.attempts < st.session_state.best_score:
                st.session_state.best_score = st.session_state.attempts
                st.success("🏆 New Best Score!")
            
            st.session_state.game_over = True
            
        else:
            # Provide hints
            if abs(guess - st.session_state.random_number) <= 5:
                st.warning("🔥 You're very close!")
            elif abs(guess - st.session_state.random_number) <= 10:
                st.info("😊 Getting warmer!")
            
            if guess < st.session_state.random_number:
                st.write("👆 Try a higher number")
            else:
                st.write("👇 Try a lower number")

# New game button
if st.session_state.game_over:
    if st.button("Start New Game"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()

# Add some fun statistics
if st.session_state.attempts > 0:
    st.sidebar.header("Game Statistics")
    st.sidebar.write(f"🎯 Attempts: {st.session_state.attempts}")
    
    # Calculate and display efficiency
    efficiency = 100 - ((st.session_state.attempts - 1) * 5) if st.session_state.attempts <= 20 else 0
    st.sidebar.progress(efficiency)
    st.sidebar.write(f"Efficiency Score: {efficiency}%")
    
    # Fun facts
    if st.session_state.attempts <= 5:
        st.sidebar.write("🌟 You're doing great!")
    elif st.session_state.attempts <= 10:
        st.sidebar.write("💪 Keep going!")
    else:
        st.sidebar.write("�� Don't give up!") 