---
# optional when the title is not the file name
title: Python Pandas Refresher
tags: python, pandas
---

When you do not use `pandas` often, searching for documentation is a time consuming step.

### Core concepts
- DataFrame (usually instantiated as `df`) is a table with row and column names/indices 
  - row index default to `0:n`, may be specified otherwise.
- avoid chained(indexing then) assignment! e.g. `df["col2"][df["col1"] > 4] = 0` will [fail][pd ref chained indexing]!

### Import export
- import from 
  - files
    - table, csv: `pd.read_csv` ...
    - json:  `pd.read_json`
      - take note of the orientations: 'split', 'records', 'index', 'columns', 'values', see [doc][pd ref read_json]
  - memory:
    - `pd.DataFrame.from_dict` or `from_records`
- export
  - `df.to` and check auto-complete

### Using
- quick view: 
  - `df.head(n=5)`
  - `df.columns` for the column names
  - `df.index` for row indices
  - `df.info` `df.describe` for statistic (mean, std, etc)
- access:
  - `df.col_label` or `df['col_label']` to get one column
  - `loc` for label, `iloc` for integer index (like usual matrix)!
  - ignore `.at`, it is for single value access
    ```py
    df[["col1", "col2"]]                        # select multiple columns
    df["col1"], df.col1                         # select the specific columns
    df.loc[["row1", "row2"], ["col1", "col2"]]  # select specific rows and columns
    df.loc["row4":"row7", "col3":"col5"]        # select row and column ranges
    df.iloc[[1, 2, 5, 8], 5:8]                  # select by indices01il
  ```
- others
  - `df.sort_index` or `df.sort_values`


## Plotting
- `matplotlib` matlab like, not the easiest, low level
- `seaborn` wrapper of `matplotlib`, still requires `matplotlib` for tweaks e.g. axis etc
- `ggplot`: from R, quite some learning curve
- `bokeh` mcm nice and clean, interactive, but must be on notebook (more or less)
- `pygal` svg, no panda integration, interactive-ish graph
- `plotly`: interactive, high lvl



## Sources


[pd ref read_json]: https://pandas.pydata.org/pandas-docs/stable/search.html?q=read_json
[pd ref chained indexing]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#why-does-assignment-fail-when-using-chained-indexing
