# Hi, I'm Mikael Rinne 👋

**1st Founding Engineer [@Ivy-Interactive](https://github.com/Ivy-Interactive)** · **Founder & CEO [@SpaceCorps](https://github.com/SpaceCorps)**

Full-stack and systems engineer from Estonia, based in Stockholm. Background in machine learning, chemistry, and computational physics — first author on an [IEEE IVNC 2023 paper](https://doi.org/10.1109/IVNC57695.2023.10188950) written in collaboration with CERN researchers. Over 25,000 GitHub contributions across systems programming, developer tooling, 3D graphics engines, and autonomous AI agents.

🌐 **[Portfolio & Contribution Heatmap](https://rorychatt.github.io/rorychatt/)** · 🪐 **[SpaceCorps Developer Hub](https://spacecorps.github.io)** · 💼 **[LinkedIn](https://www.linkedin.com/in/mikael-rinne/)** · 📄 **[IVNC 2023 Paper](https://doi.org/10.1109/IVNC57695.2023.10188950)**

---

### Core Technical Focus

- **Languages:** Rust, C# / .NET 9, TypeScript, Swift, Kotlin, Python, Fortran, WGSL / GLSL, SQL
- **Systems & 3D Graphics:** `wgpu`, WebGPU, WebGL, three.js, Tokio, Rayon, ECS, crossbeam, binary packet codecs
- **Agentic AI & Runtimes:** Apple Foundation Models, Gemini Nano / AICore, Anthropic & OpenAI APIs, MCP, Semantic Kernel, Vector Search
- **Architecture & Engineering:** Compilers, sparse Cargo registries, AST diffing, headless browser runtimes, TDD/SOLID, distributed state sync

---

## 📂 Projects by Category

### 1. 🪐 3D Graphics Engines, Simulation & Physics

High-performance real-time rendering, atomistic simulations, and virtual world engines written in pure Rust, Fortran, and TypeScript.

| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **Space3d** | 🔒 `Private` | Rust, `wgpu 30`, WGSL, ECS | Cross-platform 3D simulation and game engine in pure Rust. Features high-efficiency GPU indirect instanced rendering (1M+ instances), deterministic 60Hz fixed-timestep ECS, and native/web compilation. |
| **[Space3d-Molecular](https://github.com/SpaceCorps/Space3d-Molecular)** | 🟢 `Public` (Docs) / 🔒 `Private` (Engine) | Rust, WGSL, Rayon | Atomistic molecular dynamics (`spacemd` @ 108M atom-steps/s) and thermal-field electron emission physics (`spaceemit` @ 14 µs/pt), with WebGPU 3D viewer integration (`molviewer`). |
| **SpaceCorps2027** | 🔒 `Private` | Rust, Space3d, ECS, UDP | Native desktop 3D space MMO RPG running on the Space3d engine (client and authoritative multi-threaded game server). |
| **[SpaceCorps 2](https://github.com/rorychatt/SpaceCorps2)** / **[Front](https://github.com/SpaceCorps/SpaceCorps-Front)** | 🟢 `Public` | TypeScript, WebGL, three.js | Original WebGL 3D browser MMO RPG with real-time multiplayer network state synchronization and custom procedural world generation. |
| **[GETELEC](https://github.com/AndKyr/GETELEC)** | 🟢 `Public` | Fortran, Python, Web | General Tool for Electron Emission Calculations: computes emission currents and Nottingham-effect heating from metal/semiconductor surfaces. Developed with CERN collaborators; basis of first-author IEEE IVNC 2023 paper. |
| **[rustmc-server](https://github.com/rorychatt/rustmc-server)** | 🟢 `Public` | Rust, Tokio | High-concurrency multi-threaded Minecraft server written in Rust with Paper plugin compatibility and custom binary protocol codecs. |

---

### 2. 🤖 Autonomous Agents & On-Device AI Runtimes

Tool-calling runtimes, local neural model integration, and self-learning agent infrastructure.

| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[open-apple-models](https://github.com/SpaceCorps/open-apple-models)** | 🟢 `Public` | Swift, Rust, Python | Agentic tool calling for Apple Foundation Models: Swift package, CLI, and OpenAI-compatible server for on-device AI, NPC dialogue, and autonomous decision-making on iOS, iPadOS, and macOS. |
| **[open-android-models](https://github.com/SpaceCorps/open-android-models)** | 🟢 `Public` | Kotlin, Rust, JNI | Agentic tool calling for Android's built-in Gemini Nano (AICore / ML Kit Prompt API): Kotlin library, NPC decision engine, and JSON-RPC protocol bridge over JNI. |
| **Swindle** | 🔒 `Private` | Rust, Space3d, Apple Foundation Models, Swift | 100-day economic survival game: trade, negotiate, and bluff in a dense bazaar populated by autonomous LLM-driven NPCs with distinct personalities and memory. |
| **[open-agents](https://github.com/SpaceCorps/open-agents)** | 🟢 `Public` | Rust, TypeScript | CLI-first autonomous coding agent runner: dynamic model selection, structured tool execution, and self-learning project memory. |
| **[open-browser](https://github.com/SpaceCorps/open-browser)** | 🟢 `Public` | Rust, TypeScript, Playwright | Agentic browser automation platform: Rust backend daemon + web interface enabling autonomous agents to navigate, inspect, and interact with the web. |
| **[brainwares](https://github.com/SpaceCorps/brainwares)** | 🟢 `Public` | Rust | High-efficiency memory vault system and semantic code storage optimized for coding agents. |
| **[web-demo-generator](https://github.com/SpaceCorps/web-demo-generator)** | 🟢 `Public` | TypeScript, Puppeteer, FFmpeg | Automated product demo generator: simulates human browser interactions, captures live UI changes, and renders H.264 video patchnotes. |
| **[sc-agent](https://github.com/SpaceCorps/sc-agent)** | 🟢 `Public` | TypeScript | SpaceCorps core autonomous agent orchestrator. |

---

### 3. ⚡ SpaceCorps Agentic CLI Fleet (Native Rust)

A fleet of 24 standalone, high-performance, single-binary Rust CLIs designed for both human terminal operators and autonomous AI agents (featuring structured `--json` output, deterministic exit codes, and token-efficient formatting):

#### Cloud, Compute & Storage
| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[Sliplane-Cli](https://github.com/SpaceCorps/Sliplane-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for the Sliplane cloud hosting and deployment API (services, deployments, volumes, env vars, webhooks). |
| **[Cloudflare-Cli](https://github.com/SpaceCorps/Cloudflare-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for Cloudflare v4 API (DNS records, zone management, cache purging, page rules). |
| **[Storage-Cli](https://github.com/SpaceCorps/Storage-Cli)** | 🟢 `Public` | Rust | High-throughput CLI for uploading files/directories to Azure Blob Storage with automated zip compression and SAS token generation. |

#### AI Search, Scraping & Registry Intelligence
| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[Exa-Cli](https://github.com/SpaceCorps/Exa-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for Exa AI neural search, semantic similarities, and raw web content extraction. |
| **[Firecrawl-Cli](https://github.com/SpaceCorps/Firecrawl-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for Firecrawl web scraping, JS rendering, structured markdown extraction, and site crawling. |
| **[Tic-Cli](https://github.com/SpaceCorps/Tic-Cli)** | 🟢 `Public` | Rust | Swedish business registry (TIC) search for company financials, vehicle records, debtor data, and bankruptcy tracking. |

#### Domain Registrars & DNS Administration
| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[namecheap-cli](https://github.com/SpaceCorps/namecheap-cli)** | 🟢 `Public` | Rust | Fast, ergonomic CLI for Namecheap domain availability, contact management, DNS records, and account administration. |
| **[Spaceship-Cli](https://github.com/SpaceCorps/Spaceship-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for the Spaceship registrar, DNS management, and hosting APIs. |
| **[Loopia-Cli](https://github.com/SpaceCorps/Loopia-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for the Loopia XML-RPC API (Nordic domains, subdomains, and DNS record sets). |

#### Social, Developer & Market Intelligence (Apify-Powered)
| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[Reddit-Cli](https://github.com/SpaceCorps/Reddit-Cli)** | 🟢 `Public` | Rust | Scrape and search Reddit communities, posts, and nested comments via Apify actors. |
| **[Twitter-Cli](https://github.com/SpaceCorps/Twitter-Cli)** | 🟢 `Public` | Rust | Search and scrape Twitter / X tweets, profiles, and conversation threads via Apify actors. |
| **[Linkedin-Cli](https://github.com/SpaceCorps/Linkedin-Cli)** | 🟢 `Public` | Rust | Fetch LinkedIn profiles and extract company/personal post feeds via Apify actors. |
| **[Youtube-Cli](https://github.com/SpaceCorps/Youtube-Cli)** | 🟢 `Public` | Rust | Scrape YouTube video metadata, search results, channel playlists, and video transcripts. |
| **[TikTok-Cli](https://github.com/SpaceCorps/TikTok-Cli)** | 🟢 `Public` | Rust | Scrape TikTok creator profiles, videos, trending hashtags, and music metadata. |
| **[Producthunt-Cli](https://github.com/SpaceCorps/Producthunt-Cli)** | 🟢 `Public` | Rust | Search and scrape Product Hunt product launches, maker details, topics, and upvotes. |
| **[Stackoverflow-Cli](https://github.com/SpaceCorps/Stackoverflow-Cli)** | 🟢 `Public` | Rust | Search Stack Overflow questions, parse accepted answers, and extract tag metadata. |

#### DevOps, Alerting & Communications
| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[Bugsink-Cli](https://github.com/SpaceCorps/Bugsink-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for the Bugsink self-hosted error tracking platform (events, triage, project stats). |
| **[Heyreach-Cli](https://github.com/SpaceCorps/Heyreach-Cli)** | 🟢 `Public` | Rust | Native CLI & agent interface for HeyReach LinkedIn outbound lead generation and campaign automation. |
| **[Gmail-Cli](https://github.com/SpaceCorps/Gmail-Cli)** | 🟢 `Public` | Rust | CLI & agent interface for Gmail mailbox search, thread reading, attachment extraction, and draft dispatch. |
| **[Notify-Cli](https://github.com/SpaceCorps/Notify-Cli)** | 🟢 `Public` | Rust | Multi-channel notification CLI routing messages across Slack webhooks, SMTP email, system alerts, and message boxes. |
| **[Github-Issue-Importer](https://github.com/SpaceCorps/Github-Issue-Importer)** | 🟢 `Public` | Rust | Idempotent bulk issue and label importer for GitHub repositories from YAML/JSON specs. |
| **Claude-Sessions-Cli** | 🔒 `Private` | Rust | Tool for migrating and transferring Claude desktop Code-tab sessions between accounts and organizations. |

#### Hardware & IoT
| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[Samsung-Artmode-Cli](https://github.com/SpaceCorps/Samsung-Artmode-Cli)** | 🟢 `Public` | Rust | Local network controller for Samsung The Frame TV Art Mode (artwork upload, matte filters, brightness, and slideshows). |

---

### 4. 🌿 The Ivy Ecosystem (.NET AI & Full-Stack Tooling)

Core developer platforms and compilers powering full-stack C# and agentic software creation at Ivy.

| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **[Ivy-Framework](https://github.com/Ivy-Interactive/Ivy-Framework)** | 🟢 `Public` (434★) | C#, .NET 9, Roslyn, TypeScript | Full-stack framework for building internal web tools with LLM code generation. Unifies front-end and back-end in a single C# codebase with instant hot-reload. 1st founding engineer & core architect. |
| **[Ivy-Tendril](https://github.com/Ivy-Interactive/Ivy-Tendril)** | 🟢 `Public` (198★) | C#, .NET 9, Agent Runtimes | Next-generation developer environment built for when AI agents write 99% of code. Led implementation from first commit: 2,000+ commits and 650+ PRs in under six months. |
| **[Rusty-Framework](https://github.com/Ivy-Interactive/Rusty-Framework)** | 🟢 `Public` | Rust, axum, WASM | Full-stack web application framework in pure Rust — porting Ivy's single-language unified architecture to systems programming. |
| **[Ivy.NativeJsonDiff](https://github.com/Ivy-Interactive/Ivy.NativeJsonDiff)** | 🟢 `Public` | C#, Rust | High-performance native JSON diffing engine for reactive UI updates and state synchronization across the wire. |
| **[Ivy.Docs.Compiler](https://github.com/Ivy-Interactive/Ivy.Docs.Compiler)** | 🟢 `Public` | Rust | High-speed documentation compiler and markdown AST transformer powering Ivy developer docs. |
| **[Ivy-Command-Center](https://github.com/rorychatt/Ivy-Command-Center)** | 🟢 `Public` | C#, ASP.NET Core | Role-based authorization, enterprise permission scoping, and security policies for Ivy applications. |
| **[Ivy-Examples](https://github.com/Ivy-Interactive/Ivy-Examples)** & **[Templates](https://github.com/Ivy-Interactive/Ivy-Templates)** | 🟢 `Public` | C#, .NET | Production-ready reference architectures and blueprints showcasing full-stack C# AI applications. |
| **[Ivy-Design-System](https://github.com/Ivy-Interactive/Ivy-Design-System)** | 🟢 `Public` | TypeScript, Tailwind | Design tokens, shared UI primitives, and layout components for Ivy web applications. |
| **[Rustino](https://github.com/Ivy-Interactive/Rustino)** | 🟢 `Public` | Rust | Embedded & systems utility suite created for the Ivy engineering workflow. |
| **[edit-counter](https://github.com/Ivy-Interactive/edit-counter)** | 🟢 `Public` | Rust | Precision semantic source code edit and mutation tracker for AI code evaluation. |
| **[Pr-Cost-Calculator](https://github.com/Ivy-Interactive/Pr-Cost-Calculator)** | 🟢 `Public` | TypeScript | Token expenditure, review cost, and LLM telemetry estimator for automated pull requests. |

---

### 5. 🏗️ Developer Platforms, Venture Studio & Infrastructure

Custom Cargo distribution, venture validation systems, and design libraries powering SpaceCorps ventures.

| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **SpaceCorps Foundry** | 🔒 `Private` | Rust, TypeScript, Shell | SpaceCorps autonomous venture studio and rapid SaaS development engine: automated validation, scaffold generation, and deployment orchestration. |
| **SpaceCorps-Registry** | 🔒 `Private` | Rust, axum, Sliplane | Ultra-lightweight Cargo sparse index registry and binary distribution server running in ≈3 MiB RSS. |
| **SpaceCorps Storybook** | 🔒 `Private` | React, Storybook, Vite | SpaceCorps organization design system: shared components, renderers, tokens, and visual widgets. |
| **[SpaceCorps Developer Hub](https://github.com/SpaceCorps/spacecorps.github.io)** | 🟢 `Public` | HTML5, Tailwind, JS | Official web portal, developer hub, and agent documentation index for SpaceCorps ([spacecorps.github.io](https://spacecorps.github.io)). |
| **Devidence** | 🔒 `Private` | TypeScript, Next.js, Node.js | Verified developer credential platform: evidence-checked technical skills and automated CV claim auditing. |
| **Tendril-Vault** & **[Factory Talk](https://github.com/SpaceCorps/tendril-factory-talk)** | 🔒 `Private` / 🟢 `Public` | Markdown, C# | Internal engineering knowledge vault and retrospective slide deck (*"Three things that nearly killed our software factory"*). |
| **Business Idea Validator** | 🔒 `Private` | PowerShell, Claude Opus, HTML | Venture studio validation framework scoring product concepts against statutory registries (Bolagsverket, Companies House, ONS, SCB) and AGI durability. |

---

### 6. 💼 Production Platforms, Commercial Products & Web Apps

Vertical SaaS, systems tools, 3D interactive applications, and client solutions.

| Project | Visibility | Stack | Description |
| :--- | :---: | :--- | :--- |
| **FoodSafetyOS** | 🔒 `Private` | TypeScript, React, Tailwind | Digital *egenkontroll* (HACCP) self-serve compliance platform replacing paper binder checklists for Swedish commercial kitchens. |
| **Filament** | 🔒 `Private` | Rust, `wgpu`, Chromium | Lightweight Rust browser for E2E verification, visual diffing, and screenshot rendering: native HTML/CSS engine with Chromium escalation fallback. |
| **[KeepIn](https://github.com/rorychatt/KeepIn)** / **[keepin-api](https://github.com/rorychatt/keepin-api)** | 🟢 `Public` | C#, ASP.NET Core, React, WebGL | E-commerce inventory, handling, and messaging system featuring an interactive 3D spatial storage visualizer. |
| **[timup.pro](https://github.com/DFlats/timup.pro)** | 🟢 `Public` | C#, ASP.NET Core, PostgreSQL | Live production .NET platform built under mob-programming and strict TDD discipline during the SALT program. |
| **[open-glass](https://github.com/SpaceCorps/open-glass)** / **[gilect](https://github.com/SpaceCorps/gilect)** | 🟢 `Public` | Rust, WebGPU, React | Spatial Apple Glass UI for the Web featuring real-time optical refraction, specular highlights, and glassmorphism shaders. |
| **[GrowthHack](https://github.com/SpaceCorps/GrowthHack)** | 🟢 `Public` | TypeScript, React | Acquisition analytics, user attribution pipeline, and telemetry dashboard built for SpaceCorps games. |
| **[gitpub](https://github.com/rorychatt/gitpub)** | 🟢 `Public` | Rust | Fast Git repository publishing and branch synchronization utility. |
| **[AIOS](https://github.com/rorychatt/AIOS)** | 🟢 `Public` | Rust | Experimental agent-driven operating system shell and command dispatcher. |
| **Domain & Vertical Products** | 🟢 `Public` / 🔒 `Private` | C#, TypeScript, Python | Specialized customer platforms including **autodealer_crm**, **open-trading**, **openHosting**, **dog-shelter-ua**, **ivy-one-business-one-platform**, **ivy-qr-code-generator**, and **Private-Cloud**. |

---

### 7. 📚 Curated Research & Ecosystem Resources

Maintained community lists and research compendiums tracking agent architectures, UI design, and modern dev tools:

- **[awesome-ai-agent-platforms](https://github.com/rorychatt/awesome-ai-agent-platforms)** — Open-source AI coworkers, teammates, runtimes, and coding agents.
- **[Awesome-Graphs-Meet-Agents](https://github.com/rorychatt/Awesome-Graphs-Meet-Agents)** — Graph-empowered agents and agent-facilitated graph learning.
- **[Awesome-Reliable-Self-Evolving-Agents](https://github.com/rorychatt/Awesome-Reliable-Self-Evolving-Agents)** — Research survey on self-evolving and self-correcting agents.
- **[awesome-x402](https://github.com/rorychatt/awesome-x402)** — HTTP 402 payment required protocol, micropayments, and agent economy tooling.
- **[frontend-resources](https://github.com/rorychatt/frontend-resources)** & **[frontend-design-resources](https://github.com/rorychatt/frontend-design-resources)** — Curated directories for modern UI/UX design and frontend tooling.

---

<p align="center">
  <sub>Built with care by Mikael Rinne (@rorychatt) · Powered by Rust, .NET & Open Source</sub>
</p>
