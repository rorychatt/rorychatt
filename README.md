# Hi, I'm Mikael Rinne 👋

**1st Founding Engineer [@Ivy-Interactive](https://github.com/Ivy-Interactive)** · **Founder & CEO [@SpaceCorps](https://github.com/SpaceCorps)**

Full-stack and systems engineer from Estonia, based in Stockholm. Background in machine learning, chemistry, and computational physics — first author on an [IEEE IVNC 2023 paper](https://doi.org/10.1109/IVNC57695.2023.10188950) written in collaboration with CERN researchers. Over 25,000 GitHub contributions across systems programming, developer tooling, 3D graphics, and autonomous AI agents.

🌐 **[Portfolio & Contribution Heatmap](https://rorychatt.github.io/rorychatt/)** · 🪐 **[SpaceCorps Developer Hub](https://spacecorps.github.io)** · 💼 **[LinkedIn](https://www.linkedin.com/in/mikael-rinne/)** · 📄 **[IVNC 2023 Paper](https://doi.org/10.1109/IVNC57695.2023.10188950)**

---

### Core Technical Focus

- **Languages:** Rust, C# / .NET 9, TypeScript, Swift, Kotlin, Python, Fortran, WGSL / GLSL, SQL
- **Systems & 3D Graphics:** `wgpu`, WebGPU, WebGL, three.js, Tokio, Rayon, ECS, crossbeam, binary packet codecs
- **Agentic AI & Runtimes:** Apple Foundation Models, Gemini Nano / AICore, Anthropic & OpenAI APIs, MCP, Semantic Kernel, Vector Search
- **Architecture & Engineering:** Compilers, AST diffing, headless browser runtimes, TDD/SOLID, distributed state sync

---

## 📂 Public Projects & Open Source Directory

### 1. 🪐 3D Graphics, Simulation & Physics

Open-source real-time graphics, atomistic simulations, and virtual world engines written in Rust, Fortran, and TypeScript.

| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Space3d-Molecular](https://github.com/SpaceCorps/Space3d-Molecular)** | Rust, WGSL, Rayon | Molecular dynamics and electron-emission physics on Space3d — public API docs, input formats, and interactive 3D WebGPU viewer (`molviewer`). |
| **[SpaceCorps 2](https://github.com/rorychatt/SpaceCorps2)** / **[Front](https://github.com/SpaceCorps/SpaceCorps-Front)** | TypeScript, WebGL, three.js | Original WebGL 3D browser MMO RPG with real-time multiplayer network state synchronization and procedural world rendering. |
| **[GETELEC](https://github.com/AndKyr/GETELEC)** | Fortran, Python, Web | General Tool for Electron Emission Calculations: computes emission currents and Nottingham-effect heating from metal/semiconductor surfaces. Developed with CERN collaborators; basis of first-author IEEE IVNC 2023 paper. |
| **[rustmc-server](https://github.com/rorychatt/rustmc-server)** | Rust, Tokio | High-concurrency multi-threaded Minecraft server written in Rust with Paper plugin compatibility and custom binary packet codecs. |

---

### 2. 🤖 Autonomous Agents & On-Device AI Runtimes

Tool-calling runtimes, on-device local model integration, and self-learning agent infrastructure.

| Project | Stack | Description |
| :--- | :--- | :--- |
| **[open-apple-models](https://github.com/SpaceCorps/open-apple-models)** | Swift, FoundationModels, C ABI | Real tool calling for Apple's on-device Foundation Models on iOS, iPadOS, macOS and visionOS 27: per-step tool steering, runtime JSON-Schema tools, and a game layer for NPC dialogue, decisions and content generation. Ships as a Swift package, the `oam` CLI, an OpenAI-compatible server with working `tool_calls`, and a JSON-RPC protocol over stdio or a C ABI (C, Python and Unity C# bindings). MIT. [Docs](https://spacecorps.github.io/open-apple-models/). |
| **[open-android-models](https://github.com/SpaceCorps/open-android-models)** | Kotlin, ML Kit GenAI, JNI | The Android sibling on Gemini Nano (AICore / ML Kit GenAI Prompt API). Gemini Nano has no native tool calling yet, so tools run through a validated JSON step envelope. Kotlin agent core, the same game layer, and the same JSON-RPC protocol v1.0 over JNI, so an engine can inject either backend per platform. Pre-release: tested on the JVM and against Apple's on-device model as a proxy, not yet on a Gemini Nano device. MIT. |
| **[open-agents](https://github.com/SpaceCorps/open-agents)** | Rust, TypeScript | CLI-first autonomous coding agent runner: dynamic model selection, structured tool execution, and self-learning project memory. |
| **[open-browser](https://github.com/SpaceCorps/open-browser)** | Rust, TypeScript, Playwright | Agentic browser automation platform: Rust backend daemon + web interface enabling autonomous agents to navigate, inspect, and interact with the web. |
| **[brainwares](https://github.com/SpaceCorps/brainwares)** | Rust | High-efficiency memory vault system and semantic code storage optimized for coding agents. |
| **[web-demo-generator](https://github.com/SpaceCorps/web-demo-generator)** | TypeScript, Puppeteer, FFmpeg | Automated product demo generator: simulates human browser interactions, captures live UI changes, and renders H.264 video patchnotes. |
| **[sc-agent](https://github.com/SpaceCorps/sc-agent)** | TypeScript | SpaceCorps core autonomous agent orchestrator. |

---

### 3. ⚡ SpaceCorps Agentic CLI Fleet (Native Rust)

A fleet of standalone, high-performance, single-binary Rust CLIs designed for both human terminal operators and autonomous AI agents (featuring structured `--json` output, deterministic exit codes, and token-efficient formatting):

#### Cloud, Compute & Storage
| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Sliplane-Cli](https://github.com/SpaceCorps/Sliplane-Cli)** | Rust | Native CLI & agent interface for the Sliplane cloud hosting and deployment API (services, deployments, volumes, env vars, webhooks). |
| **[Cloudflare-Cli](https://github.com/SpaceCorps/Cloudflare-Cli)** | Rust | Native CLI & agent interface for Cloudflare v4 API (DNS records, zone management, cache purging, page rules). |
| **[Storage-Cli](https://github.com/SpaceCorps/Storage-Cli)** | Rust | High-throughput CLI for uploading files/directories to Azure Blob Storage with automated zip compression and SAS token generation. |

#### AI Search, Scraping & Registry Intelligence
| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Exa-Cli](https://github.com/SpaceCorps/Exa-Cli)** | Rust | Native CLI & agent interface for Exa AI neural search, semantic similarities, and raw web content extraction. |
| **[Firecrawl-Cli](https://github.com/SpaceCorps/Firecrawl-Cli)** | Rust | Native CLI & agent interface for Firecrawl web scraping, JS rendering, structured markdown extraction, and site crawling. |
| **[Tic-Cli](https://github.com/SpaceCorps/Tic-Cli)** | Rust | Swedish business registry (TIC) search for company financials, vehicle records, debtor data, and bankruptcy tracking. |

#### Domain Registrars & DNS Administration
| Project | Stack | Description |
| :--- | :--- | :--- |
| **[namecheap-cli](https://github.com/SpaceCorps/namecheap-cli)** | Rust | Fast, ergonomic CLI for Namecheap domain availability, contact management, DNS records, and account administration. |
| **[Spaceship-Cli](https://github.com/SpaceCorps/Spaceship-Cli)** | Rust | Native CLI & agent interface for the Spaceship registrar, DNS management, and hosting APIs. |
| **[Loopia-Cli](https://github.com/SpaceCorps/Loopia-Cli)** | Rust | Native CLI & agent interface for the Loopia XML-RPC API (Nordic domains, subdomains, and DNS record sets). |

#### Social, Developer & Market Intelligence (Apify-Powered)
| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Reddit-Cli](https://github.com/SpaceCorps/Reddit-Cli)** | Rust | Scrape and search Reddit communities, posts, and nested comments via Apify actors. |
| **[Twitter-Cli](https://github.com/SpaceCorps/Twitter-Cli)** | Rust | Search and scrape Twitter / X tweets, profiles, and conversation threads via Apify actors. |
| **[Linkedin-Cli](https://github.com/SpaceCorps/Linkedin-Cli)** | Rust | Fetch LinkedIn profiles and extract company/personal post feeds via Apify actors. |
| **[Youtube-Cli](https://github.com/SpaceCorps/Youtube-Cli)** | Rust | Scrape YouTube video metadata, search results, channel playlists, and video transcripts. |
| **[TikTok-Cli](https://github.com/SpaceCorps/TikTok-Cli)** | Rust | Scrape TikTok creator profiles, videos, trending hashtags, and music metadata. |
| **[Producthunt-Cli](https://github.com/SpaceCorps/Producthunt-Cli)** | Rust | Search and scrape Product Hunt product launches, maker details, topics, and upvotes. |
| **[Stackoverflow-Cli](https://github.com/SpaceCorps/Stackoverflow-Cli)** | Rust | Search Stack Overflow questions, parse accepted answers, and extract tag metadata. |

#### DevOps, Alerting & Communications
| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Claude-Sessions-Cli](https://github.com/SpaceCorps/Claude-Sessions-Cli)** | Rust | Instant transfer and recovery of Claude desktop Code-tab sessions across accounts and organizations without cloud telemetry. |
| **[Bugsink-Cli](https://github.com/SpaceCorps/Bugsink-Cli)** | Rust | Native CLI & agent interface for the Bugsink self-hosted error tracking platform (events, triage, project stats). |
| **[Heyreach-Cli](https://github.com/SpaceCorps/Heyreach-Cli)** | Rust | Native CLI & agent interface for HeyReach LinkedIn outbound lead generation and campaign automation. |
| **[Gmail-Cli](https://github.com/SpaceCorps/Gmail-Cli)** | Rust | CLI & agent interface for Gmail mailbox search, thread reading, attachment extraction, and draft dispatch. |
| **[Notify-Cli](https://github.com/SpaceCorps/Notify-Cli)** | Rust | Multi-channel notification CLI routing messages across Slack webhooks, SMTP email, system alerts, and message boxes. |
| **[Github-Issue-Importer](https://github.com/SpaceCorps/Github-Issue-Importer)** | Rust | Idempotent bulk issue and label importer for GitHub repositories from YAML/JSON specs. |

#### Hardware & IoT
| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Samsung-Artmode-Cli](https://github.com/SpaceCorps/Samsung-Artmode-Cli)** | Rust | Local network controller for Samsung The Frame TV Art Mode (artwork upload, matte filters, brightness, and slideshows). |

---

### 4. 🌿 The Ivy Ecosystem (.NET AI & Full-Stack Tooling)

Core developer platforms and compilers powering full-stack C# and agentic software creation at Ivy.

| Project | Stack | Description |
| :--- | :--- | :--- |
| **[Ivy-Framework](https://github.com/Ivy-Interactive/Ivy-Framework)** (435★) | C#, .NET 9, Roslyn, TypeScript | Full-stack framework for building internal web tools with LLM code generation. Unifies front-end and back-end in a single C# codebase with instant hot-reload. 1st founding engineer & core architect. |
| **[Ivy-Tendril](https://github.com/Ivy-Interactive/Ivy-Tendril)** (198★) | C#, .NET 9, Agent Runtimes | Next-generation developer environment built for when AI agents write 99% of code. Led implementation from first commit: 2,000+ commits and 650+ PRs in under six months. |
| **[Rusty-Framework](https://github.com/Ivy-Interactive/Rusty-Framework)** | Rust, axum, WASM | Full-stack web application framework in pure Rust — porting Ivy's single-language unified architecture to systems programming. |
| **[Ivy.NativeJsonDiff](https://github.com/Ivy-Interactive/Ivy.NativeJsonDiff)** | C#, Rust | High-performance native JSON diffing engine for reactive UI updates and state synchronization across the wire. |
| **[Ivy.Docs.Compiler](https://github.com/Ivy-Interactive/Ivy.Docs.Compiler)** | Rust | High-speed documentation compiler and markdown AST transformer powering Ivy developer docs. |
| **[Ivy-Command-Center](https://github.com/rorychatt/Ivy-Command-Center)** | C#, ASP.NET Core | Role-based authorization, enterprise permission scoping, and security policies for Ivy applications. |
| **[Ivy-Examples](https://github.com/Ivy-Interactive/Ivy-Examples)** & **[Templates](https://github.com/Ivy-Interactive/Ivy-Templates)** | C#, .NET | Production-ready reference architectures and blueprints showcasing full-stack C# AI applications. |
| **[Ivy-Design-System](https://github.com/Ivy-Interactive/Ivy-Design-System)** | TypeScript, Tailwind | Design tokens, shared UI primitives, and layout components for Ivy web applications. |
| **[Rustino](https://github.com/Ivy-Interactive/Rustino)** | Rust | Embedded & systems utility suite created for the Ivy engineering workflow. |
| **[edit-counter](https://github.com/Ivy-Interactive/edit-counter)** | Rust | Precision semantic source code edit and mutation tracker for AI code evaluation. |
| **[Pr-Cost-Calculator](https://github.com/Ivy-Interactive/Pr-Cost-Calculator)** | TypeScript | Token expenditure, review cost, and LLM telemetry estimator for automated pull requests. |

---

### 5. 💼 Web Platforms, Interactive Visualizations & Applications

Open-source web platforms, 3D interactive graphics, and systems tools.

| Project | Stack | Description |
| :--- | :--- | :--- |
| **[KeepIn](https://github.com/rorychatt/KeepIn)** / **[keepin-api](https://github.com/rorychatt/keepin-api)** | C#, ASP.NET Core, React, WebGL | E-commerce inventory, handling, and messaging system featuring an interactive 3D spatial storage visualizer. |
| **[timup.pro](https://github.com/DFlats/timup.pro)** | C#, ASP.NET Core, PostgreSQL | Live production .NET platform built under mob-programming and strict TDD discipline during the SALT program. |
| **[open-glass](https://github.com/SpaceCorps/open-glass)** / **[gilect](https://github.com/SpaceCorps/gilect)** | Rust, WebGPU, React | Spatial Apple Glass UI for the Web featuring real-time optical refraction, specular highlights, and glassmorphism shaders. |
| **[GrowthHack](https://github.com/SpaceCorps/GrowthHack)** | TypeScript, React | Acquisition analytics, user attribution pipeline, and telemetry dashboard built for SpaceCorps games. |
| **[gitpub](https://github.com/rorychatt/gitpub)** | Rust | Fast Git repository publishing and branch synchronization utility. |
| **[AIOS](https://github.com/rorychatt/AIOS)** | Rust | Experimental agent-driven operating system shell and command dispatcher. |
| **[SpaceCorps Hub](https://github.com/SpaceCorps/spacecorps.github.io)** | HTML5, Tailwind, JS | Official web portal, developer hub, and agent documentation index for SpaceCorps ([spacecorps.github.io](https://spacecorps.github.io)). |
| **[tendril-factory-talk](https://github.com/SpaceCorps/tendril-factory-talk)** | Markdown | Slide deck and retrospective (*"Three things that nearly killed our software factory"*). |
| **[open-trading](https://github.com/SpaceCorps/open-trading)** | C#, .NET | Algorithmic trading and portfolio simulation system. |
| **[openHosting](https://github.com/SpaceCorps/openHosting)** | TypeScript | Cloud hosting and infrastructure management dashboard. |
| **[ivy-one-business-one-platform](https://github.com/SpaceCorps/ivy-one-business-one-platform)** | C#, .NET | Enterprise all-in-one business management platform built on Ivy. |
| **[ivy-qr-code-generator](https://github.com/SpaceCorps/ivy-qr-code-generator)** | TypeScript | Dynamic QR code generator and asset pipeline. |
| **[dog-shelter-ua](https://github.com/SpaceCorps/dog-shelter-ua)** | TypeScript, React | Open-source adoption and shelter management portal. |

---

### 6. 📚 Curated Research & Ecosystem Resources

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
