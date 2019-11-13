import timeit

code_to_time = """

import concurrent.futures
import urllib.request
import threading


URLS2 = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://www.guardian.com/',
        'http://www.spiegel.de/',
        'http://www.dailymail.co.uk/',
        'http://doesnotexist-at-all.com/']

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        print("Task Executed for URL{}".format(threading.current_thread()), url, \n)
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

concurrent_URLs_example()


"""


#timeit requires a string so code to be timed appears in """...""" like a docstring
elapsed_time = timeit.timeit(code_to_time, number=5)/5              #get the average of 10 cycles
print(elapsed_time)                                                 #time printed in seconds
