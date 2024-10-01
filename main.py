import Scrapy as S

L = S.search_subreddits('mental')
S.red_dat_scraper(L[:10],50,500,300,'health','mental_posts.csv','mental_comms.csv')
