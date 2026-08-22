

import csv


class Book:
  def __init__(self , name , author , date_release , status):
    
    self.name = name
    
    self.author = author
    
    self.date_release = date_release
    
    self.status = status
    
    
  def __str__(self ):
     return f"""
         book name:  {self.name}  
         book author: {self.author}
         book date release: {self.date_release}
         book status : {self.status}
         
         """
    
    
    
    
    
    

class Library:
  def __init__(self):
    self.books = []
    
    
    
    
    
  def delete(self , name , author ):
    
    if self.books == []:
      print(' list is empty ')
      
    else:
      
      status = "book not found "
      
      for book in self.books:
        
        if book.name == name and  book.author == author :
          
          self.books.remove(book)
          status = ' you deleted this book'
          break
        
      print(status)
        
        
        
        
        
      
      
      
      
 
      
      

    
  def add_book(self , book1 ):
    
    self.books.append( book1 )
    
    print('book added to the list ')
    
    
    
    
  def search_book(self , name  , author):
    if self.books == []:
          print(' list is empty')
     
    else:
      
      status = 'this book does not exist'
      
      for item in self.books:
        if item.name == name and item.author == author:
          status = "this book is available"
          break
        
      print(status)
        
    
      
      
      
        
      
  def show_book(self ):
    
    if self.books == []:
      print('list is empty ')
      
    else:
      for b in self.books:
        print(b)
        
        
        
        
  def save_list(self ):
    
    try:
      outfile = open("book_library.csv" , mode = 'w' , newline='')
      
      csv_data = csv.writer(outfile , delimiter=',')
      
      csv_data.writerow(['book name' , 'author name' , 'data release' , 'staus'])
      
      for b in self.books:
        csv_data.writerow([b.name , b.author , b.date_release ,  b.status])
        
      
      print(' you saved the list ')
      outfile.close()
      
    except Exception as e:
      print(f" you got error : {e} ")
  
    
      
      
      
  def upload(self) :
    try:
      myfile = open("book_library.csv")
      
      csv_data = csv.reader(myfile)
      
      
      for line in csv_data:
        print(line)
        
        
      myfile.close()
      
    
    except Exception as e:
      print(f" you got error : {e} ")
      
      
  
  
  
     
      
  
  
  
  
  
  
lib = Library()


while True:
  
  
  
  
  
  print()
  
  
  print("""
        
  1. Add book to library
  
  2. Search book in library
  
  3. Show book
  
  4. Delete book
  
  5. save list
  
  6. upload list
  
  7. exit
  
 
        
        """)
  
  
  
  
  
  choice = input(' choose your number : ')
  
  
  if choice == '1':
    
    name = input(' enter a book name: ')
    
    author = input(' enter a author name : ')
    
    date_release = input(' enter date of release:  ')
    
    status = input(' enter a book status( just type checked out or exist):  ')
    
    
    book1 = Book( name , author , date_release , status)
    
    lib.add_book( book1 )
    
    
    
    
    
    
  elif choice == '2':
    name = input("enter a book name : ")
    
    author = input("enter a book author : ")
    
    lib.search_book(name , author)
    
    
    
    
  
  elif choice == '3': 
    
    lib.show_book()
    
    
    
    
  elif choice == '4':
     name = input("enter a book name : ")
     
     author = input("enter a book author : ")
     
     
     lib.delete(name , author)
    
    
    
    
    
    
  elif choice == '5':
    lib.save_list()
    
    
    
  elif choice == '6':
    lib.upload()
    
    
    
  elif choice == '7':
    print('you exited')
    break
  
  
  
    
    
    
    