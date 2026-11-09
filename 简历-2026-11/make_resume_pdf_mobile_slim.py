# -*- coding: utf-8 -*-
"""生成《曲政-包装机械-手机版简历（精简内容）》：一整条长页、无分页间隔"""
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
S['name'] = ParagraphStyle('name', fontName='CJK-Bold', fontSize=24, leading=29,
                           alignment=TA_CENTER, textColor=INK)
S['tagline'] = ParagraphStyle('tagline', wordWrap='CJK', fontName='CJK', fontSize=12,
                              leading=16, alignment=TA_CENTER, textColor=GRAY)
S['contact'] = ParagraphStyle('contact', wordWrap='CJK', fontName='CJK', fontSize=10.5,
                              leading=15, alignment=TA_CENTER, textColor=INK)
S['h'] = ParagraphStyle('h', fontName='CJK-Bold', fontSize=14, leading=18,
                        spaceBefore=14, spaceAfter=6, textColor=ACCENT)
S['job'] = ParagraphStyle('job', wordWrap='CJK', fontName='CJK-Bold', fontSize=11.5,
                          leading=16, spaceBefore=7, spaceAfter=2, textColor=INK)
S['body'] = ParagraphStyle('body', wordWrap='CJK', fontName='CJK', fontSize=11,
                           leading=17, textColor=INK)
S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=11,
                             spaceAfter=2)
S['small'] = ParagraphStyle('small', wordWrap='CJK', fontName='CJK', fontSize=10,
                            leading=14.5, textColor=GRAY)

def L(text, url):
    return f'<a href="{url}" color="#1a4f8a"><u>{text}</u></a>'

story = []
story.append(Paragraph('曲 政', S['name']))
story.append(Paragraph('包装机械设计工程师', S['tagline']))
story.append(Paragraph('凸轮机构与运动学仿真', S['tagline']))
story.append(Spacer(1, 4))
story.append(Paragraph(
    '上海 · 186-0179-3762<br/>JohnQuicker@163.com<br/>个人网站 '
    + L('johnqu.site', 'https://johnqu.site/')
    + '<br/>（蓝色文字均可点击，跳转对应项目网页）', S['contact']))
story.append(Spacer(1, 6))
story.append(HRFlowable(width='100%', thickness=0.8, color=ACCENT))

story.append(Paragraph('个人概述', S['h']))
story.append(Paragraph(
    '上海交通大学机械设计及理论硕士，十七年食品包装机械设计、制造与现场经验。'
    '研究生期间参与利乐牛奶灌装机专利规避研发；在普丽盛把交大课题的设计图纸落到工厂，'
    '并凭利乐图纸与备件、维修手册推演机械结构；自学编程后，用 Python 复现利乐 A3-Flex 柔性机'
    '双夹爪电子凸轮曲线；在曼亿主持对标意大利 G.Mondini（蒙地尼）托盒封口机的国产化设计。'
    '2026 年元旦后自曼亿离职，现可承接凸轮动作优化、结构改进与现场问题诊断，随时可到厂。', S['body']))

story.append(Paragraph('工作经历（包装机械相关）', S['h']))

story.append(Paragraph('上海曼亿包装机械有限公司 —— 设计科长（2024.04 – 2025.12）', S['job']))
story.append(Paragraph('• 主持对标意大利 G.Mondini（蒙地尼）托盒封口机的国产化，'
                       '涉及高速托盒机、四盒托盒机与单盒托盒机。', S['bullet']))
story.append(Paragraph('• 离职前完成新型上模结构设计，'
                       '实现放模、张模、拉模、收模的完整动作序列。', S['bullet']))

story.append(Paragraph('上海第一精工模塑 —— 制造工程师·自动装配方向（2012.06 – 2015.09）', S['job']))
story.append(Paragraph('• 精密自动装配机（组立机）装配与调试一线三年，'
                       '积累公差配合、精密调试与现场问题定位的一手经验。', S['bullet']))

story.append(Paragraph('上海普丽盛包装 —— 研发工程师（2009.03 – 2012.05）', S['job']))
story.append(Paragraph('• 把上海交大课题的设计图纸落实到工厂：参与柔性灌装机原理样机、'
                       '高速机终端排包机构试验样机的制图、试制与装配调试。', S['bullet']))
story.append(Paragraph('• 仅凭利乐图纸、备件手册（SPC）与维修手册（MM）推演机械结构，'
                       '重构 A3-Flex 柔性机的夹爪与驱动部分。', S['bullet']))

story.append(Paragraph('独立项目：利乐柔性机双夹爪电子凸轮曲线（2019，自学编程后完成）', S['job']))
story.append(Paragraph('• 用 Python 复现并生成 A3-Flex 双夹爪的凸轮运动曲线，'
                       '替代昂贵的商业仿真软件，形成一套可复用的凸轮设计工具链，'
                       '代码已开源（' + L('GitHub：John-Qu/tetracamthon', 'https://github.com/John-Qu/tetracamthon') + '）。', S['bullet']))

story.append(Paragraph('教育背景与在校期间课题', S['h']))
story.append(Paragraph('上海交通大学 机械设计及理论 工学硕士（2006 – 2009）', S['job']))
story.append(Paragraph('• 在校期间跟随导师参与利乐牛奶高速灌装机终端排包机构研发，'
                       '以突破利乐专利壁垒为目标，完成方案设计并试制出实物样机。', S['bullet']))

story.append(Paragraph('项目证明（点击蓝色文字打开）', S['h']))
story.append(Paragraph('• 凸轮攻关起点（2019.03，含机构示意图与加速度曲线）：'
    + L('《利乐柔性凸轮问题的新起点》', 'https://johnqu.site/cn/2019/03/new-start-line/'), S['bullet']))
story.append(Paragraph('• 凸轮攻关终点（2019.12，大包型全程凸轮曲线算出）：'
    + L('《怎样让同行感兴趣》', 'https://johnqu.site/cn/2019/12/colleage-interest/'), S['bullet']))
story.append(Paragraph('• 调试过程记录（曲线合成，附图）：'
    + L('《小段差是小问题吗》', 'https://johnqu.site/cn/2019/11/stage-difference/'), S['bullet']))
story.append(Paragraph('• 普丽盛三年项目清单：'
    + L('《梳理三年工作的得失利弊》', 'https://johnqu.site/cn/2012/01/what-I-have-done-in-three-years/'), S['bullet']))
story.append(Paragraph('• 在线简历：' + L('johnqu.site/cn/resume', 'https://johnqu.site/cn/resume')
    + '<br/>在线完整履历：' + L('johnqu.site/cn/vitae', 'https://johnqu.site/cn/vitae'), S['bullet']))

story.append(Paragraph('对标设备参考', S['h']))
story.append(Paragraph('• 利乐 '
    + L('A3/CompactFlex（A3-Flex）无菌灌装机', 'https://www.tetrapak.com/solutions/integrated-solutions-equipment/filling-machines/tetra-pak-a3-compactflex'), S['bullet']))
story.append(Paragraph('• '
    + L('G.Mondini Trave 托盒封口机', 'https://www.gmondini.com/solution/trave'), S['bullet']))

story.append(Spacer(1, 8))
story.append(HRFlowable(width='100%', thickness=0.5, color=GRAY))
story.append(Paragraph('核心能力：凸轮机构设计与运动学仿真（Python/NumPy/Matplotlib）· '
                       'SolidWorks / FreeCAD 参数化建模 · 食品包装机械（无菌灌装 / 托盒封口）· '
                       '英语（CET-6，熟读利乐/欧美技术文档）、日语（JLPT-N2）', S['small']))

# 测量内容总高，生成一整条长页（无分页间隔）
W = 100 * mm
ML = MR = 7 * mm
MT, MB = 9 * mm, 9 * mm
avail = W - ML - MR
total_h = sum(f.wrap(avail, 1000000)[1] + f.getSpaceBefore() + f.getSpaceAfter()
              for f in story)
H = total_h + MT + MB + 30  # 留少量余量，防止溢出

out = '/Users/quzheng/Projects/johnqu_site/简历-2026-11/曲政-包装机械-手机版简历-精简-2026-11.pdf'
doc = SimpleDocTemplate(out, pagesize=(W, H),
                        topMargin=MT, bottomMargin=MB,
                        leftMargin=ML, rightMargin=MR,
                        title='曲政-包装机械-手机版简历（精简）', author='曲政')
doc.build(story)

from pypdf import PdfReader
n = len(PdfReader(out).pages)
print('written:', out, f'page = {W/mm:.0f}mm x {H/mm:.0f}mm, {n} page(s)')
