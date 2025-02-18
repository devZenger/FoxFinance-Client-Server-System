import re




class Password:
    def check_pwd_form(self, pw_to_check):
        test_result = []
        
        def _check_match(pattern):
            nonlocal test_result
            matches = re.findall(pattern, pw_to_check)
            if len(matches) >= 2:
                test_result.append(True)
            else:
                test_result.append(False)
           
        
        if len(pw_to_check) >= 12:
            pattern_ABC =  r"[A-Z]"
            _check_match(pattern_ABC) # re.findall(pattern_ABC, pw_to_check)
    
            pattern_abc = r"[a-z]"
            _check_match(pattern_abc)
            
            pattern_special = r"[!#$&'*+,-.:?@^_|~]"
            _check_match(pattern_special)
        else:
            test_result.append(False)
        
        test_result.sort()
        test_result.reverse()
        
        pw_okay = False
        for result in test_result:
            if result == True:
                pw_okay = True
            else: 
                pw_okay= False
        
        return pw_okay