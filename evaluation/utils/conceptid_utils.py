def get_cate2id(type='element_zh'):
    cate2id_element_zh = {
    "几何": 0,
    "应用": 1,
    "度量与统计": 2,
    "数与代数": 3,
    "几何/平面图形": 4,
    "几何/立体图形": 5,
    "应用/基础问题": 6,
    "应用/经典问题": 7,
    "应用/行程问题": 8,
    "度量与统计/度量": 9,
    "度量与统计/统计": 10,
    "数与代数/分数运算": 11,
    "数与代数/因数与倍数": 12,
    "数与代数/基础运算": 13,
    "数与代数/比与比例": 14,
    "几何/平面图形/三角形": 15,
    "几何/平面图形/圆": 16,
    "几何/平面图形/平行四边形": 17,
    "几何/平面图形/梯形": 18,
    "几何/平面图形/正方形": 19,
    "几何/平面图形/综合问题": 20,
    "几何/平面图形/角": 21,
    "几何/平面图形/长方形": 22,
    "几何/立体图形/圆柱": 23,
    "几何/立体图形/正方体": 24,
    "几何/立体图形/综合问题": 25,
    "几何/立体图形/长方体": 26,
    "应用/基础问题/和差倍问题": 27,
    "应用/基础问题/基础问题": 28,
    "应用/基础问题/差倍问题": 29,
    "应用/基础问题/归一问题": 30,
    "应用/基础问题/归总问题": 31,
    "应用/经典问题/利息问题": 32,
    "应用/经典问题/周期问题": 33,
    "应用/经典问题/对折问题": 34,
    "应用/经典问题/工程问题": 35,
    "应用/经典问题/年龄问题": 36,
    "应用/经典问题/折扣问题": 37,
    "应用/经典问题/植树问题": 38,
    "应用/经典问题/税率问题": 39,
    "应用/经典问题/还原问题": 40,
    "应用/经典问题/页码问题": 41,
    "应用/经典问题/鸡兔同笼问题": 42,
    "应用/行程问题/相遇问题": 43,
    "应用/行程问题/行程问题": 44,
    "应用/行程问题/追击问题": 45,
    "度量与统计/度量/人民币问题": 46,
    "度量与统计/度量/时间问题": 47,
    "度量与统计/度量/浓度问题": 48,
    "度量与统计/度量/温度问题": 49,
    "度量与统计/度量/面积问题": 50,
    "度量与统计/统计/排列组合": 51,
    "度量与统计/统计/统计指标": 52,
    "度量与统计/统计/规律": 53,
    "数与代数/分数运算/分数与小数": 54,
    "数与代数/分数运算/分数应用": 55,
    "数与代数/分数运算/分数运算": 56,
    "数与代数/分数运算/最简分数": 57,
    "数与代数/因数与倍数/公倍数问题": 58,
    "数与代数/因数与倍数/公约数问题": 59,
    "数与代数/因数与倍数/因数问题": 60,
    "数与代数/因数与倍数/综合问题": 61,
    "数与代数/因数与倍数/质数问题": 62,
    "数与代数/基础运算/乘法问题": 63,
    "数与代数/基础运算/倒数问题": 64,
    "数与代数/基础运算/四则运算": 65,
    "数与代数/基础运算/定义新运算": 66,
    "数与代数/基础运算/方程问题": 67,
    "数与代数/基础运算/除法问题": 68,
    "数与代数/比与比例/倍数问题": 69,
    "数与代数/比与比例/概率问题": 70,
    "数与代数/比与比例/比例问题": 71,
    "数与代数/比与比例/百分率问题": 72
}
    cate2id_middle_zh = {
    "几何": 0,
    "函数": 1,
    "数与式": 2,
    "方程与不等式": 3,
    "统计与概率": 4,
    "几何/三角形": 5,
    "几何/四边形": 6,
    "几何/圆": 7,
    "几何/立体图形": 8,
    "函数/一次函数": 9,
    "函数/二次函数": 10,
    "函数/反比例函数": 11,
    "函数/平面直角坐标系": 12,
    "数与式/代数式": 13,
    "数与式/分式": 14,
    "数与式/因式": 15,
    "数与式/应用": 16,
    "数与式/整式": 17,
    "数与式/无理数": 18,
    "数与式/根式": 19,
    "方程与不等式/一元一次方程": 20,
    "方程与不等式/一元二次方程": 21,
    "方程与不等式/不等式与不等式组": 22,
    "方程与不等式/分式方程": 23,
    "统计与概率/数据分析": 24,
    "统计与概率/概率": 25,
    "几何/三角形/全等三角形": 26,
    "几何/三角形/勾股定理": 27,
    "几何/三角形/等腰三角形": 28,
    "几何/三角形/等边三角形": 29,
    "几何/四边形/平行四边形": 30,
    "几何/四边形/梯形": 31,
    "几何/圆/圆周角": 32,
    "几何/圆/圆心角": 33,
    "几何/圆/垂径定理": 34,
    "几何/圆/弧长和扇形面积": 35,
    "几何/圆/正多边形和圆": 36,
    "几何/圆/点、线、圆的位置关系": 37,
    "几何/立体图形/圆锥": 38,
    "函数/一次函数/一元函数与一元一次方程": 39,
    "函数/一次函数/一次函数与一元一次不等式": 40,
    "函数/一次函数/一次函数与二元一次方程（组）": 41,
    "函数/一次函数/正比例函数": 42,
    "函数/一次函数/求一次函数解析式": 43,
    "函数/二次函数/二次函数的应用": 44,
    "函数/二次函数/抛物线的性质": 45,
    "函数/反比例函数/反比例函数的定义": 46,
    "函数/反比例函数/反比例函数的应用": 47,
    "函数/反比例函数/反比例函数的性质": 48,
    "函数/平面直角坐标系/有序数对": 49,
    "函数/平面直角坐标系/点所在象限": 50,
    "数与式/代数式/代数式求值": 51,
    "数与式/代数式/同类项": 52,
    "数与式/分式/指数幂": 53,
    "数与式/分式/约分与通分": 54,
    "数与式/因式/十字相乘法": 55,
    "数与式/因式/提公因式": 56,
    "数与式/应用/流水问题": 57,
    "数与式/应用/鸽巢问题": 58,
    "数与式/整式/乘法公式": 59,
    "数与式/整式/整式的乘除及混合": 60,
    "数与式/整式/整式的加减": 61,
    "数与式/无理数/判断无理数": 62,
    "数与式/根式/二次根式的运算": 63,
    "数与式/根式/同类二次根式": 64,
    "数与式/根式/平方根与算术平方根": 65,
    "数与式/根式/立方根": 66,
    "方程与不等式/一元一次方程/一元一次方程的应用": 67,
    "方程与不等式/一元一次方程/解一元一次方程": 68,
    "方程与不等式/一元二次方程/一元二次方程的应用": 69,
    "方程与不等式/一元二次方程/解一元二次方程": 70,
    "方程与不等式/不等式与不等式组/一元一次不等式的应用": 71,
    "方程与不等式/不等式与不等式组/一元一次不等式组的应用": 72,
    "方程与不等式/不等式与不等式组/解一元一次不等式": 73,
    "方程与不等式/不等式与不等式组/解一元一次不等式组": 74,
    "方程与不等式/分式方程/分式方程的应用": 75,
    "方程与不等式/分式方程/解分式方程": 76,
    "统计与概率/数据分析/数据的波动趋势": 77,
    "统计与概率/数据分析/数据的集中趋势": 78,
    "统计与概率/概率/概率的应用": 79,
    "统计与概率/概率/求概率": 80,
    "统计与概率/概率/随机事件与概率": 81
}
    cate2id_element_en = {
    "Calculate and Properties": 0,
    "Measurement": 1,
    "geometry": 2,
    "statistics": 3,
    "Measurement/Basic knowledge": 4,
    "Calculate and Properties/Calculate": 5,
    "statistics/Classifying and sorting": 6,
    "geometry/Coordinate plane": 7,
    "statistics/Data": 8,
    "Measurement/Money": 9,
    "Calculate and Properties/Properties": 10,
    "Measurement/Ratio": 11,
    "Measurement/Size": 12,
    "geometry/Three-dimensional shapes": 13,
    "geometry/Two-dimensional shapes": 14,
    "geometry/angles": 15,
    "statistics/probability": 16,
    "Measurement/weight": 17,
    "geometry/angles/Acute, right, obtuse, and straight angles": 18,
    "Measurement/Size/Area": 19,
    "geometry/Two-dimensional shapes/Circles": 20,
    "statistics/Classifying and sorting/Classifying and sorting": 21,
    "Measurement/Money/Coin names and value": 22,
    "geometry/Three-dimensional shapes/Cones": 23,
    "geometry/Coordinate plane/Coordinate plane": 24,
    "geometry/Three-dimensional shapes/Cubes": 25,
    "geometry/Three-dimensional shapes/Cylinders": 26,
    "Calculate and Properties/Calculate/Decimals": 27,
    "Calculate and Properties/Properties/Estimation and rounding": 28,
    "Measurement/Money/Exchanging money": 29,
    "Calculate and Properties/Calculate/Fractions": 30,
    "Measurement/weight/Light and heavy": 31,
    "Calculate and Properties/Calculate/Mixed operations": 32,
    "Calculate and Properties/Calculate/Multiple": 33,
    "Calculate and Properties/Calculate/Numerical expressions": 34,
    "Calculate and Properties/Properties/Patterns": 35,
    "geometry/Two-dimensional shapes/Perimeter": 36,
    "Calculate and Properties/Calculate/Place value": 37,
    "Calculate and Properties/Calculate/Powers": 38,
    "Calculate and Properties/Calculate/Rational number": 39,
    "geometry/Three-dimensional shapes/Spheres": 40,
    "Calculate and Properties/Calculate/Subtraction": 41,
    "Measurement/Basic knowledge/Time": 42,
    "geometry/Two-dimensional shapes/Triangles": 43,
    "Calculate and Properties/Calculate/Variable expressions": 44,
    "geometry/Three-dimensional shapes/Volume": 45,
    "Calculate and Properties/Calculate/add": 46,
    "Calculate and Properties/Properties/compare": 47,
    "Calculate and Properties/Properties/count": 48,
    "Calculate and Properties/Calculate/division": 49,
    "Calculate and Properties/Calculate/equations": 50,
    "Measurement/Size/length": 51,
    "statistics/Data/mode/mean/median/range": 52,
    "Measurement/Ratio/percents": 53,
    "geometry/Two-dimensional shapes/polygons": 54,
    "statistics/probability/probability": 55,
    "Measurement/Ratio/proportional": 56,
    "geometry/Two-dimensional shapes/quadrilaterals": 57,
    "Measurement/Ratio/ratio": 58,
    "Measurement/Basic knowledge/temperature": 59,
    "Measurement/Size/volume": 60
}
    cate2id_middle_en = {
    "Expressions, Equations and Functions": 0,
    "calculate": 1,
    "geometry": 2,
    "statistic and probability": 3,
    "geometry/Congruence and similarity": 4,
    "calculate/Consumer math": 5,
    "geometry/Coordinate plane": 6,
    "statistic and probability/Data": 7,
    "Expressions, Equations and Functions/Expressions": 8,
    "calculate/Financial literacy": 9,
    "Expressions, Equations and Functions/Function concepts": 10,
    "calculate/Integers": 11,
    "calculate/Number theory": 12,
    "statistic and probability/One-variable statistics": 13,
    "calculate/Percents": 14,
    "statistic and probability/Probability": 15,
    "calculate/Rational and irrational numbers": 16,
    "calculate/Ratios and rates": 17,
    "geometry/Scale drawings": 18,
    "calculate/Sequences": 19,
    "geometry/Slope": 20,
    "geometry/Three-dimensional figures": 21,
    "geometry/Transformations": 22,
    "geometry/Two-dimensional figures": 23,
    "statistic and probability/Two-variable statistics": 24,
    "calculate/basic calculate": 25,
    "Expressions, Equations and Functions/equations": 26,
    "Expressions, Equations and Functions/inequalities": 27,
    "calculate/measurement": 28,
    "calculate/basic calculate/Add and subtract": 29,
    "calculate/Sequences/Arithmetic sequences": 30,
    "geometry/Congruence and similarity/Congruence and similarity": 31,
    "calculate/Consumer math/Consumer math": 32,
    "statistic and probability/Probability/Counting principle": 33,
    "calculate/basic calculate/Decimals": 34,
    "geometry/Coordinate plane/Distance between two points": 35,
    "calculate/basic calculate/Divide": 36,
    "Expressions, Equations and Functions/Function concepts/Domain and range of functions": 37,
    "Expressions, Equations and Functions/Expressions/Equivalent expressions": 38,
    "calculate/measurement/Estimate metric measurements": 39,
    "calculate/basic calculate/Exponents and Scientific notation": 40,
    "calculate/Financial literacy/Financial literacy": 41,
    "calculate/basic calculate/Fractions and decimals": 42,
    "calculate/Sequences/Geometric sequences": 43,
    "Expressions, Equations and Functions/Function concepts/Interpret functions": 44,
    "Expressions, Equations and Functions/equations/Linear equations": 45,
    "Expressions, Equations and Functions/Function concepts/Linear functions": 46,
    "geometry/Two-dimensional figures/Lines and angles": 47,
    "statistic and probability/Probability/Make predictions": 48,
    "calculate/basic calculate/Multiply": 49,
    "Expressions, Equations and Functions/Function concepts/Nonlinear functions": 50,
    "statistic and probability/One-variable statistics/One-variable statistics": 51,
    "calculate/Percents/Percents": 52,
    "geometry/Two-dimensional figures/Perimeter and area": 53,
    "calculate/Number theory/Prime factorization": 54,
    "calculate/Number theory/Prime or composite": 55,
    "statistic and probability/Probability/Probability of compound events": 56,
    "statistic and probability/Probability/Probability of one event": 57,
    "statistic and probability/Probability/Probability of simple events and opposite events": 58,
    "calculate/Ratios and rates/Proportional relationships": 59,
    "geometry/Coordinate plane/Quadrants": 60,
    "calculate/Rational and irrational numbers/Rational and irrational numbers": 61,
    "geometry/Scale drawings/Scale drawings": 62,
    "geometry/Slope/Slope": 63,
    "calculate/basic calculate/Square roots and cube roots": 64,
    "geometry/Three-dimensional figures/Surface area and volume": 65,
    "Expressions, Equations and Functions/equations/Systems of equations": 66,
    "geometry/Two-dimensional figures/Triangle": 67,
    "statistic and probability/Two-variable statistics/Two-variable statistics": 68,
    "calculate/Integers/absolute value": 69,
    "geometry/Coordinate plane/axes": 70,
    "statistic and probability/Data/center and variability": 71,
    "geometry/Two-dimensional figures/circle": 72,
    "calculate/Number theory/factors": 73,
    "statistic and probability/Probability/independent and dependent events": 74,
    "Expressions, Equations and Functions/inequalities/inequalities": 75,
    "statistic and probability/Data/mean, median, mode, and range": 76,
    "calculate/Integers/opposite integers": 77,
    "statistic and probability/Data/outlier": 78,
    "geometry/Two-dimensional figures/polygons": 79,
    "geometry/Three-dimensional figures/polyhedra": 80,
    "Expressions, Equations and Functions/Expressions/radical expressions": 81,
    "geometry/Transformations/reflections, rotations, and translations": 82,
    "geometry/Two-dimensional figures/square": 83,
    "geometry/Two-dimensional figures/trapezoids": 84,
    "Expressions, Equations and Functions/Expressions/variable expressions": 85
}

    if type == 'element_zh':
        return cate2id_element_zh
    elif type == 'middle_zh':
        return cate2id_middle_zh
    elif type == 'element_en':
        return cate2id_element_en
    elif type == 'middle_en':
        return cate2id_middle_en