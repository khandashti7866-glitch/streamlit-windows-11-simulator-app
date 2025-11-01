import streamlit as st
from PIL import Image
import base64

# --- Page Config ---
st.set_page_config(page_title="Windows 11 Simulator", layout="wide")

# --- CSS Styling for Windows 11 look ---
st.markdown(
    """
    <style>
    /* Body background and font */
    body {
        background-color: #0f0f0f;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Taskbar */
    .taskbar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50px;
        background: rgba(25, 25, 25, 0.95);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 999;
        border-top: 1px solid #333;
        border-radius: 15px 15px 0 0;
    }

    /* Taskbar icons */
    .taskbar-icon {
        margin: 0 15px;
        width: 30px;
        height: 30px;
        border-radius: 8px;
        transition: all 0.2s ease;
    }
    .taskbar-icon:hover {
        background-color: #3a3a3a;
        cursor: pointer;
    }

    /* Windows-style window */
    .app-window {
        position: absolute;
        top: 100px;
        left: 100px;
        width: 400px;
        height: 300px;
        background: #1a1a1a;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.6);
        padding: 10px;
        color: white;
    }

    /* Start menu */
    .start-menu {
        position: fixed;
        bottom: 60px;
        left: 20px;
        width: 300px;
        background: #1a1a1a;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.6);
        padding: 10px;
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Functions to simulate apps ---
def open_notepad():
    st.markdown('<div class="app-window"><h3>Notepad</h3><textarea style="width:100%;height:200px;"></textarea></div>', unsafe_allow_html=True)

def open_calculator():
    st.markdown('<div class="app-window"><h3>Calculator</h3><input type="text" style="width:100%;height:30px;" placeholder="0"/></div>', unsafe_allow_html=True)

def open_settings():
    st.markdown('<div class="app-window"><h3>Settings</h3>'
                '<label>Theme:</label>'
                '<select><option>Light</option><option>Dark</option></select><br><br>'
                '<label>Volume:</label>'
                '<input type="range" min="0" max="100"/><br><br>'
                '<label>Wallpaper:</label>'
                '<select><option>Default</option><option>Wallpaper 1</option><option>Wallpaper 2</option></select>'
                '</div>', unsafe_allow_html=True)

# --- Sidebar for simulation ---
st.sidebar.title("Windows 11 Simulator Controls")
app_choice = st.sidebar.selectbox("Open App:", ["", "Notepad", "Calculator", "Settings"])

# --- Open selected app ---
if app_choice == "Notepad":
    open_notepad()
elif app_choice == "Calculator":
    open_calculator()
elif app_choice == "Settings":
    open_settings()

# --- Taskbar HTML ---
st.markdown(
    """
    <div class="taskbar">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/windows10.png" title="Start Menu">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/search.png" title="Search">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/task.png" title="Task View">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/widgets.png" title="Widgets">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/folder-invoices.png" title="File Explorer">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/internet.png" title="Browser">
        <img class="taskbar-icon" src="https://img.icons8.com/ios-filled/50/ffffff/settings.png" title="Settings">
    </div>
    """,
    unsafe_allow_html=True
)
