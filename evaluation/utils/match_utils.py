import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from sympy.parsing.latex import parse_latex
import sympy as sp
import re
from math import sqrt

def text_to_num(text):
    basic_nums = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "first":1,"second":2,"third":3,"fourth":4,"one hundred":100
    }
    return str(basic_nums.get(text))

def replace_one_with_num(expr):
    '''replace one two three ... in the expr with 1 2 3 ...'''
    def replace_match(match):
        return text_to_num(match.group(0))
    pattern = r'\b(one hundred|zero|one|two|three|four|five|six|seven|eight|nine|ten|first|second|third|fourth' \
              r'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|' \
              r'twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\b'
    return re.sub(pattern, replace_match, expr)

def convert_mixed_fractions(expr):
    '''convert mixed fraction to false fraction, e.g.'a b/c' -> '(a*c+b)/c' 
    '''
    pattern = r'(\d+)\s+(\d+)/(\d+)'
    def to_improper_fraction(match):
        whole_number = int(match.group(1))
        numerator = int(match.group(2))
        denominator = int(match.group(3))
        new_numerator = whole_number * denominator + numerator
        return f'{new_numerator}/{denominator}'
    return re.sub(pattern, to_improper_fraction, expr)


def replace_pi_with_number(expr):
    '''convert pi with 3.14. e.g.10π -> 10*3.14'''
    def replace_with_number_pi(match):
        preceding_char = expr[match.start() - 1] if match.start() > 0 else ''
        if preceding_char.isdigit():
            return '*' + '3.14'
        else:
            return '3.14'

    expr = re.sub(r'(π|\\pi|\\\\pi|pi)', replace_with_number_pi, expr)
    return expr


def simplify(expr):
    expr = convert_mixed_fractions(expr)
    expr = expr.replace('$', '').replace(' ', '').replace('\t', '')
    expr = expr.replace('−', '-').replace('﹣', '-') 
    # replace pi with number
    expr = re.sub(r'(\d+(\.\d+)?)%', lambda match: str(float(match.group(1)) / 100), expr)
    expr = replace_pi_with_number(expr)
    try:
        expr = parse_latex(expr)
        expr = sp.simplify(expr)
    except:
        print(f'cannot be converted to expr: {expr}')
    return expr


def filter_digit(answer):
    # case:  "123、-45、3.14159、+6.02、1/2、5 3/4 2*pi 2π"
    regex_expr = r"[-+]?((\d+(\.\d+)?\/\d+(\.\d+)?|\d+\s+\d+\/\d+|\d+(\.\d+)?)((\*)?(π|\\pi|\\\\pi|pi))?%?|\$[^(\$|x|y|z)]*\$)"
    match = [i.group() for i in re.finditer(regex_expr, answer)]
    ret = []
    for item in match:
        if '=' in item: 
            item = item.split('=')[-1]
        ret.append(item)
    return ret

def exam_correction_with_re(gt_answer_str, pred_answer_str,concept_name):
    def is_close(a, b,concept_name):
        """Determine if two values are close enough, where delta is the maximum allowed difference"""
        try:
            delta = abs(a / 20) if a < 20 else 1
            delta = abs(a / 5) if concept_name == "Estimation and rounding" else delta
            ret = abs(a - b) <= delta
            ret = bool(ret)
        except Exception as e:
            print(e)
            ret = False
        return ret

    # Standardize answers, like [ans1,ans2,...,]
    gt_answer_str = gt_answer_str.replace('[', '').replace(']', '').replace('，', ',').replace('_', '')
    gt_answer_list = gt_answer_str.split(',')


    # replace one two three ... in the expr with 1 2 3 ...
    pred_answer_str = replace_one_with_num(pred_answer_str)
    # Remove English comma between numbers.
    pred_answer_str = re.sub(r'(?<=\d),(?=\d)', '', pred_answer_str)
    # filter digit
    pred_answer_list = filter_digit(pred_answer_str)

    # compare between gt_answer_list and pred_answer_list
    if len(pred_answer_list) == 0: return False
    pred_answer_list = [simplify(i) for i in pred_answer_list]
    gt_answer_list = [simplify(i) for i in gt_answer_list]
    for gt_answer in gt_answer_list:
        if not any(is_close(gt_answer, pred_answer,concept_name) for pred_answer in pred_answer_list):
            return False
    return True

def main_exam_number_correct(answer_str:str, response_str:str,concept_name:str=None):
    # When a keyword similar to "answer" appears, only the text segment after the keyword is taken to narrow down the extraction range.
    prompt_ans_prefix = ["答案是", '答案：', "answer (arabic numbers) is", "(arabic numerals) is", "answer is:",
                         "answer is :", "answer is", "Therefore, the answer (arab", "Answer: ", "结果是", "结果为",
                         "答案为", "答案是", "得出答案", "所以", "因此"] 
    for prefix in prompt_ans_prefix:
        ans_str_list = response_str.split(prefix)
        if len(ans_str_list) == 2:
            response_str = ans_str_list[-1]
            break
        elif len(ans_str_list) < 2:continue
        else: response_str = ans_str_list[-1]
    response_str = response_str.strip()

    # exam correction
    iscorrect = exam_correction_with_re(answer_str, response_str,concept_name)
    return iscorrect


if __name__ == "__main__":
    # main exam
    iscorrect = main_exam_number_correct(answer_str='6.47', response_str='答案是三角形面积为2π，平方米')
    print("iscorrect: ",iscorrect)

    iscorrect = main_exam_number_correct(answer_str='3.14', response_str='答案是三角形面积为3.14，平方米')
    print("iscorrect: ",iscorrect)
    
    generation = """First, we must calculate the total amount of the computer and accessories.
The total amount of the computer and accessories is €1090 + €157 + €74 + €102 = €1323.
Now, we must calculate the total amount of the budget.
The total amount of the budget is €1500.
Finally, we must calculate the amount of money that Elvira will have left for her clothing.
The amount of money that Elvira will have for her clothing is €1500 - €1323 = €177.
Therefore, Elvira will have €177 left for her clothing.
Answer: Elvira will have €177 for her clothing.
[Exp]First, let’s look at the total cost of computer equipment: 1090 + 157 + 74 + 102 = <<1090+157+74+102=1423>>1423 euros
Let us now calculate what is left for the garment: 1500 - 1423 = <<1500-1423=77>>77 euros"""
    answer = 77
    iscorrect = main_exam_number_correct(answer_str=str(answer), response_str=generation)
    print("iscorrect: ",iscorrect)