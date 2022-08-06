
from models.venue import VenueModel
from models.venue_comments import VenueCommentModel
from models.types import TypeModel

venue_type_list = [
    TypeModel(type="Outdoor"),
    TypeModel(type="Indoor"),
    ]

venue_list = [
    VenueModel(
        email="Windmill@Windmill.com",
        username="Bobby", 
        password="Windmill1",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/v1656844656/my_found_sounds_pics/r673ncsqnjycl9pztuze.jpg",
        title="Bob Smith",
        role="Manager",
        venueName="The Windmill",
        type = venue_type_list,
        venueImage="https://upload.wikimedia.org/wikipedia/commons/6/6a/Windmill%2C_Brixton_Hill%2C_SW2_%283151353450%29.jpg",
        location="london",
        address="22 Blenheim Gardens, Brixton Hill, London SW2 5BZ", 
        budget=100, 
        websiteUrl="https://www.windmillbrixton.co.uk/", 
        videoUrl="", 
        optionUrl="", 
        backgroundCardImage="https://i0.wp.com/www.brixtonbuzz.com/wp-content/uploads/2012/02/windmill-brixton-1.jpg?resize=640%2C433",
        galleryImage1="https://i0.wp.com/www.brixtonbuzz.com/wp-content/uploads/2012/02/windmill-brixton-1.jpg?resize=640%2C433", 
        galleryImage2="", 
        galleryImage3="", 
        description="If there was ever a venue that proved true the old maxim, never judge a book by its cover, The Windmill is it. Though this little back-street pub couldn’t look more unassuming if it tried, its reputation as a champion of great music, and a great place to catch a live gig stretches far and wide. The Windmill has been a lot of things in its lifetime, but morphed into a music venue in the early 2000s simply by chance, when somebody realised that its regular crowd possessed a wealth of skills in areas such as sound engineering, promotion, and music production. Sinche bar has been named as one of the best live music venues not only in London but in the country",
        socialMediaUrl1="https://www.instagram.com/windmillbrixton/?hl=en", 
        socialMediaUrl2="https://en-gb.facebook.com/windmillbrixton/", 
        socialMediaUrl3="https://twitter.com/WindmillBrixton",
        socialMediaUrl4="https://www.youtube.com/watch?v=qpegm3h79y0"),

    VenueModel(
        email="dublincastle@dublincastle.com",
        username="Patrick", 
        password="Dublincastle1",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/v1656844656/my_found_sounds_pics/r673ncsqnjycl9pztuze.jpg",
        title="Micheal Higgins",
        role="owner",
        venueName="The Dublin Castle",
        type = venue_type_list,
        venueImage="https://s3.amazonaws.com/sndb/uploads/photo/image/418883/large_image.jpg",
        location="london",
        address="94 Parkway, London NW1 7AN", 
        budget=400, 
        websiteUrl="https://thedublincastle.com/", 
        videoUrl="https://www.youtube.com/watch?v=hVI9YoYLQ7k", 
        optionUrl="", 
        backgroundCardImage="https://cdn.londonandpartners.com/asset/d695548057eb86760476f239b35fc8f5.jpg",
        galleryImage1="https://cdn.londonandpartners.com/asset/d695548057eb86760476f239b35fc8f5.jpg", 
        galleryImage2="", 
        galleryImage3="", 
        description="A favourite of the late Amy Winehouse, who could often be caught serving pints behind the bar, Dublin Castle has courted an outstanding reputation as a live music venue since the 1970s, when the band Madness secured a residency there — though they had to pretend to be a blues band just to get their first gig, having been turned down previously. The pub, which was a mainstay of the 90s Britpop movement, has been run by the same family for nearly 30 years, and is a self proclaimed ‘indie rock institution’, rather than just another music venue.",
        socialMediaUrl1="https://twitter.com/thedublincastle", 
        socialMediaUrl2="https://www.youtube.com/thedublincastletv", 
        socialMediaUrl3="https://www.instagram.com/thedublincastle/?hl=en",
        socialMediaUrl4="https://en-gb.facebook.com/groups/thedublincastle/"),

        VenueModel(
        email="jamboree@jamboree.com.",
        username="jamboree1", 
        password="jamboree1!",
        profileImage = "https://res.cloudinary.com/tjmcodes/image/upload/v1656844656/my_found_sounds_pics/r673ncsqnjycl9pztuze.jpg",
        title="Jane Bedford",
        role=" Manager",
        venueName="The Jamboree",
        type = venue_type_list,
        venueImage="https://images.cm.archant.co.uk/resource/image/3587104/landscape_ratio16x9/448/252/47ba54364c585125d57c68751e5f2827/uH/el-10-jamboree-campaign-5-cabl.jpg",
        location="london",
        address="6 St Chads Place,London, WC1X 9HH", 
        budget=400, 
        websiteUrl="https://www.jamboreevenue.co.uk/", 
        videoUrl="", 
        optionUrl="", 
        backgroundCardImage="https://www.jamboreevenue.co.uk/wp-content/uploads/2011/05/jamboree.jpg",
        galleryImage1="https://www.jamboreevenue.co.uk/wp-content/uploads/2011/05/jamboree.jpg", 
        galleryImage2="https://images.cm.archant.co.uk/resource/blob/3587096/e1c96eaf4761d98d509063bab2fc3386/el-10-jamboree-campaign-1-cabl-data.jpg", 
        galleryImage3="https://i0.wp.com/www.eastlondonlines.co.uk/ell_wp/wp-content/uploads/2018/03/interior.jpg?resize=750%2C422", 
        description="Peel black the velvet curtain and step-inside a home-made den of world music with devil may care European bohemia, crackled walls and mismatched furniture, raucous evenings, a rag-tag of eccentric characters, flowing absinthe and mad dancing. Order local ale from the charmingly peculiar bar man, possibly wearing a ripped ladies' pinafore with a string of Pat Butcher pearls … and pull up a seat to watch the Mad Hatter's tea party begin.",
        socialMediaUrl1="https://www.instagram.com/jamboreevenue/", 
        socialMediaUrl2="https://www.youtube.com/user/jamboreevenue", 
        socialMediaUrl3="https://www.facebook.com/jamboreelimehouse",
        socialMediaUrl4="https://twitter.com/jamboreevenue"),
})

]

venue_comments_list = [
    VenueCommentModel(content="This is a great Venue", rating=4, venue_id=1, artist_id=1)]

