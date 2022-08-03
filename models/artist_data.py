
# ! Import user
from models.artist import ArtistModel
from models.artist_comments import ArtistCommentModel
from models.genres import GenreModel

genre_list = [
    GenreModel(genre="Pop"),
    GenreModel(genre="Acoustic"),
    GenreModel(genre="Lofi")
]

# ! List of users
artist_list = [
    ArtistModel(
        username="Teresa",
        password="Teresa55!",
        email="teresa@teresa.com",
        artistName="Layla",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/v1658916228/mfykapjyjasaxfdhfrbt.jpg",
        genre = genre_list,
        location = "London",
        travel = 0-50,
        price = 500,
        websiteUrl = "https://www.insomniac.com/music/artists/india-jordan/",
        videoUrl = "https://www.youtube.com/watch?v=P5YJKW3BAiQ",
        optionUrl = "",
        musicUrl = "https://open.spotify.com/artist/5RMLpCv3ic2KtGnqJ7eMG4?autoplay=true",
        backgroundCardImage = "https://static.ra.co/images/news/2022/india-jordan-new-name.jpeg",
        galleryImage1 = "",
        galleryImage2 = "",
        galleryImage3 = "",
        bio = "Emerging as one of Europes most exciting producers and DJs, India Jordan is a true disciple of high-energy, fast-paced dance music. Having spent the last 10 years holding down residencies and promoting parties across the UK’s North-East, India’s unique brand of vigorous productions have earned them a spot as one of the country’s most promising talents.",
        socialMediaUrl1 = "",
        socialMediaUrl2 = "",
        socialMediaUrl3 = ""
        )
]

artist_comments_list = [
    ArtistCommentModel(content="This is a great coffee", artist_id=1,  venue_id =1)]
