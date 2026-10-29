"""Generate exploration_map.svg: every route tried so far, with its status.

Edit the COLUMNS data and re-run; render to PNG with headless Edge.
"""
from xml.sax.saxutils import escape

STYLE = {
    'strict':   dict(fill='#fdedec', stroke='#c0392b', sw=2.2, dash=None, tag='✗ 定理', tagc='#c0392b'),
    'analysis': dict(fill='#fdf2ec', stroke='#c0392b', sw=1.6, dash='6,4', tag='✗ 分析', tagc='#a04000'),
    'numeric':  dict(fill='#fdf2ec', stroke='#c0392b', sw=1.6, dash='2,3', tag='✗ 数值', tagc='#a04000'),
    'ffonly':   dict(fill='#eafaf1', stroke='#27ae60', sw=2.0, dash=None, tag='✓ 仅函数域', tagc='#1e8449'),
    'cond':     dict(fill='#fef9e7', stroke='#b7950b', sw=2.0, dash=None, tag='条件性', tagc='#7d6608'),
    'pending':  dict(fill='#fdebd0', stroke='#e67e22', sw=3.0, dash=None, tag='⏳ 待测', tagc='#ca6f1e'),
    'low':      dict(fill='#f8f9f9', stroke='#999999', sw=1.5, dash='7,5', tag='◌ 低优先', tagc='#777777'),
    'proved':   dict(fill='#d5f5e3', stroke='#27ae60', sw=2.0, dash=None, tag='✓ 已证', tagc='#1e8449'),
}

COLUMNS = [
    ('原始路线：七岛审计', '#1e8449', [
        ('strict', '桥 A（算子桥）', 'Gate A 就是孪生残差本身'),
        ('strict', '桥 B（动力学桥）', '柱集判据包含了自己的结论'),
        ('strict', '度量型证书（定理 5.5）', '同质量的对抗族：到不了种子点'),
        ('proved', '条件通路（定理 B）', 'GEH + PND_log ⟹ 孪生；显式形式'),
        ('proved', '两边相干（定理 C）', '粗糙数对上只有一个奇偶参数 δ'),
    ]),
    ('奇偶桥：已知机制', '#922b21', [
        ('strict', '膨胀 + 谱法（定理 A）', 'Tao / HR / Pilatte：z ≤ exp(O(√log x))'),
        ('strict', '熵递减（定理 E）', '只到 z ≤ (log x)^O(ε⁴)'),
        ('numeric', 'LDPT 方案的 L4 环节', '粗糙子图平均度 → 0（x 到 10⁸）'),
        ('analysis', 'FI 双线性假设 (B)', '对孪生"奇偶完备"：μ×μ 或 √x 障碍'),
        ('analysis', 'Lü–Wang–Wu 机制', '只到 z ≤ exp((log x)^(1/5))'),
    ]),
    ('新对称性筛查（9 类）', '#873600', [
        ('strict', '大素数膨胀', '定理 A 的粗糙膨胀情形'),
        ('analysis', '提取少数大素数', '落入 √x 障碍（任意系数）'),
        ('analysis', 'Gowers / 高阶 Fourier', '孪生是无穷复杂度模式'),
        ('analysis', '自守 / 谱（Kuznetsov）', 'λ 不是自守的，无法转移'),
        ('analysis', '数域 spin 符号（FI）', '分裂代数 Q×Q：没有非平凡符号'),
        ('cond', 'Siegel 零点（Heath-Brown）', '仅在 Siegel 零点存在时成立'),
        ('analysis', '遍历 / Furstenberg 系统', '粗糙度随尺度变：无固定极限系统'),
        ('analysis', 'Fourier 展开 / Chen 换位', '只携带 Type I：奇偶原理挡住'),
        ('ffonly', '函数域 Pellet 公式', 'μ=(−1)^deg·χ(disc f)；整数无类比'),
    ]),
    ('大胆假设（H 系列）', '#1f618d', [
        ('strict', 'H1 算术导数的 Jacobi 符号', '恒等式 (n′/n)=(−1)^(k(k−1)/2)'),
        ('analysis', 'H2 换奇偶检测函数', '由定理 4.1：奇偶只有一维'),
        ('numeric', 'H5 λ 在粗糙数上低复杂度', '实测符号熵 ≈ 每位 1 bit'),
        ('strict', 'H3 奇偶线性规划', '独立延拓：δ=0 世界可行（模型内）'),
        ('numeric', 'H6 大进位制 Pellet 类比', '与数字多项式的函数域 μ 无关（10⁸）'),
        ('low', 'H7 粗糙尺度二分法', '第二分支 = 粗糙数上的 Chowla'),
    ]),
]

W, COLW, GAP, X0 = 1400, 310, 20, 40
BOXH, STEP, Y0 = 70, 80, 150
nmax = max(len(c[2]) for c in COLUMNS)
H = Y0 + nmax * STEP + 170


def t(x, y, s, size=13, weight='normal', fill='#222', anchor='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}">{escape(s)}</text>')


out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
       f'font-family="Microsoft YaHei, PingFang SC, Noto Sans CJK SC, sans-serif">',
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
       t(W / 2, 44, '孪生素数奇偶桥 · 探索地图：试过哪些路，为什么不通', 25, 'bold'),
       t(W / 2, 72, '2026-10-27 · 论文 v0.7 · 所有结论均为 AI 辅助得出：“定理”有完整证明但尚待专家核查，“分析/数值”是判断而非定理', 13, fill='#666')]

for ci, (title, color, items) in enumerate(COLUMNS):
    x = X0 + ci * (COLW + GAP)
    out.append(f'<rect x="{x}" y="92" width="{COLW}" height="40" rx="8" fill="{color}"/>')
    out.append(t(x + COLW / 2, 118, title, 16, 'bold', '#ffffff'))
    for k, (st, name, why) in enumerate(items):
        s = STYLE[st]
        y = Y0 + k * STEP
        dash = f' stroke-dasharray="{s["dash"]}"' if s['dash'] else ''
        out.append(f'<rect x="{x}" y="{y}" width="{COLW}" height="{BOXH}" rx="9" fill="{s["fill"]}" '
                   f'stroke="{s["stroke"]}" stroke-width="{s["sw"]}"{dash}/>')
        out.append(t(x + 12, y + 27, name, 14, 'bold', '#222', 'start'))
        out.append(t(x + COLW - 10, y + 27, s['tag'], 12, 'bold', s['tagc'], 'end'))
        out.append(t(x + 12, y + 53, why, 12, 'normal', '#444', 'start'))

# summary band
ys = Y0 + nmax * STEP + 12
out.append(f'<rect x="{X0}" y="{ys}" width="{W - 2 * X0}" height="62" rx="10" fill="#fef9e7" stroke="#b7950b" stroke-width="2"/>')
out.append(t(W / 2, ys + 26, '共同障碍：已知的奇偶突破都依赖“许多小素数处的乘性”或整数没有的代数结构；', 15, 'bold', '#7d6608'))
out.append(t(W / 2, ys + 49, '孪生奇偶参数活在 x^η-粗糙、至多 1/η 个素因子的数上，两类资源都缺失。H 系列：H1–H6 均已判死，H7 低优先。', 15, 'bold', '#7d6608'))

# legend
yl = ys + 88
legend = ['strict', 'analysis', 'numeric', 'proved', 'ffonly', 'cond', 'pending', 'low']
names = {'strict': '严格证明不通', 'analysis': '分析判死', 'numeric': '数值判死', 'proved': '已证（正面结果）',
         'ffonly': '仅函数域成立', 'cond': '条件性成立', 'pending': '待测', 'low': '低优先'}
lx = X0
for k in legend:
    s = STYLE[k]
    dash = f' stroke-dasharray="{s["dash"]}"' if s['dash'] else ''
    out.append(f'<rect x="{lx}" y="{yl}" width="26" height="16" rx="4" fill="{s["fill"]}" stroke="{s["stroke"]}" stroke-width="{s["sw"]}"{dash}/>')
    out.append(t(lx + 34, yl + 13, names[k], 13, 'normal', '#333', 'start'))
    lx += 34 + 14 * len(names[k]) + 26
out.append('</svg>')
open('exploration_map.svg', 'w', encoding='utf-8').write('\n'.join(out))
print('wrote exploration_map.svg', W, 'x', H)
