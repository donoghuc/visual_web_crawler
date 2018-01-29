from selenium import webdriver
from bs4 import BeautifulSoup
import collections 
import sys

class web_crawler:
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.url = 'http://www.etsy.com'
		self.depth = 0
		self._count = 0
		self.crawled_list = {}
		self._output = False 
		
	def get_soup(self, url):
		self.browser.get(self.url)
		soup = BeautifulSoup(self.browser.page_source, "html.parser")
		return soup 
		
	def get_urls(self, soup):
		hrefs = [] 
		for link in soup.findAll('a', href=True):
			href = link.get('href', ' ')
			hrefs.append(href)
		return hrefs
		
	def get_title(self, soup):
		try:
			title = soup.find('title').get_text().strip().replace('\n', ' ')
		except:
			title = None
		return title
		
	def bfs_crawl(self, url):
		depth = 0
		#create new queue to store urls to crawl 
		url_queue = collections.deque()
		#add first url to queue
		self.crawled_list[url] = 1
		url_queue.append(url)
		
		while len(url_queue):
			if depth > int(self.depth): 
				return True
			#dequeue url
			url = url_queue.popleft()
			
			if url == 'next':
				url = url_queue.popleft()
				depth += 1
				
			html = self.get_soup(url)
			if not html:
				continue
				
			self._count +=1
			self.get_title(html)
			urls = self.get_urls(html)
			
			if self._output:
				self.print_results(len(urls), depth)
			
			url_queue.append('next')
			for url in urls:
				if url not in self.crawled_list:
					self.crawled_list[url] = 1
					url_queue.append(url)
					
		return True
			
	
	def dfs_crawl(self, url, depth=0):
		if depth > int(self.depth):
			return
		if url in self.crawled_list:
			return 
			
		self.crawled_list[url] = 1
		
		html = self.get_soup(url)
		if not html:
			return
		
		self._count += 1
		self.get_title(html)
		urls = self.get_urls(html)
		
		if self._output:
				self.print_results(len(urls), depth)
		
		for url in urls:
			self.dfs_crawl(url, depth+1) 
	
		return True
	
	def crawl(self, url, method, depth, output=False):
		self._count = 0 
		self.depth = depth
		
		if url in self.crawled_list:
			return 
			
		if method == 'bfs':
			return self.bfs_crawl(url)
		else:
			return self.dfs_crawl(url)

				
	def print_results(self, urls, depth):
		print ("{0}\t{1}".format(urls, depth))
		
	def main(self):
		if len(sys.argv) > 1:
			url = sys.argv[1]
			method = sys.argv[2]
			depth = sys.argv[3]
		else:
			print ('Must specify arguments')
			sys.exit(0)
		print ('URL\tDepth')
		self.crawl(url, method, depth, output=True)
		
if __name__ == '__main__':
	web_crawler().main()
		