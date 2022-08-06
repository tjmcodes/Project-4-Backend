
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
        username="RiccyM",
        password="Teresa55!",
        email="riccy@teresa.com",
        artistName="Riccy Mitchell",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/v1656844656/my_found_sounds_pics/r673ncsqnjycl9pztuze.jpg",
        genre = genre_list,
        location = "London",
        travel = 0-50,
        price = 500,
        websiteUrl = "https://www.riccymitchell.com/",
        videoUrl = "https://www.youtube.com/watch?v=Qv8jJApYAcI",
        optionUrl = "",
        musicUrl = "https://open.spotify.com/artist/0GiOZnYXdGWk8gBitd68wa?si=LknFXRXARua9-17PUIxQJg&nd=1",
        backgroundCardImage = "https://static.wixstatic.com/media/771c27_ee884f5bd7c84dcd8ed1faba69b2039b~mv2.jpg/v1/fill/w_1060,h_944,fp_0.50_0.50,q_85,usm_0.66_1.00_0.01,enc_auto/771c27_ee884f5bd7c84dcd8ed1faba69b2039b~mv2.jpg",
        galleryImage1 = "https://scontent-lhr8-1.cdninstagram.com/v/t51.2885-15/244346220_392202005734530_8391163979238528686_n.jpg?stp=dst-webp_e35_s640x640_sh0.08&cb=9ad74b5e-be52112b&_nc_ht=scontent-lhr8-1.cdninstagram.com&_nc_cat=106&_nc_ohc=IEf99bkdhewAX_j05UW&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=MjY3NzY0NTA5MTU4Nzc5MjcwMQ%3D%3D.2-ccb7-5&oh=00_AT8njOddOQmSLre_b3fWkM8D0EMDtOGvh02SUeTVlL0u9Q&oe=62F591FD&_nc_sid=30a2ef",
        galleryImage2 = "https://subfranticmusic.com/wp-content/uploads/2021/03/XDS_8580-768x1152.jpg",
        galleryImage3 = "https://subfranticmusic.com/wp-content/uploads/2021/03/King-Artwork-1024x1024.png",
        bio = "Riccy has been working as a writer for various UK artists and has spent time on the road and in the studio singing for some of his peers, such as, Michael Kiwanuka, Emeli Sande & Jake Isaac; he was also personally given the opportunity to open for soul diva and legend Jocelyn Brown at Camden’s Jazz Cafe",
        socialMediaUrl1 = "https://www.facebook.com/riccymitchell",
        socialMediaUrl2 = "https://twitter.com/riccymitchell",
        socialMediaUrl3 = "https://www.youtube.com/c/RiccyMitchell",
        socialMediaUrl4 = "https://www.instagram.com/riccymitchell/"
    ),
    ArtistModel(
        username="India",
        password="Teresa55!",
        email="india@teresa.com",
        artistName="I. Jordan",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/v1656610273/my_found_sounds_pics/vnr9dp4owptjkzxnw2qq.jpg",
        genre = genre_list,
        location = "Birmingham",
        travel = 0-500,
        price = 5000,
        websiteUrl = "https://ra.co/dj/ijordan",
        videoUrl = "https://www.youtube.com/watch?v=tTIP0TUhb7Y",
        optionUrl = "",
        musicUrl = "https://open.spotify.com/artist/5RMLpCv3ic2KtGnqJ7eMG4",
        backgroundCardImage = "https://static.wixstatic.com/media/771c27_ee884f5bd7c84dcd8ed1faba69b2039b~mv2.jpg/v1/fill/w_1060,h_944,fp_0.50_0.50,q_85,usm_0.66_1.00_0.01,enc_auto/771c27_ee884f5bd7c84dcd8ed1faba69b2039b~mv2.jpg",
        galleryImage1 = "https://imgproxy.ra.co/_/quality:100/w:484/rt:fill/plain/https://static.ra.co/images/reviews/2022/fred-again-india-jordan-admit-it-1644506636-1000x1000-cover.jpg",
        galleryImage2 = "https://d3vhc53cl8e8km.cloudfront.net/hello-staging/wp-content/uploads/2021/10/05002909/f311a26e-2572-11ec-b991-0ee6b8365494-972x597.jpg",
        galleryImage3 = "https://e.snmc.io/i/600/s/dbdb187959d8091f164dbf4cf330692b/8133555/i-jordan-for-you-cover-art.jpg",
        bio = "Emerging as one of Europe’s most exciting producers and DJs, India Jordan is a true disciple of high-energy, fast-paced dance music. Having spent the last 10 years holding down residencies and promoting parties across the UK’s North-East, India’s unique brand of vigorous productions have earned them a spot as one of the country’s most promising talents.",
        socialMediaUrl1 = "https://www.facebook.com/i.jordan.music/",
        socialMediaUrl2 = "https://mobile.twitter.com/i_jordan",
        socialMediaUrl3 = "https://www.youtube.com/channel/UCgMMGVDV32dPP-l9M-lXf2A",
        socialMediaUrl4 = "https://www.instagram.com/i.jordan/?hl=en-gb"
        )
]

artist_comments_list = [
    ArtistCommentModel(content="This is a great coffee", rating=4, artist_id=1,  venue_id =1)]
