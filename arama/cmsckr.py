import requests
import concurrent.futures
banner = '''
   \u001b[31m_____ __  __  _____    _____ _  _______  
  / ____|  \/  |/ ____|  / ____| |/ /  __ \  
 | |    | \  / | (___   | |    | ' /| |__) |
 | |    | |\/| |\___ \  | |    |  < |  _  / 
 | |____| |  | |____) | | |____| . \| | \ \ 
  \_____|_|  |_|_____/   \_____|_|\_\_|  \_\ \n
   \u001b[32mCODED BY N30N | H0RN3T_SP1D3R\n
   TEAM BADS                                         
                                            
'''
# Define ANSI color codes for printing CMS names
COLORS = {
    "wordpress": "\033[94m",  # blue
    "joomla": "\033[93m",    # yellow
    "drupal": "\033[96m",    # cyan
    "shopify": "\033[92m",   # green
    "woocommerce": "\033[91m",  # red
    "magento": "\033[95m"    # magenta
}

def check_cms(url):
    # Define the file names to save the URLs based on the CMS platform
    cms_files = {
        "wordpress": "wordpress.txt",
        "joomla": "joomla.txt",
        "drupal": "drupal.txt",
        "shopify": "shopify.txt",
        "woocommerce": "woocommerce.txt",
        "magento": "magento.txt"
    }

    response = requests.get(url)

    cms_detected = False
    for cms, filename in cms_files.items():
        if cms in response.text.lower():
            with open(filename, "a") as outfile:
                outfile.write(url + "\n")
            print(url, "uses", COLORS[cms] + cms + "\033[0m")
            cms_detected = True
            break

    if not cms_detected:
        with open("others.txt", "a") as outfile:
            outfile.write(url + "\n")
        print(url, "uses an unknown CMS")

print(banner)
filename = input("\033[1;31mENTER FILE NAME: ")
# file = open(filename).read().split()
file = open(filename, encoding="utf-8").read().split()

myfile = set(file)
thread = int(input("\033[1;31mThreads: "))

# Create a thread pool with a maximum of 10 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
    # Submit each URL to the thread pool
    futures = [executor.submit(check_cms, site) for site in myfile]

    # Wait for all threads to complete
    concurrent.futures.wait(futures)