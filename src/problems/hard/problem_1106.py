class Solution:
    def parse_or(self, or_expression: str) -> str:
        return 't' if 't' in or_expression else 'f'
    
    def parse_and(self, and_expression: str) -> str:
        return 'f' if 'f' in and_expression else 't'
    
    def parse_not(self, not_expression: str) -> str:
        return 'f' if 't' in not_expression else 't'
    
    def parse(self, expression: str) -> str:
        print(expression)
        if len(expression) == 1: return expression
        inner_opening_bracket = expression.rfind('(')
        inner_closing_bracket = expression.find(')', inner_opening_bracket)
        print(inner_opening_bracket, inner_closing_bracket)
        
        inner_expression = expression[inner_opening_bracket - 1: inner_closing_bracket + 1]
        print(inner_expression)
        if inner_expression[0] == '|':
            return self.parse(expression.replace(inner_expression, self.parse_or(inner_expression)))
        elif inner_expression[0] == '&':
            return self.parse(expression.replace(inner_expression, self.parse_and(inner_expression)))
        else:
            return self.parse(expression.replace(inner_expression, self.parse_not(inner_expression)))
        
    def parseBoolExpr(self, expression: str) -> bool:
        return self.parse(expression) == 't'
