# Django-Library-Manager-App
Powerful Library Management App

This App is made to manage the Library. It has the following features so far:
- Login for Library Staff Members and Library Members(students)
  - Staff Members: They can update, delete or create authors, books. Can renew the book to a borrower and view all the borrowers.
  - Library Members: They can view all the books, authors, copies total and available.
- Admin Panel for Admin or Staff members to add, update, delete users.
- Doesn't give sign up feature to students as the username would be provided by the school or college itself(Else the students of other school or college may also signup).

### Screenshots:I will explain step by step how to use it.

#### This is the Home Page
![Index](https://user-images.githubusercontent.com/51286676/58951936-0b97c380-87b0-11e9-920d-ef70e04289d0.PNG)

#### This is the Admin(Staff Members) Login Page where he gets all the control.
![Admin_Login](https://user-images.githubusercontent.com/51286676/58999688-8e5a6600-8824-11e9-86e9-9c0496b0058f.PNG)

##### Adding users: Now the admin can add the students or the Library members and give them a username with a pattern like firstname-lastname. Example: A student is Rahul Kashyap, then Admin can give him the username as rahul-kaushik.
![Add_User](https://user-images.githubusercontent.com/51286676/58956611-60413b80-87bc-11e9-83e6-f10f0500f605.PNG)

##### Adding Book, Copies, Authors, Languages, Genres: Admin can add the books available in the library.
![Catalog_Panel](https://user-images.githubusercontent.com/51286676/58999789-37a15c00-8825-11e9-9dfd-4d54a474758c.PNG)
![Add_Book](https://user-images.githubusercontent.com/51286676/58999850-87802300-8825-11e9-863b-685c5c0b973f.PNG)
##### Adding Copies available for each books.
![Copies](https://user-images.githubusercontent.com/51286676/58999881-b0081d00-8825-11e9-998e-b4e825b8b93a.PNG)

##### Now the Library Members or students can view all the books available in the Library.
![All_Books](https://user-images.githubusercontent.com/51286676/58956155-50752780-87bb-11e9-9f9a-fc72eb91e77b.PNG)

##### User can view the detail of a book, its summary and its number of copies and their availability for issue.
![Book_Detail](https://user-images.githubusercontent.com/51286676/58956246-81555c80-87bb-11e9-88de-91907186daf4.PNG)

##### User can view the list of all Authors available.
![All_Authors](https://user-images.githubusercontent.com/51286676/58956230-78648b00-87bb-11e9-8b2b-d8a219b8721f.PNG)

##### User can view all the books by the author available in the library.
![Author_Detail](https://user-images.githubusercontent.com/51286676/58956286-946\

##### This is the login page for users to see their borrowed book with due date.
![Login](https://user-images.githubusercontent.com/51286676/58956270-8ca88800-87bb-11e9-86c2-de3dbad154b8.PNG)
82c80-87bb-11e9-885d-ca15a8c3f347.PNG)

##### A user can check his borrowed books. Admin user or Staff members can view borrowers of all books.
![All_Borrowed_root](https://user-images.githubusercontent.com/51286676/58956316-a2b64880-87bb-11e9-88ea-007f92b47c86.PNG)

#### Features to be added soon in this App to make it more powerful for schools and colleges:
- Search bar to search for a book or author on the Home Page.
- To Show the Borrow History of a book.
- Users can add their review and rating for a book.
