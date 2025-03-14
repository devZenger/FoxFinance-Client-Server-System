import decimal

def make_tabelle(input:dict):

    for dic_in in input.values():
        for k,v in dic_in.items():
            
            if isinstance(v, decimal.Decimal):
                dic_in[k]=str(v.quantize(decimal.Decimal(1.00)))
                
            elif isinstance(v, int):
                dic_in[k]= str(v)
            elif isinstance(v, float):
                dic_in[k]=str(round(v,2))
            

    column_lengths = []
    
    for dic_in in input.values():
        
        for i, (k,v) in enumerate(dic_in.items()):
            column_lengths.append(0)
            key =len(k); vol = len(v)
            
            if key > column_lengths[i]:
                column_lengths[i]=key
            
            if vol > column_lengths[i]:
                column_lengths[i]= vol
    
    
    tabelle = []
    for i, dic_in in enumerate(input.values()):
        tabelle.append("")
        for j, (k,v) in enumerate(dic_in.items()):
            if i == 0:
                tabelle[0]= f"{tabelle[0]} {k.ljust(column_lengths[j])} |"
                tabelle.append("")
                tabelle[1]=f"{tabelle[1]}{"-"*(column_lengths[j]+3)}"
                tabelle.append("")
            
            tabelle[i+2] = f"{tabelle[i+2]} {v.ljust(column_lengths[j])} |" 
    
    return tabelle
            







if __name__ == "__main__":
    result = {'row_result0': {'isin': 'DE0005140008',
                            'company_name': 'Deutsche Bank',
                            'amount': 68,
                            'price_per_stock': 21.270000457763672,
                            'actual_price': 21.270000457763672,
                            'performance': 1.0},
              'row_result1': {'isin': 'DE0005190003',
                              'company_name': 'BMW St',
                              'amount': 79,
                              'price_per_stock': 86.44000244140625,
                              'actual_price': 86.44000244140625,
                              'performance': 1.0},
              'row_result2': {'isin': 'DE000DTR0CK8',
                              'company_name': 'Daimler Truck',
                              'amount': 34,
                              'price_per_stock': 41.91999816894531,
                              'actual_price': 41.91999816894531,
                              'performance': 1.0},
              'row_result3': {'isin': 'DE000ZAL1111',
                              'company_name': 'Zalando',
                              'amount': 54,
                              'price_per_stock': 31.229999542236328,
                              'actual_price': 31.229999542236328,
                              'performance': 1.0}}            
    
    tabelle = make_tabelle(result)
    
    for tab in tabelle:
        print(tab)               
                
                
            
        
        
        