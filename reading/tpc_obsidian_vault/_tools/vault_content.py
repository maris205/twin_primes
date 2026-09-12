"""Curated navigation and source-backed explanatory cards, not new research."""
import json
from pathlib import Path
import re
from build_vault import DATE, SUMMARY, PHYSICAL, ISLANDS, properties, wiki, relative_link

CARDS = [
 dict(id='K01', title='局部筛密度与物理计数', island='1', papers=[1], sources=['BASELINE'],
      claim=r'CRT 给出完整 primorial 周期上的局部筛密度。平方根筛阈值可以识别素数对，但不能据此直接计数：该尺度下，朴素整周期截断的误差太大。',
      limit='这是所列两种论证适用尺度之间的缺口，不是对所有筛法的不可能定理。局部奇异级数因子不等于实际孪生素数渐近式。',
      related=[('K11','定义与终点区分'),('K10','局部质量与动力学事件的对应')]),
 dict(id='K02', title='实际物理标量与算子', island='2', papers=[], sources=['PHYSICAL-DERIVATION_PACKAGE','PHYSICAL-PROOF_PACKAGE'],
      claim=r'固定 $x=2X$、$I_x=(x/2,x]$、$h_0=2$，保留实际 $\beta,w$、完整素数壳层、单位掩码、中心化和对角删除。共同对象是 $\mathfrak C_x=\langle w,A\beta\rangle$，且 $A=T-R-\Delta$。',
      limit='固定 Fourier profile 不必为偶函数。A 是 Hermitian，但不必正半定；实系数之间的混合标量仍可为复数。精确分解不等于有符号消去。',
      related=[('K03','归一化代价'),('K04','低秩方法障碍'),('K13','定义解析账本消费的对象')]),
 dict(id='K03', title='行归一化为何没有支付标量节省', island='2', papers=[], sources=['PHYSICAL-LANE_NORM_PROOF'],
      claim=r'在完整物理区间上一致有 $G(u)\asymp HQ^2/\log Q$。实际系数范数的代价使所列系数无关范数乘积表达式至少仍为 $xQ^2/\log Q$ 量级，普通行归一化也不改变这一限制。',
      limit=r'这不是 $|\mathfrak C_x|$ 的下界，不是任意起点、任意前缀、每一种预条件器的定理。限制的是具体上界方法，而非实际系数之间的消去。',
      related=[('K02','对象定义'),('K13','方法障碍提醒')]),
 dict(id='K04', title='增长秩障碍与实复秩约定', island='2', papers=[], sources=['PHYSICAL-GROWING_RANK_PROOF','PHYSICAL-REAL_GROWING_RANK_ADDENDUM'],
      claim=r'存在至少 $k_x=Q^2/4-x^{11/32}+O(1)$ 个负方向，其规模为 $Q^2/(2\log Q)$；在各自明确的实秩或复秩约定下，秩低于 $k_x$ 的修补仍保留相应范数障碍。',
      limit='实见证与复见证使用不同定理和子空间。结论没有把实际算术系数识别为这些方向，也没有给出高于该秩的成功阈值，更不是实际标量下界。',
      related=[('K02','对象定义'),('K03','范数方法边界'),('K13','不能替代解析节省')]),
 dict(id='K05', title='Kloosterman精确发射与双侧短数组', island='2', papers=[], sources=['PHYSICAL-LOCAL_EMITTER_PROOF','PHYSICAL-NEXT_ARITHMETIC_OBLIGATION'],
      claim=r'完整发射数组的长度为 $q-1$，未删对角的正包具有完整范数饱和恒等式。即使第一侧只含两个坐标，另一侧完整且中心化，通用 Kloosterman 范数仍可达到 $q$。',
      limit='没有宣称实际算术系数就是极值向量。先带符号重组、删对角并积分后，仍可能有消去；要使用双侧临界短数组定理，必须另付压缩、重组和残差代价。',
      related=[('K02','保留实际对象'),('K13','尚待证明的双侧附接')]),
 dict(id='K06', title='已经支付的集体边界项', island='2', papers=[], sources=['PHYSICAL-CONSTRUCTIVE_PARTITION_PROOF'],
      claim=r'一个明确构造的 admissible 光滑分割具有统一缩放导数控制，其加权边界标签有序对的集体贡献满足 $xQ^2x^{-11/64+o(1)}$ 的上界。',
      limit=r'只处理边界集体贡献，不是每个正包，也不是任意事先给定的分割。内部有符号估计仍未证明；若内部节省为 $\delta_{\mathrm{int}}$，这一重组可认证的全节省为 $\min(\delta_{\mathrm{int}},11/64)$。',
      related=[('K02','原标量定义'),('K13','条件性边界重组接口')]),
 dict(id='K07', title='行列式二的带掩码保序拉回', island='3', papers=[127], sources=['ATOM'],
      claim=r'在源命题的正性、互素与行列式二假设下，$n=sV=aD+2$ 给出精确的保序改写，保留每个初始前缀，以及平方自由与互素掩码。',
      limit='这是一项对象识别恒等式，不是消去估计。相位和模数不能因为记号相同就被视为跨尺度固定。用于生产级实际原子时，仍需完整权重与支撑附接。',
      related=[('K08','条件性的pair到atom接口'),('K13','结构输入不等于桥梁估计')]),
 dict(id='K08', title='有序行对与带符号子项重组', island='4', papers=[18,93,205], sources=['PAIR','CHILD','COMPOSE'],
      claim=r'opened-$D$ 的有序行对与仿射原子是不同的载体。恢复源系数必须保留完整的带权子项求和以及原有支撑限制；单个子项不是源系数本身。',
      limit='生产级 pair-to-atom 复合仍以合法附接为条件。上下游都出现“packet”或同一编号，不能替代系数、掩码、顺序与归一化核对。',
      related=[('K07','条件性的原子拉回'),('K09','守恒不等于实际覆盖')]),
 dict(id='K09', title='出现项提升与带权覆盖', island='4', papers=[143,117], sources=['LIFT','COVER'],
      claim='给定满足条件的提升时，源文中的守恒恒等式成立；给定合法合成矩阵时，可以用值域、投影或正交障碍表述覆盖判据。',
      limit='这些结论本身没有构造生产级提升、证明实际活跃非零支撑已覆盖，或支付系数加权的运输代价。历史 DONE_L0 不能直接改写为“岛④已经完成”。',
      related=[('K08','对源子项重组的边界提醒'),('K07','保持物理对象')]),
 dict(id='K10', title='实际移动筛事件与Haar几乎处处命中', island='5', papers=[], sources=['DYNAMICS'],
      claim=r'对 $n\ge3$，实际移动筛事件在种子 $0$ 处精确编码 $n,n+2$ 都为素数。CRT 与 Abel 求和给出 $\operatorname{Var}(S_N)=O(N)$、$A_N\asymp N/\log^2N$，从而 Haar 几乎每个种子无限命中。',
      limit='底层加一映射是自治的，非自治性来自移动靶和筛尺度。零测例外集可能包含指定种子0；事件质量和度量结论不能自动跨过动力学桥。',
      related=[('K01','事件质量的局部基础'),('K14','几乎处处到指定点的缺口')]),
 dict(id='K11', title='到达孪生素数终点意味着什么', island='6', papers=[], sources=[],
      claim=r'终点是 $\pi_2(y)\to\infty$。如果证明 $\sum_{n\le y}\Lambda(n)\Lambda(n+2)\sim cy$ 且 $c>0$，去掉真素数幂的较小贡献后可以推出终点，但本档案没有证明该渐近式。',
      limit='更多有限素数对、更多论文编号、checker PASS、局部恒等式或某种模型增长结论均不能单独构成到达终点的证据。该加权素数对计数也不是K02的物理标量。',
      related=[('K01','局部计数与终点区分'),('K13','解析桥仍有未证条件'),('K14','动力学桥的充分准则')]),
 dict(id='K12', title='几何提升必须有精确算术附接', island='7', papers=[], sources=['GEOMETRY','CLOCK','INTERTWINER'],
      claim='有用的几何提升至少要给出保时关系、事件拉回、适用测度对应和指定种子对应。这些是需要证明的附接要求，不能用二维相空间的图像替代。',
      limit='没有已经构造完成的孪生素数专用 Hénon 提升。平稳混合系统不能有非平凡有限加一时钟作为保测因子的论证，不排除所有非自治几何表示；实物筛演化的强迫项也不能省略。',
      related=[('K10','原事件系统'),('K14','仍须落实指定种子')]),
 dict(id='K13', title='解析桥的两道Gate与严格损失账本', island='2', bridge='A', papers=[], sources=['V58','V59','PHYSICAL-LOCAL_EMITTER_PROOF','STATUS'],
      claim=r'图像 Bridge A 内同时包含解析 Gate A 和 Gate B。完整标量目标要求 $|\mathfrak C_x|\ll xQ^2x^{-\delta+o(1)}$ 且 $\delta>1/400$。条件性的临界数组路线给出 $\delta=1/96-\ell$，所以严格需要 $\ell<19/2400$。',
      limit=r'Gate A 仍单独未证，双侧附接和残差条件也未证。终端余量为 $0<\eta<\min\{\eta_A,\delta-1/400,419/2400\}$。这个账本不是全部上游到TPC蕴含链的新证明；V58/V59是源标签，不是新TPC编号。',
      related=[('K02','对象定义'),('K03','方法边界'),('K04','低秩边界'),('K05','条件性压缩接口'),('K06','边界代价'),('K11','终点区分')]),
 dict(id='K14', title='指定种子0的柱集回接准则', island='5', bridge='B', papers=[], sources=['SEED','DYNAMICS'],
      claim=r'充分不等式 $S_N(0)\ge A_N-\sqrt{q_N}V_N-\Omega_N$ 把缺口分为点值代价与柱内振荡。若沿无界序列，两项之和最多为 $(1-\eta)A_N$，其中固定 $\eta>0$，则可推出无穷多个孪生素数。',
      limit=r'所需的振荡联合上界未证明。这只是充分条件，不是必要条件或唯一回接方式。细柱使 $\Omega_N=0$，却可能让点值代价过大；不能只保留有利的一项。',
      related=[('K10','度量结论的边界'),('K12','几何附接要求'),('K11','条件性终点接口')]),
]

def card_path(card):
    return '04_知识卡片/'+card['id']+'-'+card['title']+'.md'

def write_content(b):
    cards={c['id']:c for c in CARDS}
    matrix={s['id']:s for s in json.loads((b.source/SUMMARY/'CORE_SOURCE_MATRIX.json').read_text())['sources']}
    reverse_mentions={row['id']:[] for row in b.rows}
    for owner, mentions in b.mentions.items():
        for number, evidence in mentions.items():
            targets=b.by_number[number]
            if len(targets)==1:
                reverse_mentions[targets[0]['id']].append(owner)
                b.edges.append(dict(source='02_论文/'+owner+'.md', target='02_论文/'+targets[0]['id']+'.md',
                                    relation='source-mention', evidence=evidence))

    for row in b.rows:
        ident=row['id']; target='02_论文/'+ident+'.md'
        aliases=[row['directory']]
        if len(b.by_number[row['number']])==1 and row['number']:
            aliases += ['TPC'+str(row['number']), 'TPC-'+str(row['number'])]
        lines=[properties(id=ident,type='paper',title=row['title'],aliases=aliases,generated=True,
              source_directory=row['directory'],conversion_status=row['conversion_status'],
              semantic_review='not-certified-by-conversion',candidate_islands=row['candidate_islands'],
              tags=['tpc/paper']), '# '+ident+' — '+row['title']+'\n',
              '> [!info] 原稿与知识库的关系\n> 此条目以原目录为唯一身份；全文、摘要、原始结论与历史错误按来源保留。转换完成不等于数学内容已经独立验证。\n']
        if row['conversion_status']=='SOURCE_UNAVAILABLE':
            lines += ['> [!warning] 原稿不可访问\n> 本目录没有可获取的论文正文。不得用同为TPC207的另一目录替代，也不生成虚构摘要或证明。\n',
                      wiki('01_导航/重复编号说明.md','查看TPC207的两个不同目录')+'\n']
        else:
            pdf=b.attachment(b.source/row['paths']['pdf'])
            tex=b.attachment(b.source/row['paths']['tex'])
            lines += ['## 阅读入口\n', '- '+wiki('03_全文/'+ident+'.md','Markdown全文')+'\n',
                      '- [原始 PDF]('+relative_link(pdf,target)+')\n',
                      '- [原始 TeX 附件]('+relative_link(tex,target)+')\n',
                      '- '+wiki('99_维护/转换记录/'+ident+'.md','转换记录与限制')+'\n']
            readme='papers/'+row['directory']+'/README.md'
            if readme in b.origins: lines += ['- '+wiki(b.origins[readme],'原README与范围说明')+'\n']
            matched=re.search(r'## Abstract\s*\n(.*?)<!-- SOURCE_BODY_BEGIN -->',row['markdown'],re.S)
            if matched:
                abstract=matched[1].strip()
                # Keep the original abstract in the full text, avoiding a
                # second unadapted copy of its links/macros in the entry card.
                lines += ['## 原文摘要\n', wiki('03_全文/'+ident+'.md','阅读全文中的完整 Abstract')+'。摘要不另行机器改写，避免削弱限定语。\n']
        lines += ['## 七岛候选定位\n','以下来自原目录文字匹配，仅用于检索，**不是人工语义分类或定理依赖**。\n']
        for island in row['candidate_islands']:
            if island not in ISLANDS: continue
            node='01_导航/'+ISLANDS[island][0]+'.md'
            lines += ['- '+wiki(node,ISLANDS[island][1])+'\n']
            evidence=next((e for e in row['lexical_evidence'] if e['island']==island),None)
            b.edges.append(dict(source=target,target=node,relation='candidate-topic',evidence=evidence))
        attached=[c for c in CARDS if row['number'] in c['papers'] and row['conversion_status']!='SOURCE_UNAVAILABLE']
        if attached:
            lines += ['## 综合稿中明确选用的关系\n']
            for card in attached:
                lines += ['- '+wiki(card_path(card),card['title'])+'（核心来源矩阵指向此原稿）\n']
                b.edges.append(dict(source=card_path(card),target=target,relation='source-selected-in-synthesis',
                                    evidence={'matrix':SUMMARY+'CORE_SOURCE_MATRIX.json','source_ids':card['sources']}))
        if b.mentions.get(ident):
            lines += ['## 原始TeX中提及的TPC文档\n','这些是原文提及或书目记录，不自动解释为“证明依赖”。\n']
            for number,evidence in sorted(b.mentions[ident].items()):
                targets=b.by_number[number]
                destination='02_论文/'+targets[0]['id']+'.md' if len(targets)==1 else '01_导航/重复编号说明.md'
                locator=b.source_location(b.source/evidence['path'],evidence['line'],ident,target)
                lines += ['- '+wiki(destination,'TPC'+str(number))+ ' · [原文定位]('+locator+')\n']
        if reverse_mentions[ident]:
            lines += ['## 哪些论文提及本条目\n', ' · '.join(wiki('02_论文/'+p+'.md',p) for p in sorted(set(reverse_mentions[ident])))+'\n']
        lines += ['## 我的研究笔记\n','请在 '+wiki('80_我的笔记/使用说明.md','手写空间')+' 新建笔记并链接本条目；自动生成文件受到覆盖保护。\n',
                  wiki('01_导航/论文总览.md','全部论文')+' · '+wiki('00_开始阅读.md','首页')+'\n']
        b.put(target,'\n'.join(lines))

    for card in CARDS:
        target=card_path(card)
        lines=[properties(id=card['id'],type='knowledge-card',generated=True,island=card['island'],
                          evidence='source-backed-synthesis',bridge=card.get('bridge',''),tags=['tpc/knowledge']),
               '# '+card['title']+'\n','> [!info] 本次补充的知识卡片\n> 根据已有综合稿和原始来源整理；不是新增定理或新的TPC编号。\n',
               '## 对象与结论\n',card['claim']+'\n','## 必须保留的边界\n',card['limit']+'\n',
               '## 有类型的关联\n']
        for other,relation in card['related']:
            lines += ['- '+wiki(card_path(cards[other]),cards[other]['title'])+' — '+relation+'\n']
            b.edges.append(dict(source=target,target=card_path(cards[other]),relation=relation,
                                evidence={'synthesis':SUMMARY+'paper/main.tex','card_source_ids':card['sources']}))
        lines += ['## 来源\n','- '+wiki('05_综合与进展/七岛综合稿-中文.md','完整中文综合稿')+'\n']
        for sid in card['sources']:
            item=matrix[sid]; path=b.source/item['path']
            text=item['path']
            if item['path'] in b.origins: text=wiki(b.origins[item['path']],sid)
            lines += ['- '+text+'：'+item['claim_ceiling']+'。\n']
            for start,end in item['line_ranges']:
                loc=b.source_location(path,start,card['id'],target)
                lines += ['  - [源定位 '+str(start)+'–'+str(end)+']('+loc+')；SHA-256 `'+item['sha256']+'`。\n']
        if card['id']=='K11':
            loc=b.source_location(b.source/SUMMARY/'paper/sections/arithmetic.tex',2,card['id'],target)
            lines += ['- [综合稿算术终点段落]('+loc+')\n']
        for num in card['papers']:
            rows=[r for r in b.by_number[num] if r['conversion_status']!='SOURCE_UNAVAILABLE']
            if len(rows)==1:lines += ['- '+wiki('02_论文/'+rows[0]['id']+'.md','原论文TPC'+str(num))+'\n']
        lines += ['\n'+wiki('01_导航/'+ISLANDS[card['island']][0]+'.md','所属岛屿')+' · '+wiki('00_开始阅读.md','首页')+'\n']
        b.put(target,'\n'.join(lines))

    for island,(filename,title) in ISLANDS.items():
        lines=[properties(type='island-index',island=island,generated=True,tags=['tpc/map']),
               '# '+title+'\n','岛号是研究对象的坐标，不是完成勾选。\n','## 已整理的知识卡片\n']
        for card in CARDS:
            if card['island']==island:lines += ['- '+wiki(card_path(card),card['title'])+'\n']
        lines += ['## 论文候选索引\n','本节仅按来源清单中的字面关键词匹配归类；不据此宣称实际依赖或证明完成。\n']
        for row in b.rows:
            if island in row['candidate_islands']:
                lines += ['- '+wiki('02_论文/'+row['id']+'.md',row['id']+' — '+row['title'])+'\n']
        lines += ['\n'+wiki('01_导航/七岛总览.md','七岛总览')+' · '+wiki('01_导航/两桥与未解决问题.md','两桥与未解决问题')+'\n']
        b.put('01_导航/'+filename+'.md','\n'.join(lines))

    overview=['# 全部论文目录\n','420个目录身份包括编号TPC1–418、一个额外的TPC207缺源目录，以及MVP1原型；不是420项独立数学贡献。\n',
              '| 入口 | 原目录题目 | 阅读状态 |\n|---|---|---|']
    for row in b.rows:
        overview.append('| ['+row['id']+']('+relative_link('02_论文/'+row['id']+'.md','01_导航/论文总览.md')+') | '+row['title'].replace('|','/')+' | '+
                        ('缺源，保留说明' if row['conversion_status']=='SOURCE_UNAVAILABLE' else '全文机械阅读层')+' |')
    overview += ['\n'+wiki('01_导航/转换状态与核查.md','转换状态与核查')+' · '+wiki('00_开始阅读.md','首页')]
    b.put('01_导航/论文总览.md','\n'.join(overview)+'\n')
    b.put('01_导航/重复编号说明.md','# TPC207的两个不同目录\n\n'+
          '\n'.join('- '+wiki('02_论文/'+r['id']+'.md',r['directory'])+'：'+r['conversion_status'] for r in b.by_number[207])+
          '\n\n原文只写TPC207而没有足够上下文时，链接到本消歧页，不猜测作者指的是哪个目录。\n')
    b.put('01_导航/知识卡片索引.md','# 知识卡片索引\n\n这些是本次整理新增的解释层，完整原文仍是证据。\n\n'+
          '\n'.join('- '+wiki(card_path(c),c['id']+' — '+c['title']) for c in CARDS)+'\n')
    cn_map=b.attachment(b.source/'research/tpc-big-road/figures/tpc_route_cn.png')
    en_map=b.attachment(b.source/SUMMARY/'paper-en/figures/tpc_route_en.png')
    b.put('01_导航/七岛总览.md','# 七岛总览\n\n'+
          '![]('+relative_link(cn_map,'01_导航/七岛总览.md')+')\n\n'+
          '[英文原图]('+relative_link(en_map,'01_导航/七岛总览.md')+')。两张图均原样保存；图像不认证任何桥已经跨越。\n\n'+
          '\n'.join('- '+wiki('01_导航/'+filename+'.md',title) for filename,title in ISLANDS.values())+
          '\n\n'+wiki('05_综合与进展/七岛地图说明-原文.md','原始地图说明')+' · '+wiki('01_导航/两桥与未解决问题.md','两桥与未解决问题')+'\n')
    b.put('01_导航/两桥与未解决问题.md',r'''# 两桥与未解决问题

这是生成时状态的导航摘要，不是研究启动指令。

## 图像Bridge A：解析集体节省

解析 Gate A 与 Gate B **都位于这座桥内部**。目标是完整实际标量的有符号节省，严格要求 $\delta>1/400$；普通范数、行归一化和低秩修补障碍没有支付这项估计。

'''+'- '+wiki(card_path(cards['K13']),'两道Gate与严格损失账本')+'\n- '+wiki(card_path(cards['K06']),'已经支付的边界项与内部缺口')+r'''

## 图像Bridge B：指定算术种子

实际移动筛事件已有Haar几乎处处命中，但指定种子0还没有回接。几何表示也不能省略这一要求。

'''+'- '+wiki(card_path(cards['K14']),'柱集回接的充分准则')+'\n- '+wiki(card_path(cards['K10']),'度量命中定理及其量词边界')+
          '\n\n来源：'+wiki('05_综合与进展/当前状态-2026-09-12.md','当前状态摘要')+' 与 '+wiki('05_综合与进展/交接文档-完整快照.md','完整交接快照')+'。\n')
    b.put('05_综合与进展/当前状态-2026-09-12.md',r'''# 当前状态快照 — 2026-09-12

根据生成时读取的TPC_HANDOFF头部整理。知识库不会自动把历史状态更新为今天的事实；以后应先核对源仓库的交接变化。

- 正式编号终点：TPC418；后续有2026-09-09未编号研究。
- 当前地图位置：岛②，面向图像Bridge A内部的解析Gate B；Gate A另行开放。
- 已有实际算子精确分解、行能量与系数范数结果、增长秩障碍、完整发射恒等式，以及集体边界 $11/64$ 节省。
- 全部实际标量的系数敏感固定幂次节省仍未证明，不能把边界结果当成全标量结论。
- 动力学实际移动靶的度量命中结论不包含指定种子0；图像Bridge B仍未跨越。
- 这些整理没有证明孪生素数猜想，也没有创建新研究授权。

'''+wiki('05_综合与进展/交接文档-完整快照.md','完整交接快照')+' · '+wiki('05_综合与进展/实际算子研究汇总-2026-09-09.md','未编号实际算子研究总结')+' · '+wiki('01_导航/两桥与未解决问题.md','两桥账本')+'\n')
    b.put('05_综合与进展/历史总结校注.md',r'''# 历史总结校注：保留原文，区分时效

这是知识库新增的导航校注，不覆盖任何原总结。

1. 历史总结中“最强当前结果是有限且合成”的措辞，限于其讨论的TPC418编号发布终点。后续未编号研究已经有实际物理算子、增长秩和边界结论；但全标量固定幂次信用仍为零。
2. 历史路线顶端的TPC418和嵌入旧图中的TPC353来自不同时间。不能把每一个YOU ARE HERE都当成今天的状态。
3. 历史DONE_L0标签不能改写为“岛④完成”。形式守恒、给定提升、实际活跃支撑覆盖和带权代价必须区分。
4. 旧有限附接报告中的物理源定义缺口是历史状态；现已恢复实际hybrid与profile。原报告的核方向错误与后来的勘误应一起阅读，而不是静默改写原报告。
5. 历史RH/TPC混合范围及823项统计按原日期保留。本知识库只覆盖当前420个TPC目录，不把RH材料混入。
6. 旧仓库绝对链接仅在独立TPC仓库中存在同相对路径且属于允许范围时重定位；原链接及对应关系保存在维护账本中。缺失链接进入例外清单，不能自动补造材料。

'''+wiki('05_综合与进展/研究历史总结-原文.md','研究历史总结原文')+' · '+wiki('05_综合与进展/历史路线图-原文.md','历史路线图原文')+' · '+wiki('05_综合与进展/当前状态-2026-09-12.md','当前状态快照')+'\n')
    b.put('01_导航/转换状态与核查.md','# 转换状态与核查\n\n'+
          '- 原有完整机械MD：279份。\n- 本次从可获取TeX补转：140份。\n- 合计可获取全文：419份。\n- 独立缺源目录：1个。\n\n'+
          '原始转换与Obsidian适配分别核对数学节点序列；原PDF未重编译，也不声称源TeX与PDF已逐页一致。机械全文不是独立数学验证。\n\n'+
          wiki('99_维护/使用与更新说明.md','使用与更新')+' · '+wiki('99_维护/待解决来源链接.md','原始来源链接例外')+' · '+wiki('99_维护/验收报告.md','实际检查结果')+'\n')
    b.put('00_开始阅读.md',r'''# 孪生素数研究知识库

这是一个独立的Obsidian阅读与研究导航层：419份可获取全文、1个缺源目录说明，以及既有总结和可追溯的知识卡片。原论文和原仓库未被修改。

## 第一次打开

在Obsidian中选择“打开文件夹作为仓库”，选中整个`tpc_obsidian_vault`目录。无需社区插件或云端服务。原稿以原语言保存，中文导航和知识卡片用于串联；没有把400多篇重新翻译成同一种语言。

## 建议的阅读顺序

'''+ '\n'.join([
        '1. '+wiki('01_导航/七岛总览.md','先看七岛地图与两桥的含义'),
        '2. '+wiki('05_综合与进展/七岛综合稿-中文.md','读完整中文综合稿')+'，或 '+wiki('05_综合与进展/七岛综合稿-English.md','English synthesis'),
        '3. '+wiki('05_综合与进展/当前状态-2026-09-12.md','核对当前状态和未解决问题'),
        '4. '+wiki('01_导航/知识卡片索引.md','按问题进入14张知识卡片'),
        '5. '+wiki('01_导航/论文总览.md','从420个目录入口查阅全文和原PDF'),
        '6. '+wiki('80_我的笔记/使用说明.md','在手写空间记录自己的想法'),
    ])+r'''

## 关系图怎么读

论文入口中的“原文提及”、综合稿明确选用、知识卡片解释和七岛候选关联是不同关系。反向链接表示某处引用或链接了本笔记，不表示数学依赖已经成立。建议从具体问题的局部关系图开始，避免把全库的密集连线理解成已闭合的证明链。

## 维护与来源

'''+wiki('99_维护/使用与更新说明.md','使用和安全更新说明')+' · '+wiki('01_导航/转换状态与核查.md','转换状态')+' · '+wiki('99_维护/验收报告.md','验收结果')+' · '+wiki('05_综合与进展/历史总结校注.md','历史总结校注')+r'''

这不是孪生素数猜想的证明。原有定理、条件性接口、模型结果、有限检查及历史错误均按各自来源和范围阅读。
''')
    b.put('99_维护/使用与更新说明.md',r'''# 使用与更新说明

## 使用

1. 将整个知识库目录复制到自己的电脑，在Obsidian中打开该文件夹；先读首页。
2. 默认功能已足够：搜索、内部链接、反向链接、属性、局部关系图和数学公式。不依赖社区插件。
3. 新笔记放入`80_我的笔记/`。可以在Obsidian的文件与链接设置中将它设为默认新笔记位置。
4. `03_全文/`保存适配后的全文；`90_附件/`保留选用原PDF、TeX、书目、地图和原始材料副本。原始Markdown或代码附件用`.txt`后缀保存以免成为重复的图节点；需要时用外部编辑器打开。原始字节散列不变。
5. 原PDF中的印刷公式、定理编号仍是权威编号。`ref-…`标题仅用于源码标签跳转，不是新定理编号。
6. `99_维护/参考文献/`保存原文引用键与原书目，未匹配键会明确标示。它们不是本次重新联网核验的出版信息。
7. 历史原稿和交接快照中的命令、计划、授权措辞仅是归档内容，不自动成为新的研究或工具执行指令。

## 安全更新

构建脚本位于`_tools/`。源仓库默认在知识库旁边的`twin_primes/`；阅读知识库不需要源仓库，但重新生成需要它。

```sh
python -B _tools/prepare_sources.py --source ../twin_primes
python -B _tools/build_vault.py --source ../twin_primes
python -B _tools/preserve_reading_sources.py --source ../twin_primes
python -B _tools/validate_vault.py
```

生成器核对原源散列，拒绝默默接受已变化的源基线。若源仓库有新内容，应先审查变化、保存当前知识库快照，再建立新的输入基线；不要为消除错误而直接篡改散列。生成文件被手工改动时，生成器拒绝覆盖；不会删除或清理过期文件，也不自动提交、推送或开启同步。

`80_我的笔记/`、`_tools/`、`.build/`和已有`.obsidian`设置不属于正文生成器的覆盖目标。手写空间由你维护，自动转换只能写声明的生成区。

## 转换边界

419份原稿均有机械全文。新补转包含有界的verbatim代码块保留、无注释数学AST内换行规范化、有原文依据的星号分组，以及规范多目标引用中的TeX注释处理。剩余空数学节点会阻止转换，不能假定它们在原文中也是空的。不执行TeX、不重跑实验、不修正原有科学结论。完整数学节点检查仍不等于转换器已经理解并验证每一个证明。

原始源码、源目录和Git基线哈希由维护清单保留。关键词岛屿标签是候选导航；原文提及不等于依赖。14张知识卡片是有来源的解释层，不是400多篇的逐篇语义认证。

## 官方使用参考

- [打开文件夹作为Obsidian知识库](https://help.obsidian.md/Files+and+folders/Manage+vaults)
- [内部链接、标题链接与反向导航](https://help.obsidian.md/links)
- [笔记属性](https://help.obsidian.md/properties)
- [数学公式与高级格式](https://help.obsidian.md/advanced-syntax)

本次不安装社区插件、不启用云同步、不上传内容；若没有桌面Obsidian实测，验收报告会明确说明。
''')
    b.put('99_维护/验收报告.md','# 知识库验收报告\n\n构建已产生阅读层；完整的链接、来源和公式显示检查尚待验证器运行。此处不是数学证明认证。\n\n'+
          '请运行 `_tools/validate_vault.py --report` 生成实际验收结果。\n')
