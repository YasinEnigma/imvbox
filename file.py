# -*- coding: utf-8 -*-

import requests 
import bs4
import json

requests.encoding = "UTF-8U"
print("\n\nProgram Started!\n")

url = "https://www.imvbox.com/movies/all/all/{}/all/all/4"


try:
	with open( "movie_data.json", 'w') as movie_data : 
		for number in range(1 , 56):
			response = requests.get(url.format(number))
			response.encoding= "UTF-8"

			page_data = bs4.BeautifulSoup(response.text , "html.parser")

			movies = page_data.findAll("div" , attrs={"class" : "item item"})

			# for access the movie film, detail information about film
			links = []
			for movie in movies:
			    links.append(movie.find("a").get("href"))

			for link in links:
				link_req = requests.get(link)
				link_req.encoding = "UTF-8"
				movie_detail = bs4.BeautifulSoup(link_req.text , "html.parser")
				movie_info = movie_detail.find("div" , attrs={"class" : "movie-details-holder "})

				movie_name = movie_info.find("h2" , attrs={"class" : "movie-full-title jump"}).text

				movie_featue = movie_info.findAll("li" , attrs={"class" : "vertical-border"})
				movie_year = movie_featue[0].a.text
				movie_duration = movie_featue[1].text
				genre_list = []
				for genre in movie_featue[2].findAll("a"):
					genre_list.append(genre.text)
				movie_genre = genre_list

				movie_storyline = movie_info.find("div" , attrs={"id" : "synopsis"}).p.text

				movie_userRating = movie_info.find("div"  , attrs = {"class" : "item-rating rating-int"}).get("rel")

				movie_cast = movie_info.find("div" , attrs={"id":"cast"})
				movie_cast_row = movie_cast.findAll("div" , attrs={"class" : "row"})
				movie_cast_character_info = movie_cast.findAll("div" , attrs={"class" : "col-md-4"})
				movie_cast_character_data = movie_cast.findAll("div" , attrs={"class" : "col-md-7"})


				movie_character_info = {}
				movie_character_info["Name"] = movie_name
				movie_character_info["Production Year"] = movie_year
				movie_character_info["Duration"] = movie_duration
				movie_character_info["Genre"] = movie_genre
				movie_character_info["Story Line"] = movie_storyline
				movie_character_info["User Rating"] = movie_userRating



				for i in range(len(movie_cast_character_data)):
					character_list = []
					for name in movie_cast_character_data[i].findAll("a"):
						character_list.append(name.text)
					movie_character_info["{}".format(movie_cast_character_info[i].strong.text)] = character_list


				movie_data.write(json.dumps(movie_character_info))
				movie_data.write("\n\n")
				print("{}".format(link)+" Done!\n")
				print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
			print("Page {} Done!\n".format(number))
			print("=======================================================================================================================================================================")

	print("\n\nProgram End!\n")

except :
	print("Connection Refused!")


	    
	