
from models.venue import VenueModel
from models.venue_comments import VenueCommentModel
from models.types import TypeModel

venue_type_list = [
    TypeModel(type="Outdoor"),
    TypeModel(type="Indoor"),
    TypeModel(type="Boat"),
    TypeModel(type="House"),
    TypeModel(type="Museum"),
    TypeModel(type="other")
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
        backgroundCardImage="",
        galleryImage1="", 
        galleryImage2="", 
        galleryImage3="", 
        description="", 
        socialMediaUrl1="", 
        socialMediaUrl2="", 
        socialMediaUrl3=""),

]

venue_comments_list = [
    VenueCommentModel(content="This is a great Venue", rating=4, venue_id=1, artist_id=1)]

venue_type_list = [
    TypeModel(type="Outdoor"),
    TypeModel(type="Indoor"),
    TypeModel(type="Boat"),
    TypeModel(type="House"),
    TypeModel(type="Museum"),
    TypeModel(type="other")
    ]