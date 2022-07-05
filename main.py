import time   
import requests
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    return requests.get(url)
    
start_time = time.time()

list_of_urls = ["http://ip.jsontest.com/"]*1000

with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(get_url,list_of_urls))

print("--- %s seconds ---" % (time.time() - start_time))

