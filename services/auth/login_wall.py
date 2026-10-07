import streamlit as st
from services.persistence.exercise_repository import get_or_create_user
 
_LEFT = """
<div class="login-root">
  <div class="lg-top">
    <span class="lg-logo">A</span><span class="lg-brand">Apna Coach</span>
  </div>
  <div class="lg-eyebrow">Real-time pose AI &middot; Voice coaching</div>
  <h1 class="lg-title">Your<br><span class="lg-outline">form,</span> <span class="lg-accent">out<br>loud.</span></h1>
  <p class="lg-sub">Camera watches every rep. Coach speaks the correction before the bad habit sets in.</p>
</div>
"""
 
_RIGHT = """
<div class="login-root">
  <div class="lg-card">
    <span class="lg-tag lg-tag-a"><i></i>KNEE <b class="lg-deg"></b>&deg;</span>
    <span class="lg-tag lg-tag-b"><i></i>BACK STRAIGHT</span>
    <svg class="lg-fig" viewBox="0 0 300 340" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <defs><filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <linearGradient id="fl" x1="0" x2="1"><stop offset="0" stop-color="#FF5A2D" stop-opacity="0"/><stop offset=".5" stop-color="#FF5A2D" stop-opacity=".7"/><stop offset="1" stop-color="#FF5A2D" stop-opacity="0"/></linearGradient></defs>
      <rect x="10" y="311" width="280" height="3" rx="1.5" fill="url(#fl)"/>
      <path d="M176,134 L113,208" stroke="#FF5A2D" stroke-width="3" stroke-dasharray="3 8" opacity=".45"/><path d="M176,134 L234,144" stroke="#FF5A2D" stroke-width="3" stroke-dasharray="3 8" opacity=".45"/><path d="M113,208 L170,248" stroke="#FF5A2D" stroke-width="3" stroke-dasharray="3 8" opacity=".45"/><path d="M170,248 L138,300" stroke="#FF5A2D" stroke-width="3" stroke-dasharray="3 8" opacity=".45"/><path d="M138,300 L170,300" stroke="#FF5A2D" stroke-width="3" stroke-dasharray="3 8" opacity=".45"/>
      <path d="M150,82 L138,170" stroke="#F1ECE4" stroke-width="8" opacity="1"><animate attributeName="d" values="M150,82 L138,170;M176,134 L113,208;M150,82 L138,170" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></path><path d="M150,82 L208,112" stroke="#F1ECE4" stroke-width="8" opacity="1"><animate attributeName="d" values="M150,82 L208,112;M176,134 L234,144;M150,82 L208,112" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></path><path d="M138,170 L146,240" stroke="#F1ECE4" stroke-width="8" opacity="1"><animate attributeName="d" values="M138,170 L146,240;M113,208 L170,248;M138,170 L146,240" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></path><path d="M146,240 L138,300" stroke="#F1ECE4" stroke-width="8" opacity="1"><animate attributeName="d" values="M146,240 L138,300;M170,248 L138,300;M146,240 L138,300" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></path><path d="M138,300 L170,300" stroke="#F1ECE4" stroke-width="8" opacity="1"><animate attributeName="d" values="M138,300 L170,300;M138,300 L170,300;M138,300 L170,300" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></path>
      <circle cx="150" cy="52" r="17" stroke="#F1ECE4" stroke-width="7" fill="#0E0B0A"><animate attributeName="cx" values="150;197;150" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="52;108;52" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle>
      <circle class="lg-ring" cx="146" cy="240" r="12" stroke="#FF5A2D" stroke-width="2"><animate attributeName="cx" values="146;170;146" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="240;248;240" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle>
      <circle cx="138" cy="170" r="10" fill="#FF5A2D" stroke="#0E0B0A" stroke-width="5" filter="url(#glow)"><animate attributeName="cx" values="138;113;138" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="170;208;170" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle><circle cx="146" cy="240" r="10" fill="#FF5A2D" stroke="#0E0B0A" stroke-width="5" filter="url(#glow)"><animate attributeName="cx" values="146;170;146" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="240;248;240" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle><circle cx="138" cy="300" r="10" fill="#FF5A2D" stroke="#0E0B0A" stroke-width="5" filter="url(#glow)"><animate attributeName="cx" values="138;138;138" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="300;300;300" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle><circle cx="150" cy="82" r="8" fill="#FF5A2D" stroke="#0E0B0A" stroke-width="5" filter="url(#glow)"><animate attributeName="cx" values="150;176;150" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="82;134;82" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle><circle cx="208" cy="112" r="7" fill="#F1ECE4" stroke="#0E0B0A" stroke-width="5" filter="url(#glow)"><animate attributeName="cx" values="208;234;208" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="112;144;112" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" dur="3.6s" repeatCount="indefinite"/></circle>
    </svg>
    <span class="lg-tag lg-tag-c"><i></i>"Chest up. Drive through heels."</span>
    <div class="lg-ticker"><div class="lg-track">
      <span>PUSH-UPS &middot; CURLS &middot; LUNGES &middot; SQUATS &middot; PUSH-UPS &middot; CURLS &middot; LUNGES &middot; SQUATS &middot; </span>
      <span>PUSH-UPS &middot; CURLS &middot; LUNGES &middot; SQUATS &middot; PUSH-UPS &middot; CURLS &middot; LUNGES &middot; SQUATS &middot; </span>
    </div></div>
  </div>
</div>
"""
 
 
def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
 
    left, right = st.columns([1.05, 1], gap="large", vertical_alignment="center")
 
    with left:
        st.markdown(_LEFT, unsafe_allow_html=True)
 
        with st.form("login_form", clear_on_submit=False, border=False):
            c1, c2 = st.columns([3, 1.25], vertical_alignment="center")
            with c1:
                username = st.text_input(
                    "Name (unique)",
                    placeholder="pick a unique name",
                    label_visibility="collapsed",
                )
            with c2:
                submit_button = st.form_submit_button("Start  →", type="primary", width="stretch")
 
    with right:
        st.markdown(_RIGHT, unsafe_allow_html=True)
 
    if submit_button:
        username = (username or "").strip()
        if not username:
            with left:
                st.error("Name cannot be empty.")
            return False
 
        user = get_or_create_user(username)
 
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]
 
        st.rerun()
 
    return False