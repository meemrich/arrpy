from src.arrpy.listprocessor import open_df, write_csv

class TestWriteRead:
    def test_open(self):
        assert open_df("tests/test.csv") == open_df("tests/test.txt", delim_type = "tab")
        assert open_df("tests/test.csv") == [['1', '2'], ['cat', 'dog'], ['12', '13']]
        assert open_df("tests/test.csv", delim_type = "csv", subarray= "row") == [['1', 'cat', '12'], ['2', 'dog', '13']]
    
    def test_open_write(self):
        arr = open_df("tests/test.csv")
        write_csv(arr, "tests/test_out.csv")
        assert open_df("tests/test.csv") == open_df("tests/test_out.csv")
