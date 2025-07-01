select * from bookings.boarding_passes
	where flight_id=245;

select passenger_id, passenger_name, tickets.ticket_no, 
						seats.seat_no, seats.fare_conditions
	from (
		select bookings.ticket_flights.ticket_no,fare_conditions,seat_no 
		from bookings.ticket_flights LEFT JOIN bookings.boarding_passes
		on bookings.ticket_flights.ticket_no=bookings.boarding_passes.ticket_no
			AND
	   	   bookings.ticket_flights.flight_id=bookings.boarding_passes.flight_id
		where bookings.ticket_flights.flight_id=245
	) AS seats
	LEFT JOIN bookings.tickets 
	on bookings.tickets.ticket_no=seats.ticket_no;
