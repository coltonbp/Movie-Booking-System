class Review:
    def __init__(self, movie, review_text, rating):
        self.movie = movie
        self.review_text = review_text
        self.rating = rating
    
    def get_movie(self):
        return self.movie
    
    def get_review_text(self):
        return self.review_text
    
    def get_rating(self):
        return self.rating
    
    def set_movie(self, movie):
        self.movie = movie
        
    def set_review_text(self, review_text):
        self.review_text = review_text
        
    def set_rating(self, rating):
        self.rating = rating
        
def create_review(movies, movie, review_text, rating):
    found = False
    for i in range(len(movies)):
        if movies[i].get_title() == movie.get_title():
            found = True
            # Update movie rating
            total_rating = movies[i].get_rating() * len(movies[i].get_reviews()) + rating
            new_rating = total_rating / (len(movies[i].get_reviews()) + 1)
            movies[i].set_rating(new_rating)
            # Add review to movie
            movies[i].add_review(Review(movie, review_text, rating))
            print("Review added successfully!")
            break
    if not found:
        print("Error: Movie not found")

def see_reviews(movies, movie):
    found = False
    for i in range(len(movies)):
        if movies[i].get_title() == movie.get_title():
            found = True
            reviews = movies[i].get_reviews()
            if len(reviews) == 0:
                print("No reviews found for this movie")
            else:
                print(f"Reviews for {movie.get_title()}:")
                for j in range(len(reviews)):
                    print(f"Review {j+1}:")
                    print(f"Rating: {reviews[j].get_rating()}")
                    print(f"Text: {reviews[j].get_review_text()}")
            break
    if not found:
        print("Error: Movie not found")
