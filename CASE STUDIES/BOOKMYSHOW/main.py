from controllers.ticket_booking import BookingController
from controllers.user import UserController
from controllers.movie import MovieController
from models.movie import Movie , MovieGenre
from datetime import datetime

def main():
    booking_controller = BookingController()
    movie_controller   = MovieController()
    user_controller    = UserController()
    
    # user done
    name = "Gojo"
    email = "Gojo@ttc.com"
    password = "gojo123"
    user = user_controller.create_user(name, email, password)["user"]
    
    
    # movie done
    movie = Movie()
    movie.title = "JJK: Endgame"
    movie.genre = MovieGenre.adventure
    movie.release_date = datetime(2010, 7, 16)
    movie.language = "English"
    movie.duration = 148
    jjk_movie = movie_controller.add_movie(movie)
    
    # show todo
    
    
    # cinema todo
    
    # hall todo
    
    # seat todo
    
    # showseat todo
    
    
    booking = booking_controller.create_booking(show_id=1, seat_ids=[1, 2], user_id=user.id)
    # Confirm booking
    payment_data = {
        "amount": booking.amount,
        "payment_method": "credit_card",
        "card_number": "1234-5678-9012-3456"
    }
    booking_controller.confirm_booking(booking.id, payment_data)

    # Retrieve booking
    retrieved_booking = booking_controller.get_booking(booking.id)
    
    return retrieved_booking

if __name__ == "__main__":
    main()