# 请人审稿：邮件模板

下面的英文模板由你本人填写、发送。我没有联系过任何人。

**发送前要做的事：**
- 把 `<...>` 换成实际内容。
- 两个链接换成固定提交的永久链接：在 GitHub 页面按 `y` 键即可得到。这样对方读到的版本不会随后续推送改变。
- 篇幅控制在一屏以内，细节都在审稿指南里。

**找谁：**
- 做筛法、素数间隙或 Jacobsthal 函数的数论学者。定理 D–F 只用标准筛法定理，所以熟悉 Halberstam–Richert 或 Friedlander–Iwaniec 那套工具的人就能审。
- 先请一位看定理 D（约两页）。定理 D 过关后，E、F 是同一个框架，审起来快。

---

**Subject:** Request: checking a sieve argument on gaps between totatives of primorials (Erdős #854)

Dear Professor <name>,

I am writing to ask whether you would be willing to check a short sieve-theoretic argument, or to suggest someone who might.

The question is Erdős Problem #854: which even numbers occur as gaps between consecutive integers coprime to the primorial $P_k$. Let $s(k)$ be the smallest even number that does not occur, and $J(k)$ the Jacobsthal function. The main claims are:

- (Theorem D) $s(k)\ge(1-\varepsilon)\min\bigl(J(\lceil(1-\eta)k\rceil),\,p_k^{1+\delta_0}\bigr)$ for all large $k$;
- (Theorem E) the number of distinct even gaps is $\gg_\varepsilon\min\bigl(J(\lceil(1-\eta)k\rceil),\,p_k^{2-\varepsilon}\bigr)$;
- (Theorem F) both hold with lag $k^{1-\kappa}$, hence with $J(k)$ itself outside a set of $k$ of density zero.

The proofs, about five pages, use only the fundamental lemma, the Jurkat–Richert linear sieve and a Brun-type upper bound, all for arbitrary residue classes. The second question of #854 is not solved; it is reduced to the regularity of $J$.

The work was done with substantial AI assistance (Claude, Anthropic), and has not been refereed. A short guide lists the steps that most need checking, each as a yes/no question:

- Write-up: <permalink to note854.md>
- Referee guide: <permalink to REVIEW_GUIDE.md>

Even a check of Theorem D alone (§6.1, about two pages) would help a great deal. I would of course acknowledge your help in any version that is posted or submitted.

With thanks and best regards,
<your name>
<affiliation, if any>
