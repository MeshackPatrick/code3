from models import Restaurant, Customer, Review
from database import session

# Create sample data for testing
restaurant1 = Restaurant(name="Restaurant A", price=3)
restaurant2 = Restaurant(name="Restaurant B", price=2)

customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Shericie", last_name="Smith")

session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()

# Create reviews
review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
review2 = Review(restaurant=restaurant2, customer=customer1, star_rating=6)
review3 = Review(restaurant=restaurant1, customer=customer2, star_rating=3)

session.add_all([review1, review2, review3])
session.commit()
