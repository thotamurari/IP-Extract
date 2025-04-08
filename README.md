# 🔍 IP Extractor from URL

This Python tool extracts all IP addresses from a given URL — perfect for processing JSON logs, VirusTotal API responses, or any raw data containing `"ip_address"` fields.

---

## 💡 Features

- 🌐 Takes a URL input from the user  
- 📤 Sends a GET request and fetches data  
- 🧠 Extracts all IP addresses using regex  
- 🖥️ Outputs clean and readable IPs  
- ⚡ Lightweight and fast — no dependencies other than `requests`


## 📦 Installation

Clone this repository:
```bash
git clone https://github.com/yourusername/ip-extractor-tool.git
cd ip-extractor-tool

🚀 Usage
Run the tool using Python:

python ip_extractor.py


Enter the URL when prompted:

Enter the URL: https://www.virustotal.com/vtapi/v2/domain/report?apikey=YOUR_API_KEY&domain=example.com

You will get:

Extracted IPs:
54.75.226.1
54.75.250.69
63.32.24.250
