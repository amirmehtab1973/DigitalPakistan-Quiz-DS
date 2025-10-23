# In the Student Panel quiz section, replace the timer section with this:

if st.session_state.quiz_active and st.session_state.current_quiz_id == selected_quiz_option:
    quiz = quizzes_dict[st.session_state.current_quiz_id]
    questions = quiz['questions']
    duration_minutes = quiz.get('duration_minutes', len(questions))
    
    # Create containers for dynamic updates
    timer_container = st.empty()
    refresh_button_container = st.empty()
    
    # Calculate remaining time
    if st.session_state.quiz_start_time and st.session_state.quiz_duration:
        current_time = time.time()
        elapsed_time = current_time - st.session_state.quiz_start_time
        remaining_time = max(0, st.session_state.quiz_duration - elapsed_time)
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        
        # Determine timer color
        timer_class = ""
        if remaining_time < 60:
            timer_class = "timer-danger"
        elif remaining_time < st.session_state.quiz_duration // 2:
            timer_class = "timer-warning"
        
        # Update timer display
        with timer_container.container():
            st.markdown(f"""
            <div class="timer-wrapper">
                <div class="timer-container {timer_class}">
                    <div style="font-size: 14px; font-weight: bold; margin-bottom: 5px;">⏰ QUIZ TIMER</div>
                    <div style="font-size: 18px; font-weight: bold; font-family: 'Courier New', monospace; margin-bottom: 3px;">
                        {minutes:02d}:{seconds:02d}
                    </div>
                    <div style="font-size: 11px; opacity: 0.9;">
                        {duration_minutes} minute quiz
                    </div>
                    <div style="font-size: 10px; margin-top: 8px; color: #666;">
                        Last update: {datetime.now().strftime("%H:%M:%S")}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Update refresh button
        with refresh_button_container.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col4:
                if st.button("🔄 Update", key="dynamic_refresh_btn"):
                    st.rerun()
    
    # Add auto-refresh JavaScript
    st.markdown("""
    <script>
    // Auto-refresh every 3 seconds for better responsiveness
    setTimeout(function() {
        window.location.reload();
    }, 3000);
    </script>
    """, unsafe_allow_html=True)
    
    # ... rest of the quiz code (questions, etc.)
