# DRAFT — Original Venture OS Request / 原始需求简报

> **Status: DISCUSSION DRAFT — NOT APPROVED AS SPECIFICATION**
>
> **Origin:** User's initial request and subsequent refinements, summarized for independent review by other agents.
>
> **Purpose:** Preserve the original problem, motivations, constraints and desired outcomes **before** architecture decisions. This is a stakeholder brief, not a finalized PRD, verified market research, approved budget or instruction to start spending money.
>
> **Review first:** An agent asked to review the project should begin here, then compare proposals against this brief. Challenge assumptions freely; do not silently rewrite this original request. Put proposals in separate issues/PRs/decision records.

## 1. 原始目标 / North Star

建立一套真正适用于 **solo developer + solo entrepreneur** 的、可持续重复使用的 **low-key MBA + product discovery + validation + development + operation** 创业系统。

目标 **不是** 一开始追求最大收入或堆砌大量产品，而是以最小可控成本找到 **最有真实付费可能性、最能持续变现** 的问题与产品模式，并用数据决定「继续、改变、暂停、放弃」。

全套知识、商业决策、工作清单和实验过程优先保存在 **GitHub repository**，让人和各种 AI Agent 均能读取、执行、复盘、交接。

## 2. 商业策略与边界 / Business thesis

- **探索组合，不是产品组合：** 同时研究或轻验证 **3–5 个候选方向**，不要求同时把 3–5 个完整 App 开发上线；避免只赌一个，也不要同时管理十几个完整产品。
- **先证据，后工程：** 最早验证用户痛点、渠道触达能力和真实付费意愿，再决定是否写 PRD、投入代码、建完整 SaaS。
- **目标变现：** 优先考虑 **subscription / recurring revenue**；**不以广告收入作为产品变现模式**。但允许用广告作为获客、测试需求的实验工具。不能为了订阅而强迫明显一次性使用场景采用订阅；模式应匹配持续价值。
- **地域：** 优先考虑可在 **马来西亚** 验证和销售的场景，包括借鉴中国或海外已经验证的产品形态，再针对本地语言、支付、价位、习惯、行业痛点进行适配；不局限马来西亚，不能因为本地化就推断存在蓝海。
- **产品方向候选池：** (A) 红海工具 + 情绪/体验差异化；(B) 极窄垂直工具 + 简明收费；(C) AI 作为具体服务的替代，不是通用聊天壳；(D) 马来西亚垂直行业、本地流程或语言供给缺口；包括 Photo/Video / Utilities / Productivity / Education / 专业 B2B 方向。这些都是 **要验证的假设**，不是已经确定的 Roadmap。
- **商业目标阶段化：** 最早寻找第一笔真实付款或可核实的付费承诺，随后验证自然回访、留存、单位经济与服务成本，再争取持续 MRR。不能用下载、广告点击或用户说「有趣」冒充付费验证。
- **集中资源：** 某方向出现可重复的获客、付费和留存迹象后，绝大部分产品时间转向该方向；其他实验降到低维护或结束。具体投入百分比是待决定政策而非科学常数。

## 3. 用户最早请求的 End-to-End Workflow

建立一个从零到运营的、可以由 Agent 或人直接照做的系统：

1. **Idea sourcing:** 如何主动找 idea？查什么公开资料、竞品、差评、社群、行业、搜索意图、当地未满足需求？如何记录来源、日期、初筛判断和下一步？
2. **Opportunity evaluation:** 谁会在什么时刻遇到何种痛点，现有替代方法是什么，为什么愿意付钱，我们能否触达？商业模型、价格、分发入口、竞争和技术/合规风险是什么？
3. **Proof-driven validation:** 最便宜的验证方式是什么——访谈、现有用户访谈、manual concierge、mock demo、landing page、waitlist、预售或小预算广告？如何留存 **proof**，定义成功/失败/不确定，避免假阳性？
4. **Marketing / advertising playbook:** 从零学习如何制作/投放广告；哪个渠道适合什么类别；怎样做 Hook/Angle/Format、广告变体、广告账户管理、归因、转化漏斗和 A/B 实验；怎么判断素材真的有效；怎么控制投放成本；把每次实验形成可复用的 **advertising knowledge base**。
5. **Business planning:** 有轻量 **Lean Business Plan**、可操作的 Next Steps / Action Items、商业目标、定价、成本预算、CAC / CPS / retention / LTV 假设与风险，而非形式化报告。
6. **PRD / software planning:** 只有确实需要时才写 PRD；明确 MVP 范围、非目标、用户流程、验收条件、数据和隐私要求。
7. **AI-assisted development loop:** GitHub issue → 选取上下文 → coding agent 开发 → 测试 → PR → Review → deploy → 观察 → 修复或下一实验；支持自动化，但必须可审计、可回滚。
8. **Launch and experiments with real users:** 本地优先、尽量少 hosting；当需要外部用户和收钱，采用 **可靠、便于维护、安全** 的 hosting 与支付模式，区分实验/试点/生产要求。
9. **Maintenance and customer support:** 日常维护、错误监控、退款/取消、客户支持、依赖和安全更新、运行成本、备份恢复、投诉和留存分析。
10. **Scale / iterate / kill:** 对每个项目保存得失结论，发现明显正向信号就集中时间；没有信号就停止，而非不断增加 Feature。

每个阶段都应说明 **Input → Tasks → Expected Artifact → Evidence → Exit Gate → Next Action**，避免留下只有概念而没有执行步骤的流程图。

## 4. GitHub 要扮演什么角色？

GitHub 是 **Source of Truth / Knowledge Management / Work Management / Delivery Evidence** 的统一入口。

希望有：
- 统一入口、清晰索引、Progressive Disclosure，使 Agent 不必扫描无关文件，也不靠聊天历史了解当前状态；
- **Business Plan、PRD、Market Research、Ad Knowledge、Experiment Results、Decision Records、Operations Handbook**；
- 清晰的 **what to do next**：Issue / Projects、Task Owner、可执行任务、依赖、完成定义和审批；
- 可追踪的 evidence：来源、观察日期、样本范围、成本、广告表现、已核实/未核实的用户和付费信号；不给公共仓库存原始 PII 或 secrets；
- 可复用 templates、skills、SOP、自动化工作流和定期复盘；
- 多 Agent 并行时，不重复研究、不争写同一份文件、不依赖单个模型的 Memory 作为权威信息。

应尽可能使用 GitHub-native 能力：Issues、PRs、Projects、Actions、branch/worktree、Markdown；复杂度不足以证明价值前，不引入第二套任务数据库。

## 5. 两套 Agent 执行入口，业务核心必须统一（后续需求补充）

**Flow A — Agent Ecosystem / Autonomous Assistants**
- 希望兼容 Dots、Muse、Grok Bot、OpenClaw 一类有持续任务、定时研究、跨应用、远程执行能力的 Agent；
- 负责机会监测、市场调查、广告研究/建议、实验进度追踪、生成下一批待办、必要时委派开发；
- 由于各服务 GitHub API、可写权限、调度能力不一样，要提供适配层，不臆测所有 Provider 具备同一能力。

**Flow B — Local/Cloud Coding Agents**
- 同时兼容本地 CLI/IDE Agent 和云端 Coding Agent（例如 Codex、Claude Code、Cursor 等）；
- 从 Issue + scoped documentation 开始，读必要上下文、实现 PRD、测试、PR、代码审查与交接；
- 可以做研究；Flow A 也可以被授权做开发。流程区分是 **默认执行入口**，并非能力锁定。

**Non-negotiable:** 两条 Flow 共享 **同一份策略、知识、证据、任务契约、产物标准和决定**。若 Agent 平台的操作方式冲突，就保留 **两个独立 execution flow / adapter**，但 **不要复制或分叉一套 Business Knowledge**。

## 6. 成本与工程安全 / Cost constraints

- **实验期现金支出越低越好；**优先研究、手工服务、local prototype 或静态 demo。
- 如果需要 Hosting 才能测试用户或真实付款，允许使用可靠的小规模 managed hosting，避免前期昂贵且复杂的 infrastructure。
- 长期可维护、**稳定性和安全性仍是第一层硬约束**，不能为了便宜而暴露客户数据、支付事件、Secrets 或忽略基础备份和监控。
- 不要过早上 Kubernetes、microservices、自建长驻 orchestration 或昂贵数据平台；按真实业务风险扩展。
- 广告花费、购买服务、生产部署、对外发送消息、权限变更及不可逆操作必须有明确人工批准；Agent 可提出计划和建议但不可自行动用资金。

## 7. 广告实验策略：原始研究里的主张，需要独立验证

用户提供了多组市场 benchmark / 创业案例，目的是作为启发和待复核输入，包括：
- 不同新订阅应用达到 MRR 的比例，以及不同品类的突破率；
- 强制付费墙 vs freemium 的转化率对比；
- 订阅 LTV、周付费、PPP 定价、马来西亚消费者价格敏感性；
- ASA / Apple Ads、TikTok/Meta 的预算、CPI/CPC、素材测试建议；
- 特定独立开发案例的付费增长与 MRR；
- 本地化工具和本地垂直 SaaS 的机会。

**重要：这里所有具体数字都来自用户先前提供的研究文字，当前未逐项复核出处、发表时间、分母与适用市场。不能视为已验证事实。** 例如：
- 「50 conversions 就达到统计显著」不是通用规则，须按实验设计/功效分析；
- 「硬付费墙一定优于 freemium」不能脱离样本选择、品类与留存；
- 「RM15–30/月」只是候选测试区间，不是确定的最佳本地定价；
- 「$300–600 首月投放」是待审批假设，**不是当前预算**；
- 「ASA 首轮优于 Meta」取决于已上架的 iOS App、搜索意图、渠道政策和目标用户；无上架 App 不能直接使用这条路径；
- 「本地开发者少就意味着市场存在供给真空」逻辑不成立，需查实际支付、竞品差异与触达能力。

**Reviewer 必须标出哪些数据可以查证、哪些叙述样本偏差很大、哪些仍能指导低成本实验。**

## 8. 期望成果 / Deliverables

长期的目标不是一次生成几十份空文件，而是有：
1. 一个易浏览的 **GitHub Venture OS Starter** 和当前工作导航；
2. 可执行的 **Eight-Stage SOP**，各阶段输入、工作和检查门槛明确；
3. **Idea research + evidence + experiment** 资料体系，能有效重复使用；
4. **Low-key MBA / business playbooks**（定价、财务、风险、获客、营销等）；
5. **Ad research / test / analysis knowledge base**，能从预算、素材和归因真正学到东西；
6. **Business Plan + PRD + GitHub Issue + Coding Agent loop**；
7. **Hosting/security/monitoring/maintenance/support** 的最低有效框架；
8. **Two adapter flows** + single business knowledge source；
9. 从实验结果推动 **Scale / Iterate / Pause / Kill** 的决策结构；
10. 可从 GitHub issue 直接判断「现在应该做什么」并执行。

要求初始版 **够轻量，不为了系统完整而产生大量无维护价值的目录、文件或服务**。

## 9. 尚未决定 / Open design questions

- 哪些阶段值得通过 GitHub Actions 自动化，哪些通过外部 Agent Scheduler？如何防止重复、失控或偷偷消费 API Token？
- 3–5 个候选如何设定统一但不过度死板的保留/终止标准？
- 严格 subscription-first 是否合适？哪些「一次性服务」应该允许非订阅定价？
- 公开中央 Repo 与未来私有项目、实验原始数据、安全凭证如何隔离？
- 建立证据归因时，是否使用直接访问事件表，还是匿名汇总 + 外部可访问的审计资料？
- 多 Agent 都可研究和开发时，如何控制 Owner、Review、权限、Budget 和 Handoff？
- 哪些能力立即实施，哪些仅保持为模板，直到真正有付费实验再启动？
- GitHub Projects 值不值得从首版启用？还是先用 Issue 就够？

## 10. 给其他 Agent 的独立 Review 要求

在开始改写结构前，请先回答：
1. 是否准确覆盖原始商业诉求？遗漏了哪些工作流，过度设计了哪些部分？
2. 哪里存在 **unverified claims、unrealistic funnel metrics、错误归因、过度乐观的产品/市场假设**？
3. 为什么需要双 Flow？有没有更简单的 **shared core / provider adapter** 方式？
4. 这个 Repo 的导航、Skills、任务状态、PRD、Evidence 和安全边界是否足以给陌生 Agent 自主接手？
5. 最小 2 周可验证版本应该包含什么？哪些目录/自动化可以删除？
6. 如果下一步只能执行三个任务，哪个最能产生 **真实买家或付费证据**？

建议产出：**Gap Analysis / Challenges / Simplification Proposal / Revised Structure / Suggested First Experiment**。

---
_This file intentionally records the original intention. It is informal and subject to review. Later approved requirements should live in canonical strategy/playbooks/contracts without overwriting the historical brief._
