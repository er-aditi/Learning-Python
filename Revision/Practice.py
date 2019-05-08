book = {
    'aditi': ['C', 'Python'],
    'tanya': ['Ruby'],
    'ritik': ['java']
}


for name, books in book.items():
    print("\n", name, "Likes these books:  ")

    for b1 in books:
        print("\t", b1)