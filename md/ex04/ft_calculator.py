class calculator:
    """ e a calculator class that is able to do calculations (dot product, addition, subtraction) of 2 vectors."""
        
    # decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            raise("the size of the vectors don't has identical")
        i = 0
        pro  = 0
        while(i < len(V1)):
            pro += V1[i]*V2[i]
            i += 1
        print(f"Dot product is: {pro}")

    # decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            raise("the Vectors don't has the same size")
        for i, el in enumerate(V1):
            V1[i] += V2[i]
        print(f"Add Vector is : {V1}")
    # decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            raise("the Vectors don't has the same size")
        for i, el in enumerate(V2):
            V1[i] -= V2[i]
        print(f"Sous Vector is: {V1}")