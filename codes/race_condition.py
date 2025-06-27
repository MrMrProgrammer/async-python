import threading

available_seats = 2


class Movie:
    def booking(self, number_of_seats):
        global available_seats

        if number_of_seats <= available_seats:
            print(f'{number_of_seats} seats booked successfully for {threading.current_thread().name} \n')
            available_seats -= number_of_seats
        elif number_of_seats > available_seats:
            print(f'{threading.current_thread().name}, number of seats that you want is greater than available seats')
        else:
            print('All seats are sold out')


movie = Movie()
threads = [
    threading.Thread(target=movie.booking, args=(2,), name='Mohammad'),
    threading.Thread(target=movie.booking, args=(2,), name='Ali'),
]

[t.start() for t in threads]
[t.join() for t in threads]

print(f'Available seats: {available_seats}')
