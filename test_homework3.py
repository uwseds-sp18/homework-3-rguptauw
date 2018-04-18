import unittest
import homework3

#Define a class in which the tests will run
class TestCreateDF(unittest.TestCase):

    def test_columns(self):
        df_lst = list(homework3.create_dataframe('class.db'))
        lst_col = ['video_id', 'category_id', 'language']
        res = sorted(df_lst) == sorted(lst_col)
        self.assertTrue(res)
        
    def test_num_rows(self):
        numr = homework3.create_dataframe('class.db').shape[0]
        self.assertEqual(numr, 35950)
        
    def test_check_keys(self):
        df = homework3.create_dataframe('class.db')
        res = (df.shape[0] == df.groupby(['video_id', 'language','category_id']).ngroups)
        self.assertTrue(res)
    
    def test_path_valid(self):
        self.assertRaises(ValueError, homework3.create_dataframe, 'class_bad_path.db')

suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDF)
_ = unittest.TextTestRunner().run(suite)
