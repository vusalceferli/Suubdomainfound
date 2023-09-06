import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = "google.com"

with open ("subdomain.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        #print(word)
        url = "http://" + word + "." + target_input
        response = make_request(url)
        print(response)
        if response:
            print("found subdomain ====>" + url)
