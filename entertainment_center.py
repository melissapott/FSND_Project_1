import fresh_tomatoes
import media



kill_bill = media.Movie("Kill Bill Vol. 1",
                        "The Bride seeks vengeance on the assassins who betrayed her.",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME",
                        "2003", "Quentin Tarantino", "http://www.imdb.com/title/tt0266697/")

kill_bill_2 = media.Movie("Kill Bill Vol. 2",
                          "The Bride returns for more revenge",
                          "https://upload.wikimedia.org/wikipedia/en/4/46/Kill_bill_vol_two_ver.jpg",
                          "https://www.youtube.com/watch?v=DUwZQ6-uZ0k",
                          "2004", "Quentin Tarantino", "http://www.imdb.com/title/tt0378194/")

the_matrix = media.Movie("The Matrix",
                         "Dystopian future where humans live in a virtual reality created by machines",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                         "1999", "The Wachowskis", "http://www.imdb.com/title/tt0133093/")

excalibur = media.Movie("Excalibur",
                        "The legend of King Arthur and the quest for the holy grail",
                        "https://upload.wikimedia.org/wikipedia/en/6/60/Excalibur_movie_poster.jpg",
                        "https://www.youtube.com/watch?v=emF-m9qnF5o",
                        "1981", "John Boorman", "http://www.imdb.com/title/tt0082348/")

from_dusk_till_dawn = media.Movie("From Dusk Till Dawn",
                                  "Bank robbers encounter a roadhouse full of vampires",
                                  "https://upload.wikimedia.org/wikipedia/en/f/f0/From_dusk_till_dawn_poster.jpg",
                                  "https://www.youtube.com/watch?v=-bBay_1dKK8",
                                  "1996", "Robert Rodriquez", "http://www.imdb.com/title/tt0116367/")

magnolia = media.Movie("Magnolia",
                       "The narrator recounts three instances of incredible coincidences and suggests that forces greater than chance play important roles in life.",
                       "https://upload.wikimedia.org/wikipedia/en/4/4b/Magnolia_poster.png",
                       "https://www.youtube.com/watch?v=cxcegktcxSM",
                       "1999", "Paul Thomas Anderson", "http://www.imdb.com/title/tt0175880/")

boogie_nights = media.Movie("Boogie Nights",
                            "a dishwasher gets involved in the porn movie industry",
                            "https://upload.wikimedia.org/wikipedia/en/4/41/Boogie_nights_ver1.jpg",
                            "https://www.youtube.com/watch?v=pOk0fsMGyck",
                            "1997", "Paul Thomas Anderson", "http://www.imdb.com/title/tt0118749/")

annie_hall = media.Movie("Annie Hall",
                         "a comedian analyzes his failed relationship",
                         "https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg",
                         "https://www.youtube.com/watch?v=OqVgCfZX-yE",
                         "1977", "Woody Allen", "http://www.imdb.com/title/tt0075686/")

monty_python_holy_grail = media.Movie("Monty Python's Holy Grail",
                                      "a take on the Arthurian legend by the British comedy troupe",
                                      "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",
                                      "https://www.youtube.com/watch?v=urRkGvhXc8w",
                                      "1975", "Terry Gilliam & Terry Jones","http://www.imdb.com/title/tt0071853/" )
                            
movies = [kill_bill, kill_bill_2, the_matrix, excalibur, from_dusk_till_dawn, magnolia, boogie_nights, annie_hall, monty_python_holy_grail]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__module__)
