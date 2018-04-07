# Data Science and Artificial Intelligence Practice Homework
DSAI HW2-BooleanSearch

## Prerequisite
- Python 3.6.4

## Usage
```sh
$ python main.py [-h] [--source SOURCE] [--query QUERY] [--output OUTPUT]
```
| Optional Arguments| Description|
| --- | --- |
| -h, --help: | show this help message and exit |
| --source SOURCE: | input source data file name (default: `source.csv`) |
| --query QUERY: | query file name (defalut: `query.txt`) |
| --output OUTPUT: | output file name (default: `output.txt`) |

## Implement
### Constructor
- Load `source.csv` by pandas

### Query
- Load `query.txt`
- Counting each arguments of each query by `self.queries_distribute`
  > For example:
  > ```txt
  > 美國 and 台灣
  > 台灣 or 川普
  > 川普 not 外星人
  > ```
  > then we have `self.queries_distribute = {'美國': 1, '台灣': 2, '川普': 2, '外星人': 1}`

- Classify the type of logical operation (ex: `and`, `or`, `not`)
- According to the type of logical operation, we send each query to difference function (ex: `_and_search`, `_or_search`, `_not_search`)

### Logical Operation
- We can express the query by `'arg1' and 'arg2' and 'arg3'`
- If there is one of `arg1` to `arg3` in `self.cache`, then mean cache hit
  > There are list total of related title in cache, so we can avoid search again
- If there is no argument in `self.cache`, then mean cache miss
  > We'll choice an argument that `self.queries_distribute[arg]` is the largest <br>
  > then we'll record total of related title in `self.cache[arg]`

### Save Result
- Store result in `output.txt`

### Flowchart
<!-- ![flowchart](https://g.gravizo.com/svg?@startuml;%28*%29%20--%3E%20%22Load%20source.csv%22%20as%20B;B%20--%3E%20%22Load%20query.txt%22%20as%20C;C%20--%3E%20%22Query%22%20as%20E;E%20-%3E%20%22Search%20the%20whole%20of%20dataset%22%20as%20G;G%20--%3E%20%22According%20to%20query,%20matching\n%20which%20title%20is%20fit%20the%20bill%22%20as%20H;H%20--%3E%20if%20%22Finish%20?%22%20then;%20%20--%3E%20[True]%20%22Store%20output.txt%22%20as%20I;else;%20%20-----%3E%20[False]%20E;endif;I%20--%3E%20%28*%29;@enduml) -->
![flowchart](https://g.gravizo.com/svg?@startuml;%28*%29%20--%3E%20%22Load%20source.csv%22%20as%20B;B%20--%3E%20%22Load%20query.txt%22%20as%20C;C%20--%3E%20%22Build%20cache%22%20as%20D;D%20--%3E%20%22Query%22%20as%20E;E%20--%3E%20if%20%22Cache%20hit%20?%22%20%20then;%20%20--%3E[True]%20%22Load%20cache,%20and\n%20only%20search%20the\n%20list%20in%20cache%22%20as%20F;else;%20%20--%3E[False]%20%22Search%20all%20dataset%22%20as%20G;endif;F%20--%3E%20%22According%20to%20query,%20matching\n%20which%20title%20is%20fit%20the%20bill%22%20as%20H;G%20--%3E%20H;H%20--%3E%20if%20%22Finish%20?%22%20then;%20%20--%3E%20[True]%20%22Store%20output.txt%22%20as%20I;else;%20%20-----%3E%20[False]%20E;endif;I%20--%3E%20%28*%29;@enduml)

## Related Link
- [nbviewer](https://nbviewer.jupyter.org/github/yutongshen/DSAI-HW2-BooleanSearch/blob/master/main.ipynb)

## Authors
[Yu-Tong Shen](https://github.com/yutongshen/)
