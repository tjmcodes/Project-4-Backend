import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/VenuesandArtists_db')
secret = os.getenv('SECRET', 'AlienToughPreparatoryPlacid2')

