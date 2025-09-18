import streamlit as st
from datetime import datetime, date, time
from zoneinfo import ZoneInfo

# --- Page setup ---
st.set_page_config(
    page_title="MAYURESH KA HAPPY BIRTHDAY",
    page_icon="🐱❤️",
    layout='wide'
)

# --- Timezone ---
TZ = ZoneInfo("Asia/Kolkata")

# --- Dates ---
go_live_date = date(2025, 9, 18)
Birthday = date(2025, 9, 27)
Birthday_time = time(0, 0, 0)

# --- Daily memes (files must be in same folder as app.py) ---
DAILY_MEMES = {
    date(2025, 9, 18): "cat-drumming.gif",
    date(2025, 9, 19): "sad-cat.jpg",
    date(2025, 9, 20): "cigg-cat.jpg",
    date(2025, 9, 21): "cat-drink.jpg",
    date(2025, 9, 22): "sick-cat-awu-cat.gif",
    date(2025, 9, 23): "besito-catlove.gif",
    date(2025, 9, 24): "orange-cat-laughing.gif",
    date(2025, 9, 25): "cat-sleep.jpg",
    date(2025, 9, 26): "yippee-cat-kitty.gif",
}

DEFAULT_MEME_URL = "https://placekitten.com/1200/700"

def meme_for_day(d: date) -> str:
    return DAILY_MEMES.get(d, DEFAULT_MEME_URL)

# --- Birthday song (file must be in same folder as app.py) ---
BIRTHDAY_SONG_URL = "cat-bday-song.mp3"
SONG_AUTOPLAY_WINDOW_MIN = 5

# --- State memory ---
if "played_song" not in st.session_state:
    st.session_state.played_song = False

# --- Helper function to split seconds ---
def dhms(total_seconds: int):
    total = max(total_seconds, 0)
    d = total // 86400
    rem = total % 86400
    h = rem // 3600
    rem %= 3600
    m = rem // 60
    s = rem % 60
    return d, h, m, s

# --- Current time ---
now = datetime.now(TZ)
target = datetime.combine(Birthday, Birthday_time).replace(tzinfo=TZ)
today_ist = now.date()

# --- Header ---
st.markdown(
    """
    <div style="text-align:center;padding:1.25rem 0">
      <h1 style="margin:0;font-size:3rem">🐱 MAYURESH KA HAPPY BIRTHDAY</h1>
      <p style="margin:0.25rem 0;font-size:1.1rem;color:#777">IST · India Standard Time</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Before live date ---
if today_ist < go_live_date:
    st.info("⏳ Coming soon BABY... site goes live on 18 September (IST).")

# --- Countdown mode (18th–26th Sept) ---
elif now < target:
    show_date = today_ist
    meme_url = meme_for_day(show_date)
    day_num = (show_date - go_live_date).days + 1 if go_live_date <= show_date <= date(2025, 9, 26) else None
    caption = f"Day {day_num} of 9 😺" if day_num and 1 <= day_num <= 9 else "Daily cat vibes 😺"

    st.image(meme_url, use_container_width=True, caption=caption)

    remaining = int((target - now).total_seconds())
    d, h, m, s = dhms(remaining)
    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Days", f"{d:02d}")
    c2.metric("Hours", f"{h:02d}")
    c3.metric("Minutes", f"{m:02d}")
    c4.metric("Seconds", f"{s:02d}")
    st.caption("Countdown to September 27 (IST)")

# --- Birthday celebration (on/after 27 Sept) ---
else:
    st.success("🎉 It's party time, let's celebrate baby HAPPY BIRTHDAY SONU!! 🎉")
    st.image(meme_for_day(Birthday), use_container_width=True, caption="HAPPY BIRTHDAY SONU 🎂")
    st.balloons()

    is_birthday = (today_ist == Birthday)
    minutes_since_midnight = now.hour * 60 + now.minute

    # Autoplay window at midnight
    if is_birthday:
        within_autoplay_window = (minutes_since_midnight < SONG_AUTOPLAY_WINDOW_MIN)

        if within_autoplay_window and not st.session_state.played_song:
            st.audio(BIRTHDAY_SONG_URL, loop=False)
            st.session_state.played_song = True
            st.caption("If you don't hear music, your browser may block autoplay—use the button below.")

        # Play / Replay button all day
        col_play, _ = st.columns([1, 3])
        with col_play:
            label = "▶️ Play Birthday Song" if not st.session_state.played_song else "🔁 Replay Birthday Song"
            if st.button(label):
                st.audio(BIRTHDAY_SONG_URL, loop=False)
                st.session_state.played_song = True

    else:
        # After 27 Sept → only manual replay
        col_play, _ = st.columns([1, 3])
        with col_play:
            if st.button("🔁 Replay Birthday Song"):
                st.audio(BIRTHDAY_SONG_URL, loop=False)

    

  
      
       




    
 
 
 




   


    
