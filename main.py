# coding: utf-8

# # HW2-BooleanSearch

# ## Import package
# - pandas

# In[1]:


from src.search import SearchEngine


# ## Implement
# ### Constructor
# - Load `source.csv` by pandas
# 
# ### Query
# - Load `query.txt`
# - Counting each arguments of each query by `self.queries_distribute`
#   > For example:
#   > ```txt
#   > 美國 and 台灣
#   > 台灣 or 川普
#   > 川普 not 外星人
#   > ```
#   > then we have `self.queries_distribute = {'美國': 1, '台灣': 2, '川普': 2, '外星人': 1}`
# 
# - Classify the type of logical operation (ex: `and`, `or`, `not`)
# - According to the type of logical operation, we send each query to difference function (ex: `_and_search`, `_or_search`, `_not_search`)
# 
# ### Logical Operation
# - We can express the query by `'arg1' and 'arg2' and 'arg3'`
# - If there is one of `arg1` to `arg3` in `self.cache`, then mean cache hit
#   > There are list total of related title in cache, so we can avoid search again
# - If there is no argument in `self.cache`, then mean cache miss
#   > We'll choice an argument that `self.queries_distribute[arg]` is the largest <br>
#   > then we'll record total of related title in `self.cache[arg]`
# 
# ### Save Result
# - Store result in `output.txt`
# 
# ### Flowchart
# ![flowchart](https://github.com/yutongshen/DSAI-HW2-BooleanSearch/blob/master/img/flowchart.png?raw=true)

# In[2]:


# ## Main module

# In[3]:


if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    parser.add_argument('-f',
                        default='',
                        help='ipython')
    args = parser.parse_args()

    # Please implement your algorithm below

    # TODO load source data, build search engine
    se = SearchEngine(args.source)

    # TODO compute query result
    se.query(args.query)

    # TODO output result
    se.save_result(args.output)

