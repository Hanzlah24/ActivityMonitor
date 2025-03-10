import tkinter as tk
from tkinter import filedialog, scrolledtext
import base64
import json
from datetime import datetime

log_file = ""

def select_log_file():
    """Opens a file dialog to select a log file."""
    global log_file
    log_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if log_file:
        file_label.config(text=f"Selected File: {log_file}")
        display_all_logs()

def display_all_logs():
    """Displays all logs in a human-readable format."""
    if not log_file:
        return
    
    with open(log_file, "r") as f:
        logs = f.readlines()
    
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    
    for log in logs:
        try:
            encoded_timestamp, encoded_entry = log.strip().split(" - ")
            timestamp = decode_data(encoded_timestamp)
            log_entry = decode_data(encoded_entry)
            
            # Convert timestamp to human-readable format
            formatted_timestamp = format_timestamp(timestamp)
            
            # Convert JSON log entry to readable format
            readable_log = format_log_entry(log_entry)

            result_text.insert(tk.END, f"[{formatted_timestamp}]\n{readable_log}\n\n")
        except Exception:
            continue
    
    result_text.config(state=tk.DISABLED)

def search_logs():
    """Search logs for a keyword and display matching results."""
    if not log_file:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select a log file first.\n")
        result_text.config(state=tk.DISABLED)
        return
    
    keyword = search_entry.get().strip().lower()
    if not keyword:
        display_all_logs()
        return
    
    with open(log_file, "r") as f:
        logs = f.readlines()
    
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    
    found = False
    for log in logs:
        try:
            encoded_timestamp, encoded_entry = log.strip().split(" - ")
            timestamp = decode_data(encoded_timestamp)
            log_entry = decode_data(encoded_entry)
            
            formatted_timestamp = format_timestamp(timestamp)
            readable_log = format_log_entry(log_entry)

            if keyword in readable_log.lower():
                result_text.insert(tk.END, f"[{formatted_timestamp}]\n{readable_log}\n\n")
                found = True
        except Exception:
            continue
    
    if not found:
        result_text.insert(tk.END, "No matching logs found.\n")
    
    result_text.config(state=tk.DISABLED)

def decode_data(data):
    """Decodes Base64 encoded log entries."""
    try:
        return base64.b64decode(data).decode("utf-8")
    except Exception:
        return "(Unable to decode log entry)"

def format_timestamp(timestamp):
    """Converts raw timestamp string to a more human-readable format."""
    try:
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%A, %B %d, %Y at %I:%M:%S %p")  # Example: Sunday, March 03, 2025 at 12:34:56 PM
    except ValueError:
        return timestamp  # Return as-is if format is incorrect

def format_log_entry(log_entry):
    """Converts JSON log entries into a more readable text format."""
    try:
        log_data = json.loads(log_entry)
        return f"Active Browser Tab: {log_data.get('active_browser_tab', 'Unknown')}"
    except json.JSONDecodeError:
        return log_entry  # Return raw log if not valid JSON

# GUI Setup
root = tk.Tk()
root.title("Activity Log Viewer")
root.geometry("600x400")

tk.Button(root, text="Select Log File", command=select_log_file).pack()
file_label = tk.Label(root, text="No file selected")
file_label.pack()

tk.Label(root, text="Enter keyword to search:").pack()
search_entry = tk.Entry(root, width=50)
search_entry.pack()

tk.Button(root, text="Search", command=search_logs).pack()

result_text = scrolledtext.ScrolledText(root, width=70, height=20, state=tk.DISABLED)
result_text.pack()

root.mainloop()
