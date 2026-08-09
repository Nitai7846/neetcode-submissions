class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        def to_number(s):
            try:
                return int(s)      # or float(s) if decimals matter
            except ValueError:
                return None        # "C" -> None


        for string in operations:

            val = to_number(string)
            if val is not None:
                record.append(val)

            
            elif string == "+":
                val1 = record[-1]
                val2 = record[-2]
                val = val1+val2
                record.append(val)
            
            elif string == "C":
                record.pop()
            
            elif string == "D":
                val1 = record[-1]
                val = 2*val1 
                record.append(val)
        
        return sum(record)








        