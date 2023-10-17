with open("books.txt") as books:
    for passages in books:
        books = passages.strip()
        print(books)
