# Paper Decomposition

Use this guide before designing slides. The goal is to turn a paper into a presentation argument, not to summarize paragraph by paragraph.

## Structure-First Principle

Default to the paper's actual structure. Common economics paper sections include:

`Introduction -> Literature Review -> Theory/Model -> Mechanism/Hypotheses -> Data/Empirical Design -> Main Results -> Robustness -> Heterogeneity -> Further Analysis -> Conclusion`

Reorder only when presentation clarity requires it. For example, split a difficult theoretical model across several slides, or turn a robustness check into a question-led page.

## Extraction Checklist

Extract these facts in order:

1. **Identity**
   - Paper title, field, contest/defense setting, author/team, target audience.
   - One-sentence research question.
2. **Motivation**
   - Policy background, real-world contradiction, why the topic matters now.
   - Any striking fact, policy timeline, or puzzle that can become slide 2.
3. **Literature and Gap**
   - 2-4 literature streams.
   - What existing studies miss: method, context, mechanism, data, or policy object.
4. **Contribution**
   - Theoretical contribution.
   - Empirical/method contribution.
   - Policy/application contribution.
5. **Theory and Hypotheses**
   - Core causal chain.
   - Hypothesis labels and directions.
   - Mechanisms and boundary conditions.
6. **Empirical Design**
   - Identification strategy: DID, PSM-DID, event study, IV, threshold, mediation, etc.
   - Treatment/control definition.
   - Sample period, sample size, data sources.
   - Core model equation and fixed effects.
7. **Variables**
   - Explained variable, core explanatory variable, mediators, moderators, controls.
   - Units and measurement definitions.
8. **Evidence**
   - Baseline regression.
   - Robustness tests.
   - Parallel trend or dynamic effects.
   - Mechanism tests.
   - Heterogeneity tests.
   - Any original figures/tables that must be shown.
9. **Conclusion**
   - 2-4 main findings.
   - Policy recommendations.
   - Limitations or future research only if needed.

## Long Text Indexes

For 40-page-plus papers, build these indexes before planning slides:

- **Section map:** paper section -> key claims -> expected PPT pages.
- **Formula/model map:** equation/proposition -> symbols -> intuition -> slide treatment.
- **Figure/table map:** figure/table number -> evidence role -> whether to quote, crop, redraw, or split.
- **Literature map:** cited study -> method/data/context/finding -> relevance.
- **Test map:** empirical test -> doubt addressed -> result -> interpretation.

## Claim Spine Rules

Each slide should have:

- **Claim:** a complete sentence, not just a noun title.
- **Proof object:** table, equation, plot, mechanism diagram, policy timeline, or short evidence card.
- **Takeaway:** a highlighted phrase, number, coefficient, or implication.

Bad slide title: `基准回归`.

Good slide title: `绿色金融试验区显著降低城市碳排放强度`.

## Question-Led Evidence Pages

When a robustness check, identification test, model choice, or further analysis is clearly answering a doubt, use the question as the slide title.

Examples:

- `为什么不能直接使用 OLS？`
- `平行趋势假设是否成立？`
- `换一组被解释变量后结论还稳吗？`
- `样本选择会不会影响估计结果？`
- `机制变量真的解释了政策效应吗？`

Each question-led page should include:

- The doubt or challenge.
- The method used by the paper.
- The original figure/table/model evidence.
- A short interpretation of what the evidence proves.

## Handling Missing Details

- If a source table is missing, create a clearly labeled placeholder: `此处放表 X：基准回归结果`.
- If a coefficient is unavailable, do not fabricate one. Write `待填：核心系数`.
- If the paper is too dense, split content across slides rather than shrinking text.

## Evidence Mapping

Before building, create a slide inventory:

`page -> paper section -> claim -> proof object -> source location -> page type -> active style component`

This inventory is the control document for the deck. Update it if page count changes.
