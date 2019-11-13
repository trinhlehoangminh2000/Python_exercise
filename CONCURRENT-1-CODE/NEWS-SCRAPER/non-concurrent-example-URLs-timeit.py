
import timeit

code_to_time = """

import urllib.request


URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def non_concurrent_URLs_example():
    for url in URLS:
        try:
            data = load_url(url, 60)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
    print(\n)


non_concurrent_URLs_example()

"""

elapsed_time = timeit.timeit(code_to_time, number=10)/10            #get the average of 10 cycles
print(elapsed_time)   
