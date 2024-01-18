def find_product(products: list, keyproduct):
    for i in range(len(products)):
        if keyproduct == products[i]:
            return i
    return None

print(find_product(["apple", "banana", "pineapple"],"apple"))