from src.arrpy.listprocessor import extract_row

class TestExtractRow:
    def test_invalid_row(self):
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], -1) is None
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], 3) is None
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], "foo") is None
        assert extract_row([[], [], []], 0) is None
    
    def test_correct_output(self):
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], 0) == [1, 4, 7, 10]
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], 2) == [3, 6, 9, 12]
        assert extract_row([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], "2") == [3, 6, 9, 12]