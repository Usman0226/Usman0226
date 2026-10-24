<img src="./assets/hero.svg" alt="Usman. Full-stack and AI engineer building real-time web applications and backend systems. Available for internships & freelance. 2,100+ students cleared dues through NoDues at MITS. 4 production platforms live. 10+ shipped tools, APIs, and libraries." width="100%">

<img src="./assets/i-pin.svg" width="18" height="18" align="middle"> Madanapalle, Andhra Pradesh &nbsp;·&nbsp; Available for freelance & select client work

## <img src="./assets/i-layers.svg" width="18" height="18" align="middle"> Selected work

<table>
<tr>
<td width="50%" valign="top">
<a href="https://www.nodues-arcclub.tech/"><img src="./assets/work-nodues.svg" alt="NoDues - Animated clearance checklist" width="100%"></a><br>
<b><a href="https://www.nodues-arcclub.tech/">NoDues</a></b> &nbsp; <a href="https://www.nodues-arcclub.tech/"><img src="./assets/i-link.svg" width="13" height="13" align="middle"></a><br>
Semester clearance for ~2,100 students and 30+ faculty at MITS. Approvals update live over SSE, and class setup imports Excel timetables with fuzzy faculty matching.<br>
<code>React</code> <code>Express</code> <code>MongoDB</code> &nbsp;·&nbsp; <a href="https://github.com/Usman0226/NoDues">Source</a>
</td>
<td width="50%" valign="top">
<a href="https://dfesta.in"><img src="./assets/work-dfesta.svg" alt="D'FESTA 2K26 - Animated event pass with scanning QR laser" width="100%"></a><br>
<b><a href="https://dfesta.in">D'FESTA 2K26</a></b> &nbsp; <a href="https://dfesta.in"><img src="./assets/i-link.svg" width="13" height="13" align="middle"></a><br>
Ticketing, payments and judging for the department symposium. AES-signed QR tickets, triple-node SMTP failover, and paise-offset UPI reconciliation.<br>
<code>Next.js 16</code> <code>TypeScript</code> <code>MongoDB</code>
</td>
</tr>
<tr>
<td valign="top">
<img src="./assets/work-bizeasy.svg" alt="BizEasy - WhatsApp-style order with payment confirmation" width="100%"><br>
<b>BizEasy</b><br>
A seller platform for small businesses in Andhra Pradesh, run over <img src="./assets/i-chat.svg" width="15" height="15" align="middle"> WhatsApp. I'm the backend engineer. Each seller connects their own number to their own bot.<br>
<code>Node.js</code> <code>Meta Cloud API</code> <code>Razorpay</code>
</td>
<td valign="top">
<a href="https://ncc-exam-portal.vercel.app/"><img src="./assets/work-ncc.svg" alt="NCC Exam Portal - Animated question card with ticking exam clock" width="100%"></a><br>
<b><a href="https://ncc-exam-portal.vercel.app/">NCC Exam Portal</a></b> &nbsp; <a href="https://ncc-exam-portal.vercel.app/"><img src="./assets/i-link.svg" width="13" height="13" align="middle"></a><br>
Timed exams for the NCC Tirupati Unit with admin, officer and cadet <img src="./assets/i-shield.svg" width="15" height="15" align="middle"> roles. Tenant isolation lives in Prisma middleware, and the server decides when an exam <img src="./assets/i-timer.svg" width="15" height="15" align="middle"> ends.<br>
<code>React</code> <code>Express</code> <code>PostgreSQL</code> <code>Prisma</code>
</td>
</tr>
<tr>
<td valign="top">
<a href="https://github.com/Usman0226/The-Brain"><img src="./assets/work-hireminds.svg" alt="HireMinds AI - Animated interview with filling score bar" width="100%"></a><br>
<b><a href="https://github.com/Usman0226/The-Brain">HireMinds AI</a></b> &nbsp; <a href="https://github.com/Usman0226/The-Brain"><img src="./assets/i-link.svg" width="13" height="13" align="middle"></a><br>
An autonomous interviewer with an agentic loop, a multi-layer evaluation engine, a critic layer and a recruiter dashboard.<br>
<code>FastAPI</code> <code>React</code> <code>Groq</code>
</td>
<td valign="top">
<a href="https://github.com/Usman0226/LifeLink"><img src="./assets/work-lifelink.svg" alt="LifeLink - Animated emergency dispatch with geolocation route and hospital radar" width="100%"></a><br>
<b><a href="https://github.com/Usman0226/LifeLink">LifeLink</a></b> &nbsp; <a href="https://github.com/Usman0226/LifeLink"><img src="./assets/i-link.svg" width="13" height="13" align="middle"></a><br>
<img src="./assets/i-trophy.svg" width="15" height="15" align="middle"> Emergency medical dispatch platform connecting hospitals, ambulances, and patients with real-time geolocation. LifeLink Hackathon Winner.<br>
<code>React</code> <code>Node.js</code> <code>Socket.io</code> <code>Leaflet</code>
</td>
</tr>
</table>

<details>
<summary><b>How a BizEasy order flows</b></summary>

```mermaid
flowchart LR
  C[Customer on WhatsApp] --> M[Meta Cloud API]
  M -->|webhook, routed by phone_number_id| A[BizEasy API]
  A --> B[Per-seller bot state machine]
  B --> O[(Orders)]
  B --> P[Razorpay payment link]
  P -->|webhook confirms payment| A
  A -->|WebSocket| S[Seller app]
```

</details>

<details>
<summary>More on GitHub</summary>

- [OCR_BENCHMARKING](https://github.com/Usman0226/OCR_BENCHMARKING): benchmarking OCR engines (PaddleOCR, Tesseract) on scanned historical documents, with word-level bounding boxes.
- [COMPONENTS](https://github.com/Usman0226/COMPONENTS): motion components for React. Copy, paste, done.
- [Agent-Effi](https://github.com/Usman0226/Agent-Effi): makes your AI agent think like the laziest senior dev in the room.
- [INCOIS-Sytem](https://github.com/Usman0226/INCOIS-Sytem): oceanographic scientist dashboard with geospatial ocean data visualization.

</details>

## Live systems

<img src="./assets/status.svg" alt="Live status table for NoDues, D'FESTA 2K26 and the NCC Exam Portal, refreshed every six hours" width="100%">

## Recognition

<img src="./assets/recognition.svg" alt="LifeLink hackathon winner. Onco-IQ internship at NIT Pondicherry. IIC Innovation Coordinator and ARC Club Student Coordinator at MITS Madanapalle." width="100%">

## Stack

<img src="./assets/stack.svg" alt="Product: React, Next.js, TypeScript, Tailwind, Framer Motion. Backend and data: Node.js, Express, NestJS, PostgreSQL, MongoDB, Prisma, Redis. AI: Python, FastAPI, LangChain, RAG pipelines, Gemini, Groq. Shipping: Vercel, Azure, Firebase, GitHub Actions." width="100%">

## Activity

<img src="./assets/activity.svg" alt="Public contributions over the last 12 months, with longest streak and busiest week, and a weekly sparkline" width="100%">

Client and event platforms live in private repositories, so this shows only part of the work. Redrawn every day by a GitHub Action.

## Contact

Available for freelance contracts, full-stack MVPs, and client projects:

<a href="https://www.linkedin.com/in/chandan-usman-gani-163aa9321/"><img src="./assets/btn-linkedin.svg" alt="LinkedIn" height="40"></a>
<a href="mailto:chandanusmangani@gmail.com"><img src="./assets/btn-email.svg" alt="Email me" height="40"></a>
