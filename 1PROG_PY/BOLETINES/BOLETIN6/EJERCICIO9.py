def vectores():

    vector_a = [1, 2, 3]

    vector_b = [-1, 0, 2]

    productoEscalar = 0


    for a_i, b_i in zip ( vector_a, vector_b):
        productoEscalar += a_i * b_i


    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"O produto escalar de A e B é: {productoEscalar}")

if __name__ == "__main__":
    vectores()