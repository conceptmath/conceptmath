
def get_few_shot_prompt(grade_type):
    if grade_type == 'element_zh':
        dialog_prompt = [
            {'role': 'user', 'content': '小文用量角器测量一个角的度数时，误把外圈刻度看成了内圈刻度，量出的角是65°，这个角实际是多少度？'}, 
            {"role": "assistant", 'content': '量角器一般有两个圈的刻度，内圈刻度通常是顺时针方向从0度到180度，外圈刻度通常是逆时针方向从0度到180度。如果小文误把外圈刻度看成了内圈刻度，那么测量出的角度其实是从180°减去错误读数。因此，实际的角度应该是：180° - 65° = 115°。\n因此，答案是115。'}, 
            {'role': 'user', 'content': '小明以每小时2千米的速度上山，到了山顶后立即以每小时3千米的速度按原路返回。求小明上下山的平均速度是多少千米？'}, 
            {"role": "assistant", 'content': '要计算小明上下山的平均速度，我们需要知道他上山和下山所走的总距离以及总时间。\n首先，总距离 = 上山距离+下山距离=d+d= 2d千米。\n然后，计算总时间：上山时间 = 上山距离/上山速度 = d/2小时，下山时间 = 下山距离/下山速度 = d/3小时，因此，总时间=上山时间+下山时间 = d/2 + d/3小时。\n最后，计算平均速度：平均速度=总距离 / 总时间 = 2d / (d/2 + d/3) = 2d / (5d/6) = 12 / 5 = 2.4千米/小时。\n因此，答案是2.4千米/小时。'}, 
            {'role': 'user', 'content': '一个礼盒长20cm、宽15cm、高10cm，用彩带捆扎这样的一个礼盒，至少需要多长的彩带？（接头处12厘米）'}, 
            {"role": "assistant", 'content': '要捆扎这样一个礼盒，通常情况下我们会沿着礼盒的长和宽方向各绕一圈，即绕过礼盒的长和宽两次，然后再留一些长度作为接头。\n首先，计算沿着礼盒的长方向绕一圈的长度：绕长方向长度 = （礼盒的长 + 礼盒的高）* 2 = （20 + 10）* 2 = 30 * 2 = 60 cm\n然后，计算沿着礼盒的宽方向绕一圈的长度：绕宽方向长度 = （礼盒的宽 + 礼盒的高）* 2 = （15 + 10）* 2 = 25 * 2 = 50 cm\n最后，计算总需要彩带长度：总长度 = 绕长方向长度 + 绕宽方向长度 + 接头长度 = 60 + 50 + 12 = 122 cm\n因此，答案是122厘米。'}, 
            {'role': 'user', 'content': '千岛湖大桥的一侧每隔10米安装1盏灯，共需91盏（两端都装），现在改装61盏（两端都装），平均每相邻两盏灯之间的距离是多少米？'}, 
            {"role": "assistant", 'content': '原来每隔10米安装1盏灯，共需91盏，这意味着桥的总长度覆盖了90个10米的间隔，所以桥的总长度 = 90间隔 * 10米/间隔 = 900米。\n现在改装61盏灯（两端都装），也就是说将这900米分成60个间隔（因为61个灯包含了两端的灯，所以间隔数比灯的数量少一个），每个间隔的长度 = 900米 / 60间隔 = 15米/间隔。\n因此，答案是115米。'}, 
            {'role': 'user', 'content': 'a是b的3/4，则a比b少(  )，b比a多(  )，b与a的比是(  )，如果a、b两数的和是210，则a＝(  )，b＝(  )，括号处分别为多少？'}, 
            {"role": "assistant", 'content': '已知a是b的3/4，则a = 3/4  * b。因此，a比b少 (1-3/4)/1 = 1/4，b比a多（1-3/4)/(3/4) = 1/3，b与a的比为b : (3/4 * b) = 4:3\n若已知a、b两数的和是210，则a+b = 210，将a = (3/4) * b 代入方程得到：3/4 * b + b  = 210，解得b = 120，a = 3/4 * b = 3/4 * 120 = 90\n因此，答案分别是 1/4，1/3，4:3，90，120。'}]

    elif grade_type == 'middle_zh':
        dialog_prompt = [
            {'role': 'user', 'content': '不等式-x^2-2x+8>0的解集为？'}, 
            {"role": "assistant", 'content': '-x^2 - 2x + 8 > 0，通过分解因式方式，得到 -(x - 2)(x + 4) > 0\n因此，答案是 (-4, 2)。'}, 
            {'role': 'user', 'content': '已知函数y=2x+3与的图象y=-1/2x+m交y轴于点A、B，两函数图象的交点为P(n,-2)，求m和n的值？'},
            {"role": "assistant", 'content': '两函数图像交点为P(n,-2)，意味着这个点同时满足上述两个函数方程：\n将P点的坐标(n,-2)代入函数y=3x+3，即-2=3n+3，解得n=-5/2。\n将P点坐标(-5/2,-2)代入函数y=-1/2x+m，即-2=-1/2*(-5/2)+m，解得m=-13/4。\n因此，答案是m为-13/4，n为-5/2。'}, 
            {'role': 'user', 'content': '已知PA是圆O的切线，A为切点，PC与圆O相交于B、C两点，PB=2cm，BC=8cm，则PA的长是多少厘米？'}, 
            {"role": "assistant", 'content': '由于PA是圆O的切线，根据切割线定理，我们知道从圆外一点引圆的两条割线，这一点到每条割线与圆的交点的两条线段长的积相等，即PA^2 = PC * PB ,\n已知PB=2cm、BC=8cm，则PC = PB + BC = 2cm + 8cm = 10cm。\nPA^2 = PC * PB  = 10 * 2 = 20，解得PA = 2\\sqrt{5} cm。\n因此，答案是2\\sqrt{5}厘米。'}, 
            {'role': 'user', 'content': '南宋著名数学家杨辉精研数学，著有《详解九章算法》，对数的运算进行了深入研究与总结，类比其中的思想方法，可以解决很多数与式的计算问题已知a，b为实数，且a+b=3，ab=1，计算可得：a^2+b^2=7，a^3+b^3=18，a^4+b^4=47，由此求a^5+b^5得多少？'},
            {"role": "assistant", 'content': '已知 a + b = 3和 ab = 1，可得：\na^2 + b^2 = (a + b)^2 - 2ab = 3^2 - 2 * 1 = 9 - 2 = 7\na^3 + b^3 = (a + b)(a^2 - ab + b^2) = 3(7 - 1) = 3 * 6 = 18\na^4 + b^4 = (a^2 + b^2)^2 - 2a^2b^2 = 7^2 - 2 * 1^2 = 49 - 2 = 47\na^5 + b^5 = (a + b)(a^4 - a^3b + a^2b^2 - ab^3 + b^4) = 3(a^4 + b^4 - a^2b^2) = 3(47 - 1) = 3 * 46 = 138。\n因此，答案是138。'}, 
            {'role': 'user', 'content': '某单位要招聘1名英语翻译，甲、乙两人报名参加了听、说、读、写等项素质测试，甲的成绩分别为：90分、80分、85分、78分；乙的成绩分别为：78分、82分、85分、88分．如果把听、说、读、写的成绩按2:2:3:3计算素质测试平均成绩，那么甲和乙的平均成绩分别是多少？'}, 
            {"role": "assistant", 'content': '甲的平均成绩为 (90*2 + 80*2 + 85*3 + 78*3) / (2+2+3+3) = (180 + 160 + 255 + 234) / 10 = 829 / 10 = 82.9 分，乙的平均成绩为 (78*2 + 82*2 + 85*3 + 88*3) / (2+2+3+3) = (156 + 164 + 255 + 264) / 10 = 839 / 10 = 83.9 分。\n因此，答案是甲的平均成绩是82.9分，乙的平均成绩是83.9分。'}]

    elif grade_type == 'element_en':
        dialog_prompt = [
            {"role": "user","content": "For a party, Oscar gets 4 different kinds of soda. He buys a 6-pack of each kind. At home, he divides the sodas evenly among 3 coolers. How many sodas are in each cooler?"},
            {"role": "assistant","content": "Oscar buys 4 different kinds of soda, and he gets a 6-pack of each kind. This means that he has 4 * 6 = 24 sodas in total.\nHe divides these 24 sodas evenly among 3 coolers. So number of sodas per cooler is 24 / 3 = 8.Therefore, the answer is 8."},
            {"role": "user","content": "Amazing Animals Zoo is building a new home for its 8 zebras. Each zebra will get 2 acres of grassy land to roam around in. The zebras will have a pond that covers 1 acre. How big will the zebras' new home be?"},
            {"role": "assistant","content": "The total required grassland area for the zebras is: 8 zebras * 2 acres per zebra = 16 acres. Then, we need to add the extra 1 acre for the pond: 16 acres (for the zebras) + 1 acre (for the pond) = 17 acres. Therefore, the answer is  17."},
            {"role": "user","content": "The state taxes personal income exceeding 3500 yuan (this portion not to exceed 3500 yuan) at a rate of 3%. If Xiaoming's father's monthly salary is 4700 yuan, how much personal income tax should Xiaoming's father pay each month?"},
            {"role": "assistant","content": "To calculate the amount of personal income tax Xiaoming's father should pay, we can follow this simple process:\nSubtract the tax-free threshold from the monthly salary. Taxable income = Monthly salary - Tax-free threshold = 4700 - 3500 = 1200 yuan.\nApply the tax rate to the amount that exceeds the threshold. Tax owed = Taxable income × Tax rate = 1200 × 3% = 36 yuan.\nTherefore, the answer is 36."},
            {"role": "user","content": "Find the 10th term in the arithmetic sequence where the first term is 3 and the common difference is 4."},
            {"role": "assistant","content": "To find the nth term in an arithmetic sequence, we can use the formula: a_n = a_1 + (n - 1) * d, where: a_n is the nth term, a_1 is the first term, d is the common difference, n is the term number.\nGiven that the first term (a_1) is 3 and the common difference (d) is 4, we can find the 10th term (a_10) by plugging these values into the formula:  a_10 = a_1 + (10 - 1) * d = 3 + 9 * 4 = 3 + 36 = 39.\nTherefore, the answer is 39."},
            {"role": "user","content": "A regular polygon has an interior angle of 156 degrees. How many sides does the polygon have?"},
            {"role": "assistant","content": "To find the number of sides of a regular polygon with a given interior angle, we can use the formula: Interior Angle = [(n - 2) * 180] / n, where n is the number of sides. Given that interior angle is 156 :  156 = [(n - 2) * 180] / n. Solve for n, so we get n = 15. Therefore, the answer is  15."}
        ]   
    elif grade_type == 'middle_en':
        dialog_prompt = [
            {'role': 'user', 'content': 'g(x) = x^2, f(x) = 3(x-2)^2, h(x)=g(x)-f(x), y=h(23), give me the value of y.'}, 
            {"role": "assistant", 'content': 'First, calculate g(23) and f(23): g(23) = 23^2 = 529.\nNext, calculate f(23): f(23) = 3(23-2)^2 = 3(21)^2 = 3 * 441 = 1323.\nNow, we calculate h(23): h(23) = g(23) - f(23) = 529 - 1323 = -794.\nTherefore, the answer is -794.'}, 
            {'role': 'user', 'content': 'What is the slope of the line segment between the two points: (3,1), (5,2)?'}, 
            {"role": "assistant", 'content': 'The slope of a line between two points (x1, y1) and (x2, y2) can be found using the formula: slope (m) = (y2 - y1) / (x2 - x1). \nGiven the two points (3, 1) and (5, 2), we can substitute these values into the formula: slope (m) = (2 - 1) / (5 - 3) = 1/2 = 0.5.\nTherefore, the answer is 1/2.'}, 
            {'role': 'user', 'content': 'In a party, there are 5 cupcakes remaining and 10 children. A mother inserts 10 pieces of paper into a hat, 5 with a cupcake image and 5 without. The children who draw the cupcake paper will receive a cupcake. If the first child draws a paper with a cupcake image, what is the probability that the second child will also draw a cupcake paper?'}, 
            {"role": "assistant", 'content': 'Initially, there are 5 cupcake papers and 5 non-cupcake papers in the hat, making a total of 10 papers. After the first child draws a cupcake paper, there are 4 cupcake papers and 5 non-cupcake papers left in the hat, with a total of 9 papers.\nThe probability that the second child will draw a cupcake paper is then the number of cupcake papers left divided by the total number of papers left:\nProbability = Number of cupcake papers left / Total number of papers left = 4/9. \nTherefore, the answer is 4/9.'}, 
            {'role': 'user', 'content': 'What is the total area of an irregular polygon that consists of two squares and two rectangles where the sides of the squares are 12 cm and 16 cm respectively, and the dimensions of the rectangles are 13 cm by 20 cm and 10 cm by 7 cm respectively?'}, 
            {"role": "assistant", 'content': 'To find the total area of an irregular polygon consisting of two squares and two rectangles, you would sum up the individual areas of each shape.\nThe area of a square is given by the formula  A = s^2, where s is the length of a side of the square.\nFor the first square with a side of 12 cm: A_1 = 12^2 = 144 cm^2.\nFor the second square with a side of 16 cm: A_2 = 16^2 = 256 cm^2.\nThe area of a rectangle is given by the formula ( A = l \times w ), where ( l ) is the length and ( w ) is the width of the rectangle.\nFor the first rectangle with dimensions 13 cm by 20 cm: A_3 = 13 \times 20 = 260 cm^2\nFor the second rectangle with dimensions 10 cm by 7 cm: A_4 = 10 \times 7 = 70 cm^2\nTota Area = A_1 + A_2 + A_3 + A_4 = 144 + 256 + 260 + 70 = 730 cm^2\nTherefore, the answer is 730.'}, 
            {'role': 'user', 'content': 'Susie is making invitations to her party this coming weekend. It takes her about 5 minutes to make each invitation. It took her 2 hours to finish all the invitations. How many people is Susie inviting?'}, 
            {"role": "assistant", 'content': 'First, convert the 2 hours into minutes to match the unit of time used for the invitation-making process. 2 hours = 120 minutes.\nThen, divide the total time spent by the time it takes to make one invitation to find out how many invitations she made: 120 minutes total / 5 minutes per invitation = 24 invitations\nTherefore, the answer is 24.'}]

    return dialog_prompt