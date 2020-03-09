import numpy as np
import pandas as pd
### Creating a Series, letting pandas create a default index
s = pd.Series([1, 3, 5, 6, 8])
### Creating a DataFrame
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
### Creating DataFrame by passing dict
df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
df2.sort_values(by='B')
print(df2)
