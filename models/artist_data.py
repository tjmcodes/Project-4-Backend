
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
        username="India",
        password="Teresa55!",
        email="india@teresa.com",
        artistName="I. Jordan",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/ar_1:1,b_rgb:000000,bo_2px_solid_rgb:2f9cff,c_thumb,e_transition,g_auto:face,q_auto,r_100,w_200/v1659801458/i-jordan-20220530_uofrpv.jpg",
        genre = genre_list,
        location = "Birmingham",
        travel = 0-500,
        totalRatings = 4,
        price = 5000,
        websiteUrl = "https://ra.co/dj/ijordan",
        videoUrl = "https://www.youtube.com/watch?v=tTIP0TUhb7Y",
        optionUrl = "",
        musicUrl = "https://open.spotify.com/artist/5RMLpCv3ic2KtGnqJ7eMG4",
        backgroundCardImage = "https://geo-media.beatport.com/image_size/590x404/3cf3d220-d721-4300-b581-b2e1a0eefbbf.jpg",
        galleryImage1 = "https://res.cloudinary.com/tjmcodes/image/upload/c_fit,h_614,w_500/v1659801523/fred-again-india-jordan-admit-it-1644506636-1000x1000-cover_szebjt.jpg",
        galleryImage2 = "https://res.cloudinary.com/tjmcodes/image/upload/c_fit,h_614,w_500/v1659801569/f311a26e-2572-11ec-b991-0ee6b8365494-972x597_ktj6zo.jpg",
        galleryImage3 = "https://res.cloudinary.com/tjmcodes/image/upload/c_fit,h_614,w_500/v1659802012/i-jordan-for-you-cover-art_yrtfek.jpg",
        bio = "Emerging as one of Europe’s most exciting producers and DJs, India Jordan is a true disciple of high-energy, fast-paced dance music. Having spent the last 10 years holding down residencies and promoting parties across the UK’s North-East, India’s unique brand of vigorous productions have earned them a spot as one of the country’s most promising talents.",
        fbUrl = "https://www.facebook.com/i.jordan.music/",
        twitterUrl = "https://mobile.twitter.com/i_jordan",
        youTubeUrl = "https://www.youtube.com/channel/UCgMMGVDV32dPP-l9M-lXf2A",
        instagramUrl = "https://www.instagram.com/i.jordan/?hl=en-gb"
        ),
    ArtistModel(
        username="RiccyM",
        password="Teresa55!",
        email="riccy@teresa.com",
        artistName="Riccy Mitchell",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/ar_1:1,b_rgb:000000,bo_2px_solid_rgb:2f9cff,c_thumb,e_transition,g_auto:face,q_auto,r_100,w_200/v1659800976/ab6761610000e5eb1e9f7c130b859ec0922a831c_al6qk1.jpg",
        genre = genre_list,
        location = "London",
        travel = 0-50,
        totalRatings = 4,
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
        fbUrl = "https://www.facebook.com/riccymitchell",
        twitterUrl = "https://twitter.com/riccymitchell",
        youTubeUrl = "https://www.youtube.com/c/RiccyMitchell",
        instagramUrl = "https://www.instagram.com/riccymitchell/"
    ),
    ArtistModel(
        username="JoshS",
        password="Teresa55!",
        email="josh@teresa.com",
        artistName="Josh Savage",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/ar_1:1,b_rgb:000000,bo_2px_solid_rgb:2f9cff,c_thumb,e_transition,g_auto:face,q_auto,r_100,w_200/v1659899266/Josh-Savage-01_l37ev7.jpg",
        genre = genre_list,
        location = "London",
        travel = 0-50,
        totalRatings = 4,
        price = 500,
        websiteUrl = "https://www.joshsavagemusic.com/",
        videoUrl = "https://www.youtube.com/watch?v=FZI1hzh3STM",
        optionUrl = "",
        musicUrl = "https://open.spotify.com/artist/0doJV5UAkt2hGKYrpNsHY5?si=Ok-POxBiQE-_tSclHynemw&nd=1",
        backgroundCardImage = "https://novamusic.blog/wp-content/uploads/2020/04/Josh-Savage-performing-live-scaled.jpg",
        galleryImage1 = "https://hotvox.co.uk/wp-content/uploads/2020/03/Josh-Savage-02.jpg",
        galleryImage2 = "http://www.rightchordmusic.co.uk/wp/wp-content/uploads/2014/04/Josh-368.jpg",
        galleryImage3 = "https://blog.reverbnation.com/wp-content/uploads/2016/04/1447931981_josh_savamge_RVA_color-31.png",
        bio = "With no management, publishing or record support to speak of, singer/songwriter Josh Savage has blazed a bright trail through the music industry, which should serve as a beacon to any musician looking to make a name for themselves in the unrecognisable 21st Century landscape. “The most promising new young artist to emerge in Winchester in years” has built a loyal fanbase one living room at a time, and his sprawling career has seen him supporting acts as diverse as Razorlight, Rizzle Kicks, Reverend and the Makers, Roll Deep, and even some acts with names that dont begin with R such as Benjamin Francis Leftwich, John Hiatt, Catfish & The Bottlemen & Ward Thomas. ",
        fbUrl = "https://www.facebook.com/joshsavagemusic",
        twitterUrl = "https://twitter.com/joshdjsavage",
        youTubeUrl = "https://www.youtube.com/user/joshsavagemusic/",
        instagramUrl = "https://www.instagram.com/joshsavagemusic/"
    )

]

artist_comments_list = [
    ArtistCommentModel(content="This is a great coffee", rating=4, artist_id=1,  venue_id =1)]
