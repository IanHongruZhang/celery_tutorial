from celery_app import crawler1
from celery_app import crawler2

URL_BASH_1 = "https://www.thepaper.cn/"
URL_BASH_2 = "https://www.jiemian.com/lists/32.html"

def manage_crawl_task(url1,url2):
	crawler1.crawl_thepaper.apply_async(args=(url1,))
	crawler2.crawl_jiemian.apply_async(args=(url2,))

if __name__ == '__main__':
	manage_crawl_task(URL_BASH_1,URL_BASH_2)