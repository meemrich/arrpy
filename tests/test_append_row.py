from src.arrpy.listprocessor import append_row

class TestAppendRow:
    def test_invalid_row(self):
        assert append_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], -1) is None
        assert append_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], [1, 2, 3]) is None
    
    def test_correct_output(self):
        assert append_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]],
                                       [13, 14, 15, 16]) == [[1, 2, 3, 13],
                                                             [4, 5, 6, 14],
                                                             [7, 8, 9, 15],
                                                             [10, 11, 12, 16]]
        assert append_row([[], [], []], [1, 2, 3]) == [[1], [2], [3]]