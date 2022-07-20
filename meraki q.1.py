from bs4 import BeautifulSoup
import requests
import pprint 

url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
print(page)
soup=BeautifulSoup(page.text,"html.parser")
print(soup)

def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    # print(main_div)
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")

    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_ratings=[]
    movie_urls=[]

    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "."not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
        # print(movie_ranks)

        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)
        

        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_realease.append(year)

        imdb_rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)

        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)

    top_movies=[]
    movie_details={'position':'','name':'','year':'','rating':'','url':''}
    for i in range(0,len(movie_ranks)):
        movie_details["position"]=int(movie_ranks[i])
        movie_details["name"]=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        movie_details["year"]=int(year_of_realease[i])
        movie_details["rating"]=float(movie_ratings[i])
        movie_details["url"]=movie_urls[i]
        top_movies.append(movie_details)
        movie_details={'position':'','name':'','year':'','rating':'','url':''}
        #top_movies.append(details.copy())

    return(top_movies)
# pprint.pprint(scrap_top_list())
# scrapped=scrap_top_list()
scrap=scrap_top_list()

##task 4


# def scrap_movie_details(movie_url):
#     page=requests.get(movie_url)
#     soup=BeautifulSoup(page.text,'html.parser')


#     title_div=soup.find('div',class_="title_wrapper").h1.get_text()
#     movie_name=""
#     for i in title_div:
#         if '('not in i:
#             movie_name=(movie_name+i).strip()
#         else:
#             break

# sub_div=soup.find('div',class_="subtext")

# runtime=sub_div.find('time').get_text().strip()
# runtime_hours=int(runtime[0])*60
# if 'min' in sub_div:
#     runtime_minutes=int(movie_runtime[3:].strip('min'))
#     movie_runtime=runtime_hours+runtime_minutes
# else:
#     movie_runtime=runtime_hours

# gener=sub_div.find_all('a')
# gener.pop()
# movie_gener=[i.get_text() for i in gener]

# summary=soup.find('div',class_="plot_summary")

# movie_bio=summary.find('div',class_="summary_text").get_text().strip()

# director=summary.find('div',class_="credit_summary_item")
# director_list=director.find_all('a')
# movie_director=[i.get_text().strip() for i in director_list]

# extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
# list_of_divs=extra_details.find_all('div')
# for div in list_of_divs:
#     tag_h4=div.find_all('h4')
#     for text in tag_h4:
#         if 'language:'in text:
#             tag_anchor=div.find_all('a')
#             movie__language=[language.get_text() for language in tag_anchor]
#         elif 'Country:' in text:
#             tag_anchor=div.find_all('a')
#             movie_country=''.join([country.get_text() for country in tag_anchor])
# movie_poster_link=soup.find('div',class_="poster").a['href']
# movie_poster="https://www.imdb.com"+movie_poster_link

# movie_detail_dic={'name':'','director':'','bio':'','runtime':'','gener':'','language':'','country':'','poster_img_url':'',}

# movie_detail_dic['name']=movie_name
# movie_detail_dic['director']=movie_director
# movie_detail_dic['bio']=movie_bio
# movie_detail_dic['runtime']=movie_runtime
# movie_detail_dic['grner']=movie_gener
# movie_detail_dic['language']=movie__language
# movie_detail_dic['country']=movie_country
# movie_detail_dic['poster_img_url']=movie_poster
# return movie_detail_dic
# url1=scrap[0]['url']
# movie_detail=scrap_movie_details(url1)
# print(movie_detail)








            





































###task2 and 3 task

# def group_by_year(movies):
#     years=[]
#     for i in movies:
#         year=i["year"]
#         if year not in years:
#             years.append(year)
#     movie_dict={i:[]for i in years}
#     for i in movies:
#         year=i["year"]
#         for x in movie_dict:
#             if str(x)==str(year):
#                 movie_dict[x].append(i)
#     return movie_dict 

# print(group_by_year(scrapped))
