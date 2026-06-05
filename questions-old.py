"""
AI Maturity Assessment — Question Bank
7 Dimensions, multiple questions each, scored on 1–5 maturity scale.
Score 5 = Leading, 4 = Scaling, 3 = Defined, 2 = Emerging, 1 = Unaware
"""

MATURITY_LEVELS = {
    5: {"label": "Leading",  "color": "#00C896", "desc": "Leaders that have industrialised AI, embedding it across strategy, operations, and governance for measurable impact."},
    4: {"label": "Scaling",  "color": "#4CAF50", "desc": "Companies that have built strong AI foundations and are selectively scaling enterprise use cases."},
    3: {"label": "Defined",  "color": "#FFC107", "desc": "Organisations that have deployed pilots, with selected initiatives beginning to scale and show measurable results."},
    2: {"label": "Emerging", "color": "#FF9800", "desc": "Organisations are testing and learning through pilots or proofs of concept, often within isolated teams."},
    1: {"label": "Unaware",  "color": "#F44336", "desc": "Organisations that have minimal or no formal AI activity, with efforts limited to basic awareness or isolated experimentation."},
}

# Each question has 5 options; option index 0 = score 5 (best), index 4 = score 1 (lowest)
DIMENSIONS = [
    {
        "id": "strategy",
        "label": "Strategy and\nOperating Model",
        "label_short": "Strategy &\nOp. Model",
        "color": "#1565C0",
        "questions": [
            {
                "id": "S1",
                "sub_dimension": "STRATEGY AND OPERATING MODEL",
                "title": "Enterprise AI Vision and Roadmap",
                "question": "How clearly is your AI ambition aligned to enterprise strategy?",
                "options": [
                    {"score": 5, "text": "AI is a CEO/board priority; roadmap informs portfolio choices and scorecards."},
                    {"score": 4, "text": "AI is embedded in 3yr plans with a published roadmap and milestones."},
                    {"score": 3, "text": "There's a core AI strategy; alignment exists in pockets, not yet consistent."},
                    {"score": 2, "text": "Some teams mention AI in plans, but no shared enterprise North Star."},
                    {"score": 1, "text": "Not Aware Or We're exploring AI but don't have a defined AI vision or roadmap."},
                ],
            },
            {
                "id": "S2",
                "sub_dimension": "STRATEGY AND OPERATING MODEL",
                "title": "AI Governance & Operating Model",
                "question": "How mature is your AI governance structure and operating model?",
                "options": [
                    {"score": 5, "text": "Federated AI CoE with clear ownership, policies, and cross-functional accountability."},
                    {"score": 4, "text": "Central AI team exists with defined roles; governance evolving enterprise-wide."},
                    {"score": 3, "text": "AI governance exists but inconsistently applied across business units."},
                    {"score": 2, "text": "Informal governance; decisions made ad hoc without clear ownership."},
                    {"score": 1, "text": "No formal AI governance or operating model in place."},
                ],
            },
            {
                "id": "S3",
                "sub_dimension": "STRATEGY AND OPERATING MODEL",
                "title": "Investment & Business Case",
                "question": "How effectively does your organisation prioritise and fund AI investments?",
                "options": [
                    {"score": 5, "text": "AI funding tied to value metrics; portfolio-managed with ROI tracking at board level."},
                    {"score": 4, "text": "Structured business cases reviewed centrally; investment aligned to strategy."},
                    {"score": 3, "text": "Business cases exist but ROI measurement is inconsistent across projects."},
                    {"score": 2, "text": "Funding decisions made opportunistically; limited financial tracking."},
                    {"score": 1, "text": "No dedicated AI investment or business case process in place."},
                ],
            },
        ],
    },
    {
        "id": "value",
        "label": "Value\nRealisation",
        "label_short": "Value\nRealisation",
        "color": "#1565C0",
        "questions": [
            {
                "id": "V1",
                "sub_dimension": "VALUE REALISATION",
                "title": "Value Tracking",
                "question": "How effectively does your organisation track and realise value from AI initiatives?",
                "options": [
                    {"score": 5, "text": "AI value is systematically tracked; financial and non-financial metrics reported to leadership with feedback loops."},
                    {"score": 4, "text": "Most AI projects have defined KPIs; value reviewed quarterly with stakeholders."},
                    {"score": 3, "text": "Some projects track ROI, but measurement is inconsistent across the portfolio."},
                    {"score": 2, "text": "AI teams often perform one-time discharge for each project or initiative."},
                    {"score": 1, "text": "Not Aware Or AI-ready datasets rarely exist, large cleanup efforts required before any use."},
                ],
            },
            {
                "id": "V2",
                "sub_dimension": "VALUE REALISATION",
                "title": "Use Case Prioritisation",
                "question": "How systematically does your organisation identify and prioritise AI use cases?",
                "options": [
                    {"score": 5, "text": "Enterprise-wide use case factory with scoring model; roadmap refreshed quarterly."},
                    {"score": 4, "text": "Structured prioritisation framework used across most BUs; backlog maintained."},
                    {"score": 3, "text": "Use cases identified in workshops; prioritisation varies by domain."},
                    {"score": 2, "text": "Use cases driven by individual champions; no consistent discovery process."},
                    {"score": 1, "text": "No formal process; AI experiments started on an ad-hoc basis."},
                ],
            },
            {
                "id": "V3",
                "sub_dimension": "VALUE REALISATION",
                "title": "Scaling & Industrialisation",
                "question": "How effectively do you scale AI solutions from pilot to production?",
                "options": [
                    {"score": 5, "text": "Industrialised deployment pipeline; >70% of pilots reach production scale."},
                    {"score": 4, "text": "Clear path to production; most pilots scale with defined transition process."},
                    {"score": 3, "text": "Some pilots scale successfully; bottlenecks exist in handoff to production."},
                    {"score": 2, "text": "Pilots frequently stall; scaling is manual and resource-intensive."},
                    {"score": 1, "text": "Most AI pilots remain proofs-of-concept; none have reached enterprise scale."},
                ],
            },
        ],
    },
    {
        "id": "data",
        "label": "Data\nFoundation",
        "label_short": "Data\nFoundation",
        "color": "#1565C0",
        "questions": [
            {
                "id": "D1",
                "sub_dimension": "DATA FOUNDATION",
                "title": "Data Quality and Standards",
                "question": "How prepared and AI-ready is your data, data governance and data environment for high-value AI use cases and final office for cost-quality goals?",
                "options": [
                    {"score": 5, "text": "All critical data is consistently AI-ready and supports cross-domain, real-time use cases."},
                    {"score": 4, "text": "AI-ready datasets available for most high-value use cases."},
                    {"score": 3, "text": "Growing availability of AI-ready datasets, though gaps with false projects."},
                    {"score": 2, "text": "AI teams often perform one-time cleanup for each project, mitigating."},
                    {"score": 1, "text": "Not Aware Or AI-ready datasets rarely exist, large cleanup efforts required before any use."},
                ],
            },
            {
                "id": "D2",
                "sub_dimension": "DATA FOUNDATION",
                "title": "Data Architecture & Platforms",
                "question": "How well does your data architecture support AI at scale?",
                "options": [
                    {"score": 5, "text": "Unified data platform (lakehouse/mesh) with real-time pipelines and feature stores enterprise-wide."},
                    {"score": 4, "text": "Modern data architecture deployed; data products available for most AI use cases."},
                    {"score": 3, "text": "Hybrid architecture; data lakes exist but integration with AI tooling is partial."},
                    {"score": 2, "text": "Siloed data stores; significant engineering effort needed per AI project."},
                    {"score": 1, "text": "Legacy systems with no structured data architecture supporting AI."},
                ],
            },
            {
                "id": "D3",
                "sub_dimension": "DATA FOUNDATION",
                "title": "Data Governance & Compliance",
                "question": "How mature is your data governance and regulatory compliance posture for AI?",
                "options": [
                    {"score": 5, "text": "Automated data lineage, cataloguing, and access controls enforced; GDPR/AI Act compliant."},
                    {"score": 4, "text": "Data governance framework active; compliance monitored with regular audits."},
                    {"score": 3, "text": "Governance policies defined but inconsistently enforced across data domains."},
                    {"score": 2, "text": "Basic data policies exist; compliance is reactive, not proactive."},
                    {"score": 1, "text": "No formal data governance; compliance not yet considered for AI use cases."},
                ],
            },
        ],
    },
    {
        "id": "people",
        "label": "People and\nCulture",
        "label_short": "People &\nCulture",
        "color": "#1565C0",
        "questions": [
            {
                "id": "P1",
                "sub_dimension": "PEOPLE AND CULTURE",
                "title": "Training & Development",
                "question": "How effectively does your organisation build AI skills and capabilities across the workforce?",
                "options": [
                    {"score": 5, "text": "Company-wide, role-specific AI curricula with certifications; performance tracked and linked to delivery outcomes and shared tools."},
                    {"score": 4, "text": "Structured training available for key roles; AI literacy programmes provide all staff."},
                    {"score": 3, "text": "Formal training modules available but adoption and completion vary significantly."},
                    {"score": 2, "text": "Ad hoc AI training offered; limited reach and no formalised development pathways."},
                    {"score": 1, "text": "No formal AI training or development performed staff-wise."},
                ],
            },
            {
                "id": "P2",
                "sub_dimension": "PEOPLE AND CULTURE",
                "title": "Data Literacy & Multi-Stakeholder Engagement",
                "question": "What mechanisms exist to ensure that diverse stakeholder perspectives are incorporated into AI risk assessments, approvals, and ongoing monitoring?",
                "options": [
                    {"score": 5, "text": "Categorical multi-stakeholder risk forums, aligned all impact assessments and outcomes monitoring with feedback loops and audit trails."},
                    {"score": 4, "text": "Regular cross-functional reviews and standardised decision monitoring dashboards seen next in process."},
                    {"score": 3, "text": "Documented procedures for soliciting inputs; incorporation is periodic and project specific."},
                    {"score": 2, "text": "AI bias awareness checked occasionally; limited inconsistency across teams affects decisions."},
                    {"score": 1, "text": "Not Aware Or No formal mechanisms technical teams decide with minimal stakeholder input."},
                ],
            },
            {
                "id": "P3",
                "sub_dimension": "PEOPLE AND CULTURE",
                "title": "AI Culture & Change Management",
                "question": "How embedded is an AI-first culture across your organisation?",
                "options": [
                    {"score": 5, "text": "AI-first mindset embedded; leadership champions innovation and change management is systematic."},
                    {"score": 4, "text": "Strong AI culture in key functions; change programmes in place to broaden adoption."},
                    {"score": 3, "text": "Culture evolving; pockets of enthusiasm but resistance remains in some areas."},
                    {"score": 2, "text": "Limited awareness; culture change not yet formally addressed."},
                    {"score": 1, "text": "No deliberate culture or change management programme for AI adoption."},
                ],
            },
        ],
    },
    {
        "id": "trusted",
        "label": "Trusted and\nResponsible AI",
        "label_short": "Trusted &\nResponsible AI",
        "color": "#1565C0",
        "questions": [
            {
                "id": "T1",
                "sub_dimension": "TRUSTED AND RESPONSIBLE AI",
                "title": "Responsible Design and Ethical Development",
                "question": "How do your teams practise ethical guidelines, privacy, transparency, and accountability norms at AI design and development phase?",
                "options": [
                    {"score": 5, "text": "Ethical guidelines fully embedded in every design stage with mandatory checkpoints, automated monitoring, and cross-functional governance sign-off."},
                    {"score": 4, "text": "Standardised ethical design practices within domains; inconsistency controlled by most designers."},
                    {"score": 3, "text": "Ethical guidelines documented and referenced, but inconsistently practiced across most teams."},
                    {"score": 2, "text": "Basic awareness of ethical principles; limited ad-hoc incorporation in design workflows."},
                    {"score": 1, "text": "Not Aware Or No formal guidelines or processes integrated into AI development."},
                ],
            },
            {
                "id": "T2",
                "sub_dimension": "TRUSTED AND RESPONSIBLE AI",
                "title": "AI Risk & Compliance Framework",
                "question": "How mature is your organisation's AI risk management and regulatory compliance framework?",
                "options": [
                    {"score": 5, "text": "Enterprise AI risk taxonomy; automated compliance monitoring aligned to EU AI Act and sector regulations."},
                    {"score": 4, "text": "AI risk framework deployed; compliance reviewed regularly with clear escalation paths."},
                    {"score": 3, "text": "Risk assessment processes exist but are not consistently applied across projects."},
                    {"score": 2, "text": "Risk management ad hoc; compliance checked reactively post-deployment."},
                    {"score": 1, "text": "No formal AI risk or compliance framework in place."},
                ],
            },
            {
                "id": "T3",
                "sub_dimension": "TRUSTED AND RESPONSIBLE AI",
                "title": "Grounded GenAI Quality, Safety & Governance",
                "question": "How do you ensure quality, safety and governance for GenAI (RAG, PromptOps, usage, safety, rollback, governance)?",
                "options": [
                    {"score": 5, "text": "Automated output quality gates, grounding pipelines, and rollback mechanisms fully embedded with audit trails."},
                    {"score": 4, "text": "Changes to deployment pipelines actively reviewed; most quality and safety controls enforced."},
                    {"score": 3, "text": "Logs for model/prompt quality centrally stored, sometimes incomplete."},
                    {"score": 2, "text": "Not Aware Or Have some form of monitoring in place but without coverage of all critical content."},
                    {"score": 1, "text": "No formal monitoring or processes integrated into AI development."},
                ],
            },
        ],
    },
    {
        "id": "advanced",
        "label": "Advanced\nCapabilities",
        "label_short": "Advanced\nCapabilities",
        "color": "#1565C0",
        "questions": [
            {
                "id": "A1",
                "sub_dimension": "ADVANCED CAPABILITIES",
                "title": "Scalable AI Platform Enablement",
                "question": "What enterprise-grade platforms are you using for your technical AI development?",
                "options": [
                    {"score": 5, "text": "Unified enterprise AI stack (e.g. Azure, GCP, Databricks, Snowflake) fully integrated with MLOps pipelines, governance, and available company-wide."},
                    {"score": 4, "text": "Standardised enterprise platforms adopted across most teams with shared tooling, pipelines, and centralised governance."},
                    {"score": 3, "text": "Approved platforms documented; usage varies by team with partial toolchain integration."},
                    {"score": 2, "text": "Mixed tools and environments; limited enterprise alignment or scalability."},
                    {"score": 1, "text": "Not Aware Or No defined enterprise-grade AI platforms; development occurs in ad hoc or local setups."},
                ],
            },
            {
                "id": "A2",
                "sub_dimension": "ADVANCED CAPABILITIES",
                "title": "MLOps & Model Lifecycle Management",
                "question": "How mature is your MLOps practice for model development, deployment and monitoring?",
                "options": [
                    {"score": 5, "text": "Full MLOps automation: CI/CD for models, automated retraining, drift detection, and model registry enterprise-wide."},
                    {"score": 4, "text": "MLOps practices standardised; most models deployed via pipeline with monitoring dashboards."},
                    {"score": 3, "text": "MLOps partially implemented; some automation but manual steps in deployment and monitoring."},
                    {"score": 2, "text": "Ad hoc model deployment; limited version control or monitoring in place."},
                    {"score": 1, "text": "No MLOps practice; models deployed manually without lifecycle management."},
                ],
            },
            {
                "id": "A3",
                "sub_dimension": "ADVANCED CAPABILITIES",
                "title": "GenAI & Agentic AI Adoption",
                "question": "How mature is your organisation's adoption of Generative AI and Agentic AI capabilities?",
                "options": [
                    {"score": 5, "text": "GenAI and agentic workflows embedded in core products; prompt engineering, RAG, and agent orchestration at enterprise scale."},
                    {"score": 4, "text": "GenAI solutions in production for multiple use cases; agentic pilots underway."},
                    {"score": 3, "text": "Several GenAI POCs completed; moving towards production with governance in place."},
                    {"score": 2, "text": "Exploring GenAI; one or two experimental projects but no production deployment."},
                    {"score": 1, "text": "Not Aware Or No GenAI initiatives; limited understanding of applicability."},
                ],
            },
        ],
    },
    {
        "id": "engineering",
        "label": "AI\nEngineering",
        "label_short": "AI\nEngineering",
        "color": "#1565C0",
        "questions": [
            {
                "id": "E1",
                "sub_dimension": "AI ENGINEERING",
                "title": "AI Engineering Practices",
                "question": "How mature are your AI engineering standards, code quality, and delivery practices?",
                "options": [
                    {"score": 5, "text": "Enterprise-wide AI engineering standards; automated code review, testing, and security scanning fully integrated into CI/CD pipelines."},
                    {"score": 4, "text": "Engineering standards defined and adopted across most AI teams with peer review processes."},
                    {"score": 3, "text": "Standards documented; adoption varies by team and project type."},
                    {"score": 2, "text": "Some engineering best practices followed informally; no formal standards."},
                    {"score": 1, "text": "No formal AI engineering standards or delivery practices in place."},
                ],
            },
            {
                "id": "E2",
                "sub_dimension": "AI ENGINEERING",
                "title": "Build, Deploy & Scale AI Systems",
                "question": "How effectively can your engineering teams build, deploy, and scale production-grade AI systems?",
                "options": [
                    {"score": 5, "text": "AI systems built to enterprise production standards; automated deployment, scaling, and incident response across all environments."},
                    {"score": 4, "text": "Most AI systems production-ready; deployment pipelines well-defined with SLAs and monitoring."},
                    {"score": 3, "text": "Growing capability; some systems in production but scaling requires significant manual effort."},
                    {"score": 2, "text": "Engineering capacity limited; production deployments require significant manual effort and oversight."},
                    {"score": 1, "text": "Not Aware Or AI systems not yet at production grade; dev and prototype only."},
                ],
            },
            {
                "id": "E3",
                "sub_dimension": "AI ENGINEERING",
                "title": "AI Security & Infrastructure Resilience",
                "question": "How secure and resilient is your AI infrastructure and model deployment environment?",
                "options": [
                    {"score": 5, "text": "AI security integrated into DevSecOps; model adversarial testing, data encryption, and zero-trust architecture enforced."},
                    {"score": 4, "text": "Security policies defined for AI workloads; vulnerability assessments conducted regularly."},
                    {"score": 3, "text": "Basic security controls applied; AI-specific threat modelling not yet formalised."},
                    {"score": 2, "text": "Security considered post-deployment; limited AI-specific controls in place."},
                    {"score": 1, "text": "No AI-specific security or resilience measures; standard IT policies applied only."},
                ],
            },
        ],
    },
]

TOTAL_DIMENSIONS = len(DIMENSIONS)
QUESTIONS_PER_DIMENSION = max(len(d["questions"]) for d in DIMENSIONS)
MAX_SCORE_PER_DIMENSION = 5 * max(len(d["questions"]) for d in DIMENSIONS)
