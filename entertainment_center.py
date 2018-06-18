import media
import fresh_tomatoes



#Create the Movie objects
interstellar = media.Movie("Interstellar",
                        "A team of explorers travel through a wormhole in space"
                           " in an attempt to ensure humanity's survival.",
                        "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

ex_machina = media.Movie("Ex Machina",
                        "A young programmer is selected to participate in a"
                        "ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.",
                        "https://m.media-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=EoQuVnKhxaM")

shutter_island = media.Movie("Shutter Island",
                        "In 1954, a U.S. Marshal investigates the disappearance"
                        "of a murderer, who escaped from a hospital for the"
                        "criminally insane.",
                        "https://m.media-amazon.com/images/M/MV5BYzhiNDkyNzktNTZmYS00ZTBkLTk2MDAtM2U0YjU1MzgxZjgzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=YDGldPitxic")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, finding"
                        "solace and eventual redemption through acts of common decency.",
                        "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

godfather = media.Movie("The Godfather",
                        "The aging patriarch of an organized crime dynasty"
                        "transfers control of his clandestine empire to his"
                        "reluctant son.",
                        "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,704,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

batman = media.Movie("Batman Begins",
                        "After training with his mentor, Batman begins his fight"
                        "to free crime-ridden Gotham City from the corruption"
                        "that Scarecrow and the League of Shadows have cast"
                        "upon it.",
                        "https://m.media-amazon.com/images/M/MV5BZmUwNGU2ZmItMmRiNC00MjhlLTg5YWUtODMyNzkxODYzMmZlXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX750_AL_.jpg",
                        "https://www.youtube.com/watch?v=neY2xVmOfUM")

#Put all movies objects inside an array
movies = [interstellar, ex_machina, shutter_island, shawshank_redemption,
          godfather, batman]

#Call open_movies method to open up the browser and display the movies
fresh_tomatoes.open_movies_page(movies)
