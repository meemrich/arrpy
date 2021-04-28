from src.arrpy.listprocessor import avg_col

class TestAverage:
    def test_equal_dims(self):
        assert avg_col([[], [], []], True, True) == []
        assert avg_col([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]], True, True) == [5.5, 6.5, 7.5]
    
    def test_correct_output(self):
        assert avg_col([[], [], []]) == []
        assert avg_col([[1, 2, 3], [4,5,6], [7,8, 9], [10, 11, 12]]) == [5.5, 6.5, 7.5]