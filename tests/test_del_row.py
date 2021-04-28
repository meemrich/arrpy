from src.arrpy.listprocessor import del_row

class TestDelRow:
    def test_invalid_row(self):
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], -1) is None
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], 3) is None
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], "foo") is None
        assert del_row([[], [], []], 0) is None
    
    def test_correct_output(self):
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9],
                       [10, 11, 12]], 0) == [[2, 3],
                                             [5, 6], [8, 9], [11, 12]]
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9],
                       [10, 11, 12]], 2) == [[1, 2],
                                             [4, 5], [7, 8], [10, 11]]
        assert del_row([[1, 2, 3], [4,5,6], [7,8, 9],
                       [10, 11, 12]], "2") == [[1, 2],
                                               [4, 5], [7, 8], [10, 11]]