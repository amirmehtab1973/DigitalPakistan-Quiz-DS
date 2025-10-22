# In the student panel quiz section, replace the timer section with:

if st.session_state.quiz_active and st.session_state.current_quiz_id == selected_quiz_option:
    quiz = quizzes_dict[st.session_state.current_quiz_id]
    questions = quiz['questions']
    duration_minutes = quiz.get('duration_minutes', len(questions))
    
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
        
        # Display timer in fixed position
        timer_html = f"""
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
                    Auto-updates every second
                </div>
            </div>
        </div>
        """
        st.markdown(timer_html, unsafe_allow_html=True)
    
    # Add a manual refresh button in the main content area
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("🔄 Manual Refresh Timer", key="manual_refresh_btn", use_container_width=True):
            st.rerun()
    
    # Time expired warning
    if st.session_state.time_expired:
        st.error("⏰ TIME'S UP! Your quiz is being submitted...")
    
    st.markdown(f"""
    <div class="quiz-container">
        <h3>📝 Taking Quiz: {quiz['title']}</h3>
        <p><strong>Total Questions:</strong> {len(questions)} | <strong>Time Allowed:</strong> {duration_minutes} minutes</p>
        <p><em>Timer updates automatically every second. Use 'Manual Refresh' if needed.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # ... rest of the questions code ...
