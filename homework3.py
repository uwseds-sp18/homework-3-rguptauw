#importing all modules in the starting
import sqlite3
import pandas as pd
import numpy as np
from pathlib import Path

#part 1
def create_dataframe(path):
    my_file = Path(path)
    if my_file.is_file():
        conn = sqlite3.connect(path)
        df = pd.read_sql_query("""select category_id, video_id, 'ca' as language from CAvideos UNION
        select category_id,video_id, 'de' as language from DEvideos UNION
        select category_id, video_id, 'fr' as language from FRvideos UNION
        select category_id, video_id, 'gb' as language from GBvideos UNION
        select category_id, video_id, 'us' as language from USvideos""", conn)
        return df
    else:
        raise ValueError("Valid file does not exist at the specified path")