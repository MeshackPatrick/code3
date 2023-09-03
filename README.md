# Restaurant Review Application

## Overview

This is a Python application for managing restaurant reviews. It includes three main models: `Restaurant`, `Review`, and `Customer`. The application allows customers to leave reviews for restaurants, and it provides various features for querying and managing restaurant reviews.


## Getting Started

To get started with this application, follow these steps:

1. Clone the repository to your local machine:

   
   git clone https://github.com/MeshackPatrick/code3
1. Install the required dependencies using pip:
   pip install -r requirements.txt
2. Run the database migrations to set up the database schema:
    alembic upgrade head
3. Seed the database with sample data using the provided seeds.py script:
    python seeds.py
## Migrations

Before working on the application's features, you need to create a migration for all the tables. In particular, you should create a migration for the reviews table using the attributes specified in the deliverables.

A Review belongs to a Restaurant, and a Review also belongs to a Customer. In your migration, create any columns your reviews table will need to establish these relationships.
The reviews table should also have a star_rating column that stores an integer.

## Object Relationship Methods

The application provides the following object relationship methods:

## Review
Review.customer(): Returns the Customer instance for this review.
Review.restaurant(): Returns the Restaurant instance for this review.
## Restaurant
Restaurant.reviews(): Returns a collection of all the reviews for the restaurant.
Restaurant.customers(): Returns a collection of all the customers who reviewed the restaurant.
## Customer
Customer.reviews(): Returns a collection of all the reviews that the customer has left.
Customer.restaurants(): Returns a collection of all the restaurants that the customer has reviewed.
Make sure to check that these methods work as expected in the application.

## Aggregate and Relationship Methods

The application also provides several aggregate and relationship methods:

## Customer
Customer.full_name(): Returns the full name of the customer, with the first name and last name concatenated, Western style.
Customer.favorite_restaurant(): Returns the restaurant instance that has the highest star rating from this customer.
Customer.add_review(restaurant, rating): Takes a restaurant (an instance of the Restaurant class) and a rating, and creates a new review for the restaurant with the given restaurant_id.
Customer.delete_reviews(restaurant): Takes a restaurant (an instance of the Restaurant class) and removes all their reviews for this restaurant. This operation deletes rows from the reviews table.
## Review
Review.full_review(): Returns a string formatted as follows: "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars."
## Restaurant
Restaurant.fanciest() (class method): Returns one restaurant instance for the restaurant that has the highest price.
Restaurant.all_reviews(): Returns a list of strings with all the reviews for this restaurant, formatted as follows:

## Usage

To use the application, you can refer to the provided example usage in the main.py file. Here are some examples of how to interact with the application:

## Get the fanciest restaurant:
    fanciest_restaurant = Restaurant.fanciest()
    print(f"The fanciest restaurant is {fanciest_restaurant.name} with a price rating of {fanciest_restaurant.price}")
## Get all reviews for a restaurant ():
    restaurant_reviews = restaurant_instance.all_reviews()
    print("Reviews for Restaurant A:")
    for review in restaurant_reviews:
    print(review)
## Get the full name of a customer:
    customer = session.query(Customer).first()
    full_name = customer.full_name()
    print(f"Customer's full name: {full_name}")
## Get the favorite restaurant of a customer:
    favorite = customer.favorite_restaurant()
    if favorite:
        print(f"{customer.first_name}'s favorite restaurant is {favorite.name}")
    else:
        print(f"{customer.first_name} has not reviewed any restaurants yet.")

## License

This project is licensed under the MIT License zdc.


