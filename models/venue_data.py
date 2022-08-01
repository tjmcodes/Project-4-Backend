from models.venue import VenueModel
from models.venue_comments import VenueCommentModel



venue_list = [
    VenueModel(
        username="Windmill", 
        password="Windmill1",
        email="Windmill@Windmill.com", 
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
    VenueCommentModel(content="This is a great coffee", venue_v_id=1)]
