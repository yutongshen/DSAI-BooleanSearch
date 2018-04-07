class SearchEngine:
    def __init__(self, source_file):
        self.data = open(source_file).readlines()
        self.data_size = len(self.data)
        self.queries_result = None
        self.queries_distribute = {}
        self.cache = {}
    
    def query(self, query_file):
        queries = open(query_file).readlines()
        queries_list = []

        for q in queries:
            args = q.split()
            query_operand = args[::2]
            queries_list.append((args[1], query_operand))
            for arg in query_operand:
                cnt = self.queries_distribute.get(arg, 0) + 1
                self.queries_distribute[arg] = cnt
                if cnt == 2:
                    self.cache[arg] = []
        
        self._build_cache()
        
        op_switch = {
            'and': lambda operand: self._and_search(operand),
            'or' : lambda operand: self._or_search(operand),
            'not': lambda operand: self._not_search(operand)
        }
                
        result = []
        for query_operator, query_operand in queries_list:
            try: 
                search = op_switch[query_operator]
                match = search(query_operand)
                if match:
                    result.append(','.join(map(str, match)))
                else:
                    result.append('0')
            except:
                print('error')
                    
        self.queries_result = result

    def save_result(self, output_file):
        with open(output_file, 'w') as f:
            f.write('\n'.join(self.queries_result))

    def _build_cache(self):
        for i, sentence in enumerate(self.data):
            for op in self.cache.keys():
                if op in sentence:
                    self.cache[op].append(i + 1)

    def _list_intersection(self, list1, list2):
        res = []
        i = j = 0
        i_max = len(list1)
        j_max = len(list2)

        while i != i_max and j != j_max:
            if list1[i] < list2[j]:
                i += 1
            elif list1[i] == list2[j]:
                res.append(list1[i])
                i += 1
                j += 1
            else:
                j += 1

        return res
        
    def _list_merge(self, list1, list2):
        res = []
        i = j = 0
        i_max = len(list1)
        j_max = len(list2)

        while i != i_max and j != j_max:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            elif list1[i] == list2[j]:
                res.append(list1[i])
                i += 1
                j += 1
            else:
                res.append(list2[j])
                j += 1
       
        return res + list1[i:] + list2[j:]

    def _list_difference(self, list1, list2):
        res = []
        i = j = 0
        i_max = len(list1)
        j_max = len(list2)

        while i != i_max and j != j_max:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            elif list1[i] == list2[j]:
                i += 1
                j += 1
            else:
                j += 1

        return res + list1[i:]

    def _and_search_force(self, ops):
        result = range(1, self.data_size + 1)
        for op in ops:
            result = [i for i in result if op in self.data[i - 1]]
        return result

    def _or_search_force(self, ops):
        result = []
        
        for i, sentence in enumerate(self.data):
            find = False
            for op in ops:
                if op in sentence:
                    find = True
                    break
            if find:
                result.append(i + 1)

        return result


    def _not_search_force(self, ops):
        result = []
        
        for i, sentence in enumerate(self.data):
            find = True
            if not ops[0] in sentence:
                continue
            for op in ops[1:]:
                if op in sentence:
                    find = False
                    break
            if find:
                result.append(i + 1)

        return result
    
    def _and_search(self, ops):
        cache = []
        ops_not_in_cache = []
        for op in ops:
            try: 
                cache.append(self.cache[op])
            except: 
                ops_not_in_cache.append(op)
        
        try: 
            result = cache[0]
        except: 
            return self._and_search_force(ops)

        for res in cache[1:]:
            result = self._list_intersection(result, res)

        for op in ops_not_in_cache:
            result = [i for i in result if op in self.data[i - 1]]

        return result

    def _or_search(self, ops):
        cache = []
        ops_not_in_cache = []
        for op in ops:
            try: 
                cache.append(self.cache[op])
            except: 
                ops_not_in_cache.append(op)

        if len(ops_not_in_cache) != 0:
            result = self._or_search_force(ops_not_in_cache)
        else:
            result = []

        for res in cache:
            result = self._list_merge(result, res)

        return result

    def _not_search(self, ops):
        cache = []
        ops_not_in_cache = []
        first_hit = True

        try: 
            result = self.cache[ops[0]]
        except: 
            first_hit = False

        for op in ops[1:]:
            try: 
                cache.append(self.cache[op])
            except: 
                ops_not_in_cache.append(op)
        
        if not first_hit:
            result = [i for i in range(1, self.data_size) if ops[0] in self.data[i - 1]]

        for res in cache:
            result = self._list_difference(result, res)

        for op in ops_not_in_cache:
            result = [i for i in result if not op in self.data[i - 1]]
        
        return result
