diskette_capacity_mb = 1.44
page_size_bytes = 50 * 25 * 4  
num_pages = 100

book_size_bytes = page_size_bytes * num_pages

num_books_on_diskette = diskette_capacity_mb * 1024 * 1024 // book_size_bytes

print("Количество книг, которое поместится на дискету:", num_books_on_diskette)
