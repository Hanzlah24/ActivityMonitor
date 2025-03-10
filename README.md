# User Manual for Activity Logger

## Overview
This project consists of two Python scripts:
1. **monitor.py** - Tracks active browser windows and logs activity.
2. **admin.py** - Provides a GUI for viewing and searching log files.

## Installation Guide

### Step 1: Download and Extract
1. Download the ZIP file containing the scripts.
2. Extract the contents to your preferred directory.

### Step 2: Install Dependencies
Run the following command to install the required modules:
```sh
pip install -r requirements.txt
```

## Usage Instructions

### Running `monitor.py`
To start logging active browser tabs and fake logs:
```sh
python monitor.py
```

### Running `admin.py`
To open the log viewer GUI:
```sh
python admin.py
```

## Features
- **monitor.py**
  - Detects active Chrome or Edge browser windows.
  - Logs activity only when switching between tabs.
  - Generates fake logs for realistic terminal output.
- **admin.py**
  - Allows users to select log files.
  - Displays logs in a readable format.
  - Supports searching for specific logs.

## Notes
- The logs are encoded in Base64 for obfuscation.
- Log entries are saved in `activity_log.txt`.

