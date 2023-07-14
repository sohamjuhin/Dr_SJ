import requests

def gather_information(target_url):
    # Perform footprinting activities to gather information
    
    # Send an HTTP GET request to the target URL
    response = requests.get(target_url)
    
    # Gather information from the response
    status_code = response.status_code
    headers = response.headers
    content = response.text
    
    # Print the gathered information
    print("Target URL:", target_url)
    print("Status Code:", status_code)
    print("Headers:")
    for header, value in headers.items():
        print(header + ":", value)
    print("Content:", content)

def main():
    # Prompt the user to enter the target URL
    target_url = input("Enter the target URL: ")
    
    # Call the gather_information function with the target URL
    gather_information(target_url)

if __name__ == "__main__":
    main()
