import json

class MyLibrary:
    def __init__(self):
        self.books = []
        self.data_file = "my_books.json"
        self.load_books()

    def load_books(self):
        try:
            with open(self.data_file, "r") as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.data_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        title = input("Book Title: ")
        author = input("Author: ")
        year = input("Publication Year: ")
        genre = input("Genre: ")
        has_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": has_read,
        }

        self.books.append(book)
        self.save_books()
        print("\nYour new book has been added!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print("\nBook removed successfully!\n")
                return
        print("\nOops! That book wasn't found in your library.\n")

    def search_books(self):
        search_choice = input("Search by:\n1. Title\n2. Author\nEnter your choice (1 or 2): ").strip()
        keyword = input("Enter your search keyword: ").strip().lower()

        if search_choice == "1":
            matching_books = [book for book in self.books if keyword in book["title"].lower()]
        elif search_choice == "2":
            matching_books = [book for book in self.books if keyword in book["author"].lower()]
        else:
            print("\nInvalid choice! Please enter 1 or 2.\n")
            return

        if matching_books:
            print("\nHere are your matching books:")
            for i, book in enumerate(matching_books, 1):
                status = "Read" if book["read"] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} [{status}]")
            print()
        else:
            print("\nNo matching books found.\n")

    def edit_book(self):
        title = input("Enter the title of the book you wish to update: ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                print("Press Enter to keep the current value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New publication year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
                self.save_books()
                print("\nBook details updated successfully!\n")
                return
        print("\nBook not found in your collection.\n")

    def display_books(self):
        if not self.books:
            print("\nYour library is currently empty.\n")
            return

        print("\nYour Personal Library:")
        for i, book in enumerate(self.books, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} [{status}]")
        print()

    def reading_statistics(self):
        total = len(self.books)
        read_count = sum(1 for book in self.books if book["read"])
        progress = (read_count / total * 100) if total else 0
        print(f"\nTotal books: {total}")
        print(f"Books read: {read_count}")
        print(f"Completion: {progress:.2f}%\n")

    def run(self):
        while True:
            print("=== Welcome to My Personal Library! ===")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Edit book details")
            print("5. View all books")
            print("6. View reading statistics")
            print("7. Exit")
            choice = input("Choose an option (1-7): ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.edit_book()
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                self.reading_statistics()
            elif choice == "7":
                print("\nGoodbye! Happy reading!\n")
                break
            else:
                print("\nInvalid choice! Please select a valid option.\n")

if __name__ == "__main__":
    library = MyLibrary()
    library.run()
