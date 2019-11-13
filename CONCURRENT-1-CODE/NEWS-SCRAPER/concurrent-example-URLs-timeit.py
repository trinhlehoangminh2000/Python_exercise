import timeit

code_to_time = """

import concurrent.futures
import urllib.request
import threading


URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def concurrent_URLs_example():

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc), \n)
            else:
                print('%r page is %d bytes' % (url, len(data)),\n)
        print(\n)

concurrent_URLs_example()


"""


#timeit requires a string so code to be timed appears in """...""" like a docstring
elapsed_time = timeit.timeit(code_to_time, number=10)/10            #get the average of 10 cycles
print(elapsed_time)                                               #time printed in seconds
