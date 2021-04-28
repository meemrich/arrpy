from src.arrpy.listprocessor import avg_col, extract_row, append_row, del_row

class TestCheck:
    def test_type(self):
        assert avg_col((1, 2)) is None
        assert extract_row((1, 2), 0) is None
        assert append_row((1, 2), [1, 2]) is None
        assert del_row((1, 2), 0) is None
    
    def test_size(self):
        assert avg_col([[1]]) is None
        assert extract_row([[1]], 0) is None
        assert append_row([[1]], [1]) is None
        assert del_row([[1]], 0) is None
    
    def test_dimcount(self):
        assert avg_col([]) is None
        assert avg_col([1, 2, 3]) is None
        assert avg_col([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]) is None
        assert extract_row([], 0) is None
        assert extract_row([1, 2, 3], 0) is None
        assert extract_row([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]]], 0) is None
        assert append_row([], []) is None
        assert append_row([1, 2, 3], [1, 2, 3]) is None
        assert append_row([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]]], [1, 2, 3]) is None
        assert del_row([], 0) is None
        assert del_row([1, 2, 3], 0) is None
        assert del_row([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                  [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                 [[1, 2, 3], [1, 2, 3], [1, 2, 3]]], 0) is None
        
        
    def test_ragged(self):
        assert avg_col([[1, 2, 3], [4,5,6], [7,8, 9], [7,9]]) is None
        assert avg_col([[1, 2, 3], [4,5,6], [7,8, 9], [7,8, 9, 10]]) is None
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [7,9]], 0) is None
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [7,8, 9, 10]], 0) is None
        assert append_row([[1, 2, 3], [4,5,6], [7,8, 9], [7,9]],
                                        [1, 2, 3, 4]) is None
        assert append_row([[1, 2, 3], [4,5,6], [7,8, 9], [7,8, 9, 10]],
                                        [1, 2, 3, 4]) is None
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9], [7,9]], 0) is None
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9], [7,8, 9, 10]], 0) is None
    
    def test_equal_dims(self):
        assert avg_col([[1, 2, 3], [2, [3]]], True, True) is None
        assert extract_row([[1, 2, 3], [2, [3]]], 0, True) is None
        assert append_row([[1, 2, 3], [2, [3]]], [1, 2], True, True) is None
        assert del_row([[1, 2, 3], [2, [3]]], 0, True) is None