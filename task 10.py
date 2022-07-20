import json
with open("Task5.json","r") as file:
    data1=json.load(file)
def language_and_directors(movie_list):
    Dict={}
    for movies in movie_list:
        for Director in movies:
            if Director=="Director:":
                Dict[movies[Director]]={}
                print(Dict)
    for i in range(len(movie_list)):
        for Director in Dict:
            if Director in movie_list[i]["Director:"]:
                for language in movie_list[i]:
                    if language=="Original Language:":
                        a=movie_list[i]["Original Language:"]
                        Dict[Director][a]=0
    for i in range(len(movie_list)):
        for Director in Dict:
            if Director in movie_list[i][ "Director:"]:
                for language in movie_list[i]:
                    if language=="Original Language:":
                        for l in Dict[Director]:
                            Dict[Director][l]+=1
    return Dict
Director_language=language_and_directors(data1)
with open("Task10.json","w") as f:
    json.dump(Director_language,f,indent=2)
print(Director_language) 

    