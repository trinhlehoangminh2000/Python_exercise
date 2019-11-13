import newspaper
from newspaper import Article
import concurrent.futures


def get_headlines():

    URLs = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:              #Create 5 executors
        future_to_url = {executor.submit(load_url,url): url for url in URLs}            #Assign each a function load_url with a parameter 'url'
            
        for future in concurrent.futures.as_completed(future_to_url):                   #For each future wait until completed to print the result
            url = future_to_url[future]
            try:
                print(future.result())
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc),'\n')
                
def load_url(url):
    res = newspaper.build(url, memoize_articles=False)
    articles ="The headlines from "+url+" are: \n" 
    for i in range(1,6):
        art = res.articles[i]
        art.download()
        art.parse()
        articles += (art.title +'\n')                                                   #Gather all the headlines in a single String variables
    return articles
   

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=3)/3             
    print(elapsed_time) 
