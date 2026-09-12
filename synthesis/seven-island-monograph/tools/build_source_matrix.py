#!/usr/bin/env python3
"""Source inventory generation, validating selected files against frozen Git HEAD."""
import hashlib
import json
from pathlib import Path
import subprocess

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
BASE = 'd37c92b8a66bbd3d9084b1597d346429a9285302'
PHYSICAL = 'research/tpc-big-road/research-rounds/2026-09-09-physical-return-loop/'
ITEMS = [
 ('MAP', 'research/tpc-big-road/TPC_ISLAND_MAP_GUIDE.md', 'all', '路线含义；不是状态或定理证据'),
 ('STATUS', 'TPC_HANDOFF.md', '1-90', '当前结论边界；原证明另列'),
 ('BASELINE', 'papers/tpc-1-two-scale-prime-sieve-correlations/main.tex', '99-168;203-269;625-684', 'CRT、完整周期与端点尺度；经典输入'),
 ('ATOM', 'papers/tpc-127-determinant-two-liouville-pullback/main.tex', '75-199;251-385', '完整带掩码保序变换；无消去结论'),
 ('PAIR', 'papers/tpc-18-mobius-tail-determinant-dispersion/sections/opened-d-dispersion.tex', '4-57', '有序对的源系数；不是已构造的对到原子附接'),
 ('CHILD', 'papers/tpc-93-literal-low-window-affine-export/sections/decorated-affine-export.tex', '155-282', '保留源项的子项逆映射与带符号重组'),
 ('COVER', 'papers/tpc-117-full-block-physical-cover/main.tex', '98-205;263-303', '实际矩阵已提供后的带权覆盖判据'),
 ('LIFT', 'papers/tpc-143-frontier-occurrence-lift-contract/main.tex', '83-202', '已提供合法提升时的守恒；不构造生产提升'),
 ('COMPOSE', 'papers/tpc-205-pair-native-post-ttstar-registry-interface/main.tex', '119-155', '生产对复合的条件接口'),
 ('V59', 'research/tpc-big-road/bridge_b_polarized_local_bdh_scalar_compiler.md', 'all', '共同标量、极化、分割与条件账本；短数组条件以后续发射证明及外部原定理为准'),
 ('V58', 'research/tpc-big-road/bridge_b_terminal_scalar_root_and_q_transverse_split.md', '34-104;293-330', '导入终端接口、物理输出与399/400参照指数；Gate A和全标量节省仍是假设'),
 ('DYNAMICS', 'research/tpc-big-road/README.md', '5803-5929', '实际移动靶 CRT-Abel 方差证明；不包括指定点'),
 ('SEED', 'research/tpc-big-road/research-rounds/2026-09-09-multi-agent-recon/agent-reports/recon-distinguished-seed.md', '78-105', '源侦察报告中的充分引理；本稿重新给出证明，不沿用未经独立审计标识'),
 ('INTERTWINER', 'research/tpc-big-road/bridge_b_physical_intertwiner.md', '21-234;278-391', '精确复制删除、限定障碍与拟议物理回接'),
 ('CLOCK', 'research/tpc-big-road/bridge_b_euler_zero_axis_and_kernel_carrier.md', '758-802', '平稳混合系统的有限时钟因子障碍'),
 ('GEOMETRY', 'TPC_COMPASS.md', '6185-6193', '拟议几何附接条件；本稿不援引未经外部核验的 Hénon 文献定理'),
]
for name in ['DERIVATION_PACKAGE', 'PROOF_PACKAGE', 'LANE_NORM_PROOF', 'GROWING_RANK_PROOF',
             'REAL_GROWING_RANK_ADDENDUM', 'LOCAL_EMITTER_PROOF', 'NEXT_ARITHMETIC_OBLIGATION',
             'CONSTRUCTIVE_PARTITION_PROOF']:
    ITEMS.append(('PHYSICAL-'+name, PHYSICAL+name+'.md', 'all', '实际固定对象的限定证明；不是全体有符号估计'))

def main():
    rows = []
    for key, name, ranges, ceiling in ITEMS:
        path = ROOT / name
        raw = path.read_bytes()
        original = subprocess.check_output(['git', 'show', f'{BASE}:{name}'], cwd=ROOT)
        if raw != original:
            raise ValueError(f'Source differs from baseline: {name}')
        count = len(raw.splitlines())
        spans = [[1, count]] if ranges == 'all' else [[int(x) for x in r.split('-')] for r in ranges.split(';')]
        if any(not 1 <= a <= b <= count for a, b in spans):
            raise ValueError(f'Invalid source range: {name}')
        rows.append(dict(id=key, path=name, line_ranges=spans, sha256=hashlib.sha256(raw).hexdigest(),
                         claim_ceiling=ceiling, baseline_identical=True))
    (PROJECT / 'CORE_SOURCE_MATRIX.json').write_text(json.dumps(dict(baseline=BASE, sources=rows), ensure_ascii=False, indent=2)+'\n')
    lines = ['# 核心来源矩阵', '', f'基准提交：`{BASE}`。逐文件字节与该提交一致；散列只证明来源保真，不认证数学正确。',
             '正文按主题重组；原始 TeX/证明包为证据，Handoff 是状态，原图是导航。完整外部引用见 paper/references.bib。', '',
             '| 来源键 | 原始文件和行区间 | 声明边界 | SHA-256 |', '|---|---|---|---|']
    for row in rows:
        spans = ', '.join(f'{a}–{b}' for a,b in row['line_ranges'])
        lines.append(f"| {row['id']} | [{row['path']}](../../{row['path']})，{spans} | {row['claim_ceiling']} | `{row['sha256']}` |")
    (PROJECT / 'CORE_SOURCE_MATRIX.md').write_text('\n'.join(lines)+'\n')
    print(f'{len(rows)} exact source files validated against {BASE}')

if __name__ == '__main__':
    main()
