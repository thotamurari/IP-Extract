import re
import requests

def extract_ips_from_url():
    url = input("Enter the URL: ").strip()
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            
            # Extract IPs using regex
            ip_pattern = re.compile(r'(?:"ip_address":\s*")(\d{1,3}(?:\.\d{1,3}){3})')
            ip_addresses = ip_pattern.findall(content)
            
            if ip_addresses:
                print("\nExtracted IPs:")
                for ip in ip_addresses:
                    print(ip)
            else:
                print("No IP addresses found.")
        else:
            print(f"Failed to fetch URL. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the tool
extract_ips_from_url()
