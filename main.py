from models import Restaurant, Customer, Review
from database import session


# Review methods
def customer(self):
    return self.customer


def restaurant(self):
    return self.restaurant


Review.customer = property(customer)
Review.restaurant = property(restaurant)


# Restaurant methods
def reviews(self):
    return self.reviews


def customers(self):
    return [review.customer for review in self.reviews]


Restaurant.reviews = property(reviews)
Restaurant.customers = property(customers)


# Customer methods
def reviews(self):
    return self.reviews


def restaurants(self):
    return [review.restaurant for review in self.reviews]


def full_name(self):
    return f"{self.first_name} {self.last_name}"


def favorite_restaurant(self):
    reviews = self.reviews
    if reviews:
        max_rating_review = max(reviews, key=lambda x: x.star_rating)
        return max_rating_review.restaurant
    return None


def add_review(self, restaurant, rating):
    new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
    session.add(new_review)
    session.commit()


def delete_reviews(self, restaurant):
    reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
    for review in reviews_to_delete:
        session.delete(review)
    session.commit()


Customer.reviews = property(reviews)
Customer.restaurants = property(restaurants)
Customer.full_name = property(full_name)
Customer.favorite_restaurant = property(favorite_restaurant)
Customer.add_review = add_review
Customer.delete_reviews = delete_reviews


# Restaurant methods
@classmethod
def fanciest(cls):
    return session.query(cls).order_by(cls.price.desc()).first()


def all_reviews(self):
    return [f"Review for {self.name} by {review.customer.full_name}: {review.star_rating} stars." for review in
            self.reviews]


Restaurant.fanciest = classmethod(fanciest)
Restaurant.all_reviews = property(all_reviews)

if __name__ == '__main__':
    # Example usage:

    # Get the fanciest restaurant
    fanciest_restaurant = Restaurant.fanciest()
    print(f"The fanciest restaurant is {fanciest_restaurant.name} with a price rating of {fanciest_restaurant.price}")

    # Get all reviews for a restaurant
    restaurant_reviews = restaurant1.all_reviews()
    print("Reviews for Restaurant A:")
    for review in restaurant_reviews:
        print(review)

    # Get the full name of a customer
    customer = session.query(Customer).first()
    full_name = customer.full_name()
    print(f"Customer's full name: {full_name}")

    # Get the favorite restaurant of a customer
    favorite = customer.favorite_restaurant()
    if favorite:
        print(f"{customer.first_name}'s favorite restaurant is {favorite.name}")
    else:
        print(f"{customer.first_name} has not reviewed any restaurants yet.")
