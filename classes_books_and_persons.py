from datetime import datetime, timedelta
from random import randrange

class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  def __repr__(self):
    return 'The book\'s title is {title}, it\'s author is {author} and it has {pages} pages..'.format(title = self.title, author = self.author, pages = self.pages)

  def reading_time(self, pace, pages):
    return pages / pace

  def datetime_of_completion(self, reading_time, start_date):
    return start_date + timedelta(hours = reading_time)

  def page_feedback(self, pages):
    if pages <= 200:
      return 'Considering the amount of pages, this is an easy read.'
    elif pages <= 300:
      return 'Considering the amount of pages, this becomes more challenging.'
    else:
      return 'Considering the amount of pages, get ready for a hard but fun time!'

class Person:
  def __init__(self, name, pace, to_read, read, stars):
    self.name = name
    self.pace = pace
    self.to_read = to_read
    self.read = read
    self.stars = stars

  def __repr__(self):
    return 'My name is {name}, I read {pace} pages per hour, and the book(s) on my to-read list is/are {to_read}. I have already read {read}. I rated it/them {stars} stars respectively.'.format(name = self.name, pace = self.pace, to_read = self.to_read, read = self.read, stars = self.stars)

  def read_next(self, to_read):
    number_of_picks = len(to_read)
    random_pick = randrange(0, number_of_picks)
    return to_read[random_pick]

  def time_to_start(self, starting_date):
    acceptable_start = datetime(2024, 4, 27, 6)
    acceptable_end = datetime(2024, 4, 27, 21)
    if starting_date <= acceptable_end and starting_date >= acceptable_end:
      return 'Looks like you have time to read.'
    elif starting_date < acceptable_start:
      return 'It\'s too early to start reading now.'
    else:
      return 'It\'s too late to start reading now.'

  def rating(self, stars):
    self.zero_stars = 0
    self.one_stars = 0
    self.two_stars = 0
    self.three_stars = 0
    self.four_stars = 0
    self.five_stars = 0
    
    rating = ''

    for item in stars:
      if item == 0:
        self.zero_stars += 1
      if item == 1:
        self.one_stars += 1
      if item == 2:
        self.two_stars += 1
      if item == 3:
        self.three_stars += 1
      if item == 4:
        self.four_stars += 1
      if item == 5:
        self.five_stars += 1
    
    rating += 'I rated {zero_stars} book(s) 0 stars, a shame.\n'.format(zero_stars = self.zero_stars)
    rating += 'I rated {one_stars} book(s) 1 star, a bummer.\n'.format(one_stars = self.one_stars)
    rating += 'I rated {two_stars} book(s) 2 stars, I guess.\n'.format(two_stars = self.two_stars)
    rating += 'I rated {three_stars} book(s) 3 stars, which is okay.\n'.format(three_stars = self.three_stars)
    rating += 'I rated {four_stars} book(s) 4 stars, amazing!\n'.format(four_stars = self.four_stars)
    rating += 'I rated {five_stars} book(s) 5 stars, spectacular!.'.format(five_stars = self.five_stars)
    
    return rating
        

def formatter(list):
  string = ''
  for index in range(len(list)):
    if index == 0:
      string += str(list[index])
    elif index == len(list) - 1:
      string += ' and ' + str(list[index])
    else:
      string += ', ' + str(list[index])
  return string

starting_date = datetime(2024, 4, 27, 4)
# print(starting_date)

book1 = Book('Stoner', 'John Williams', 288)
book2 = Book('The Fifth Season', 'N.K. Jemisin', 468)
book3 = Book('The Mars Room', 'Rachel Kushner', 338)
# print(book1)
# print(book2)
# print(book3)

person1_books_to_read = ['Stoner', 'The Mars Room']
person1_books_read = ['The Fifth Season']
person1_books_stars = [4, 3]
person1 = Person('Laura', 40, formatter(person1_books_to_read), formatter(person1_books_read), formatter(person1_books_stars))
# print(person1)

person2_books_to_read = ['The Mars Room', 'Stoner']
person2_books_read = ['The Fifth Season']
person2_books_stars = [4]
person2 = Person('Kim', 35, formatter(person2_books_to_read), formatter(person2_books_read), formatter(person2_books_stars))
# print(person2)

person3_books_to_read = ['The Fifth Season']
person3_books_read = ['Stoner', 'The Mars Room']
person3_books_stars = [3, 3]
person3 = Person('Johan', 50, formatter(person3_books_to_read), formatter(person3_books_read), formatter(person3_books_stars))
# print(person3)

hours_book1_person1 = book1.reading_time(person1.pace, book1.pages)
ending_date_book1_person1 = book1.datetime_of_completion(hours_book1_person1, starting_date)
feedback_book1 = book1.page_feedback(book1.pages)
# print(hours_book1_person1)
# print(ending_date_book1_person1)
# print(feedback_book1)

random_pick_person1 = person1.read_next(person1_books_to_read)
start_reading_person1  =  person1.time_to_start(starting_date)
ratings_person1 = person1.rating(person1_books_stars)
# print(random_pick_person1)
# print(start_reading_person1)
print(ratings_person1)