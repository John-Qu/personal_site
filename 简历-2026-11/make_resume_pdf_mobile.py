# -*- coding: utf-8 -*-
"""生成《曲政-包装机械-手机版简历》PDF：窄长单页、大字体、适合手机滑动阅读"""
import os
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable)

regular_font = os.environ.get('DAIMON_CJK_FONT_REGULAR')
bold_font = os.environ.get('DAIMON_CJK_FONT_BOLD')
if not regular_font or not bold_font:
    raise RuntimeError('Daimon managed CJK fonts are unavailable')
pdfmetrics.registerFont(TTFont('CJK', regular_font))
pdfmetrics.registerFont(TTFont('CJK-Bold', bold_font))
pdfmetrics.registerFontFamily('CJK', normal='CJK', bold='CJK-Bold',
                              italic='CJK', boldItalic='CJK-Bold')

INK = HexColor('#222222')
GRAY = HexColor('#666666')
ACCENT = HexColor('#1a4f8a')

S = {}
S['name'] = ParagraphStyle('name', fontName='CJK-Bold', fontSize=22, leading=27,
                           alignment=TA_CENTER, textColor=INK)
S['tagline'] = ParagraphStyle('tagline', wordWrap='CJK', fontName='CJK', fontSize=11,
                              leading=15, alignment=TA_CENTER, textColor=GRAY)
S['contact'] = ParagraphStyle('contact', wordWrap='CJK', fontName='CJK', fontSize=10,
                              leading=14.5, alignment=TA_CENTER, textColor=INK)
S['h'] = ParagraphStyle('h', fontName='CJK-Bold', fontSize=13.5, leading=17,
                        spaceBefore=14, spaceAfter=5, textColor=ACCENT)
S['job'] = ParagraphStyle('job', wordWrap='CJK', fontName='CJK-Bold', fontSize=11,
                          leading=15.5, spaceBefore=7, spaceAfter=2, textColor=INK)
S['body'] = ParagraphStyle('body', wordWrap='CJK', fontName='CJK', fontSize=10.5,
                           leading=16.5, textColor=INK)
S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=10,
                             spaceAfter=2)
S['small'] = ParagraphStyle('small', wordWrap='CJK', fontName='CJK', fontSize=9.5,
                            leading=14, textColor=GRAY)

def L(text, url):
    return f'<a href="{url}" color="#1a4f8a"><u>{text}</u></a>'

def job(title, bullets):
    out = [Paragraph(title, S['job'])]
    out += [Paragraph('• ' + b, S['bullet']) for b in bullets]
    return out

story = []
story.append(Paragraph('曲 政', S['name']))
story.append(Paragraph('包装机械技术支持工程师', S['tagline']))
story.append(Paragraph('凸轮机构与运动学仿真 ｜ 懂技术的销售', S['tagline']))
story.append(Spacer(1, 4))
story.append(Paragraph(
    '上海 · 186-0179-3762<br/>JohnQuicker@163.com<br/>个人网站 '
    + L('johnqu.site', 'https://johnqu.site/')
    + '<br/>（蓝色文字均可点击，跳转对应项目网页）', S['contact']))
story.append(Spacer(1, 6))
story.append(HRFlowable(width='100%', thickness=0.8, color=ACCENT))

story.append(Paragraph('个人概述', S['h']))
story.append(Paragraph(
    '上海交通大学机械设计及理论硕士，十七年机械行业经验，现为独立技术支持工程师。'
    '职业主线是食品包装机械：研究生期间参与利乐高速灌装机专利规避研发；'
    '在普丽盛把图纸落到工厂、凭利乐手册推演结构；'
    '在曼亿主持对标意大利 G.Mondini（蒙地尼）托盒封口机的国产化设计。'
    '其间经历三年精密装配一线（第一精工）与四年技术销售（日电产东测、晋兆），'
    '既懂设计，又懂现场和客户。2018 年起自学编程，用 Python 做凸轮曲线计算与运动学仿真。'
    '2026 年元旦后自上海曼亿离职，可独立承接凸轮动作优化等现场技术支持，随时可到厂。', S['body']))

story.append(Paragraph('核心能力', S['h']))
for b in [
    '凸轮机构设计与运动学仿真：用 Python（NumPy/Matplotlib）自建工具链，'
    '复现过利乐 A3-Flex 柔性机双夹爪电子凸轮曲线。',
    '食品包装机械：无菌灌装机（利乐对标）、托盒封口机（G.Mondini 对标）的结构设计与国产化。',
    '逆向与正向结合：凭图纸与备件/维修手册推演原厂结构；SolidWorks / FreeCAD 参数化建模。',
    '现场能力：三年自动装配机调试一线；技术销售出身，擅长在现场定位问题、与客户把方案谈清楚。',
    '语言：英语（CET-6，熟读利乐手册与欧美技术文档）、日语（JLPT-N2）。',
]:
    story.append(Paragraph('• ' + b, S['bullet']))

story.append(Paragraph('工作经历', S['h']))

story += job('上海曼亿包装机械有限公司 —— 设计科长（2024.04 – 2025.12）', [
    '主持对标意大利 G.Mondini（蒙地尼）托盒封口机的国产化，'
    '涉及高速托盒机、四盒托盒机与单盒托盒机。',
    '建立"设计复盘"机制：测绘图纸之外要求提交设计决策文档，'
    '把仿制过程沉淀为可复用的设计资产。',
    '离职前完成新型上模结构设计，实现放模、张模、拉模、收模的完整动作序列。',
])
story += job('上海晋兆智能技术有限公司 —— 技术销售经理 / 解决方案工程师（2021.09 – 2024.03）', [
    '技术转销售的第二站，做一名"懂技术的销售"：直接面对客户的测量与自动化需求，'
    '现场出方案、跟到底。',
    '主导圆柱电池充放电测量工装开发：FreeCAD 全参数化建模，'
    '在极度受限的空间内一次性通过客户验收。',
])
story += job('自由职业 · 技能重塑期（2017.03 – 2021.09）', [
    '全职育儿期间系统自学计算机科学（MIT 6.00）与全栈开发，完成机械与软件的跨界。',
    '独立项目：用 Python 复现并生成利乐 A3-Flex 柔性机双夹爪电子凸轮曲线，'
    '替代昂贵的商业仿真软件，形成可复用的凸轮设计工具链，'
    '代码已开源（' + L('GitHub：John-Qu/tetracamthon', 'https://github.com/John-Qu/tetracamthon') + '）。',
])
story += job('日电产东测（Nidec Tosok）—— 售前技术 / 客户经理（2015.10 – 2017.02）', [
    '技术转销售的第一步：精密测量设备的售前技术支持与客诉处理，'
    '跑遍压缩机、汽车零部件客户现场，练就"听懂客户问题、协调资源解决问题"的能力。',
])
story += job('上海第一精工模塑 —— 制造工程师·自动装配方向（2012.06 – 2015.09）', [
    '主动从研发岗下沉到装配一线：精密自动装配机（组立机）装配与调试三年，'
    '积累公差配合、润滑特性与精密调试的一手经验，反哺后续设计的可装配性。',
])
story += job('上海普丽盛包装 —— 研发工程师（2009.03 – 2012.05）', [
    '把上海交大课题的设计图纸落实到工厂：柔性灌装机原理样机、'
    '高速机终端排包机构试验样机的制图、试制与装配调试。',
    '仅凭利乐图纸、备件手册（SPC）与维修手册（MM）推演机械结构，'
    '重构 A3-Flex 柔性机的夹爪与驱动部分。',
])

story.append(Paragraph('教育背景', S['h']))
story += job('上海交通大学 机械设计及理论 工学硕士（2006 – 2009）', [
    '在校期间跟随导师参与利乐牛奶高速灌装机终端排包机构研发，'
    '以突破利乐专利壁垒为目标，完成方案设计并试制出实物样机。',
])
story.append(Paragraph('大连理工大学 机械设计制造及其自动化 工学学士（2002 – 2006）', S['job']))

story.append(Paragraph('项目证明（点击蓝色文字打开）', S['h']))
for b in [
    '凸轮攻关起点（2019.03，总结普丽盛时期的积累，再出发）：'
    + L('《利乐柔性凸轮问题的新起点》', 'https://johnqu.site/cn/2019/03/new-start-line/'),
    '凸轮攻关终点（2019.12，大包型全程凸轮曲线算出，附曲线图）：'
    + L('《怎样让同行感兴趣》', 'https://johnqu.site/cn/2019/12/colleage-interest/'),
    '调试过程记录（曲线合成，附图）：'
    + L('《小段差是小问题吗》', 'https://johnqu.site/cn/2019/11/stage-difference/'),
    '普丽盛三年项目清单：'
    + L('《梳理三年工作的得失利弊》', 'https://johnqu.site/cn/2012/01/what-I-have-done-in-three-years/'),
    '在线简历：' + L('johnqu.site/cn/resume', 'https://johnqu.site/cn/resume'),
    '在线完整履历：' + L('johnqu.site/cn/vitae', 'https://johnqu.site/cn/vitae'),
]:
    story.append(Paragraph('• ' + b, S['bullet']))

story.append(Paragraph('对标设备参考', S['h']))
story.append(Paragraph('• 利乐 '
    + L('A3/CompactFlex（A3-Flex）无菌灌装机', 'https://www.tetrapak.com/solutions/integrated-solutions-equipment/filling-machines/tetra-pak-a3-compactflex'), S['bullet']))
story.append(Paragraph('• '
    + L('G.Mondini Trave 托盒封口机', 'https://www.gmondini.com/solution/trave'), S['bullet']))

story.append(Spacer(1, 8))
story.append(HRFlowable(width='100%', thickness=0.5, color=GRAY))
story.append(Paragraph('服务过的客户（技术销售期间）：苏州大金、上海海立、沈阳三洋、天津 LG、'
                       '大连松下、南昌海立、广汽发动机、东风本田、柳州五菱、昆明云内等。', S['small']))

# 先测量内容总高，再用刚好够高的单页生成，实现"长条不分页"
W = 100 * mm
ML = MR = 7 * mm
MT, MB = 9 * mm, 9 * mm
avail = W - ML - MR
total_h = sum(f.wrap(avail, 1000000)[1] + f.getSpaceBefore() + f.getSpaceAfter()
              for f in story)
out = '/Users/quzheng/Projects/johnqu_site/简历-2026-11/曲政-包装机械-手机版简历-2026-11.pdf'
doc = SimpleDocTemplate(out, pagesize=(W, 200 * mm),
                        topMargin=MT, bottomMargin=MB,
                        leftMargin=ML, rightMargin=MR,
                        title='曲政-包装机械-手机版简历', author='曲政')
doc.build(story)
from pypdf import PdfReader
print('written:', out, f'page = {W/mm:.0f}mm x 200mm, '
      f'{len(PdfReader(out).pages)} page(s)')
