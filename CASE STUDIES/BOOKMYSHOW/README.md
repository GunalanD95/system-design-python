# Design Online Movie Ticketing Platform

### TEMPLATE FOR LLD ROUNDS
- Gathering the Requirements: [ 7 mins ]
- Clarifying the Requirements: [ 7 mins ]
- Use Case Diagram [ 5 mins ]
- Class Diagram [10 mins ]
- SCHEMA DESIGN
- CODING 


## Gathering the Requirements
- A Movie ticket platform basically is -> where users can come and book movies
- A movie can premerie in multiple theaters with different location , timings etc
- There exist multiple cinemas in the city, and the cinema has multiple halls.
- A User should be able to book movie for a particular movie using filters ( location , halls etc )
- The booking system has information on all cinemas present in different cities and the hall information for each cinema
- The system displays a seating layout that identifies booked and available seats so that the customer can choose to reserve available seats
- Once the customer completes the payment for the booking, the seat booking is confirmed and the customer receives an email notification.


## Clarifying the Requirements
- Is there any such limit of booking seats a particular customer can book ? -> yes 10 per user for a movie
- What payment methods can the customer use (for example, credit card or cash)? -> debit card , credit card and upi
- How does the price of movie ticket is decided ? -> it depends on popluarity of the movie 
- How will the system make sure that multiple users do not book the same seat? -> we need to have timeout here
- Does the seat type affect the pricing? -> yes each type may have different price (silver, gold, and platinum)
- Is the same movie being shown at different times in the same cinema/hall? -> it is possible
- will there a be admin -> yes there will be admins ( who can add remove show) , add movie etc

## Design Patterns
- singleton for booking system
- adapter for payment service
- strategy for price assignment ?

## Use Case Diagram
```
Primary Actors
- customers
- system 

Secondary Actors
- admin
- ticket agent
```

## Class Diagram

```
Identity the Nouns
- Customer
- Movie
- Theater
- Hall
- Seat
- Ticket
- Location
- Ticket Agent
- Booking system
```

## SCHEMA DESIGN

