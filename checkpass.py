import requests
import hashlib

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/'+query
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error fetching request for {query} = {res.status_code}")
    return res

def get_passwords_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)
    

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(response)
    print(first5_char, tail)
    return get_passwords_leaks_count(response, tail)

pwned_api_check('123')