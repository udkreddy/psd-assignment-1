import pytest
from sparse_recommender import SparseMatrix

def test_set_get():
    matrix = SparseMatrix(3, 3)

    # Test setting and getting values
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    matrix.set(2, 2, 3)

    assert matrix.get(0, 0) == 1
    assert matrix.get(1, 1) == 2
    assert matrix.get(2, 2) == 3
    assert matrix.get(1, 0) == 0  # Non-set element should be 0

def test_recommend():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    matrix.set(2, 2, 3)
    vector = [1, 0, 0]

    # Test the recommend method
    result = matrix.recommend(vector)
    assert result == [1, 0, 0]

    vector2 = [0, 1, 0]

    # Test recommend with a different vector
    result2 = matrix.recommend(vector2)
    assert result2 == [0, 2, 0]

def test_add_movie():
    matrix1 = SparseMatrix(3, 3)
    matrix1.set(0, 0, 1)
    matrix1.set(1, 1, 2)
    matrix1.set(2, 2, 3)

    matrix2 = SparseMatrix(3, 3)
    matrix2.set(0, 0, 2)
    matrix2.set(1, 1, 4)
    matrix2.set(2, 2, 6)

    # Test adding two matrices
    result = matrix1.add_movie(matrix2)
    assert result.get(0, 0) == 3
    assert result.get(1, 1) == 6
    assert result.get(2, 2) == 9
    assert result.get(1, 0) == 0  # Non-set element should be 0

def test_dense():
    matrix = SparseMatrix(2, 2)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)

    # Test converting to a dense matrix
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[1, 0], [0, 2]]

def test_invalid():
    matrix = SparseMatrix(3, 3)

    # Test setting and getting with invalid indices
    with pytest.raises(ValueError):
        matrix.set(4, 0, 1)
    
    with pytest.raises(ValueError):
        matrix.get(0, 4)
    
    # Test recommending with a vector of incorrect size
    with pytest.raises(ValueError):
        matrix.recommend([1, 0, 0, 1])

if __name__ == "__main__":
    pytest.main()
