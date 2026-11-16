<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:1e1b4b,100:312e81&height=230&section=header&text=Hi,%20I'm%20Sathwik&fontSize=60&fontColor=e0e7ff&animation=fadeIn&fontAlignY=36&desc=Software%20Enthusiast%20%7C%20Backend%20%C2%B7%20Full-Stack%20%C2%B7%20AI%20Systems&descSize=18&descColor=c7d2fe&descAlignY=58" width="100%" alt="header"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=900&color=A5B4FC&center=true&vCenter=true&width=760&height=50&lines=Software+Engineer;Backend+%7C+Microservices+%7C+REST+APIs;Full-Stack+Development;AI+Systems+%7C+LLMs+%7C+Agents+%7C+RAG;I+build+the+whole+stack" alt="Typing SVG" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=saisathwik22&label=PROFILE+VIEWS&color=312e81&style=for-the-badge&labelColor=0f0c29" alt="views"/>
<img src="https://img.shields.io/badge/STATUS-OPEN_TO_WORK-312e81?style=for-the-badge&labelColor=0f0c29" alt="status"/>

<br/><br/>

<a href="https://linkedin.com/in/saisathwik2822"><img src="https://img.shields.io/badge/LinkedIn-saisathwik2822-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:sathwik2822@gmail.com"><img src="https://img.shields.io/badge/Email-sathwik2822@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>

</div>

<br/>

---

## About Me

**🎓 Education**
<!-- ✏️ EDIT THIS LINE -->
B.Tech in Computer Science Engineering · Aurora Engineering College, Affiliated to JNTU Hyderabad

**📍 Location**
Hyderabad, Telangana, India

**💡 Interests** : AI | Backend | Full Stack

**🛠️ What I know and what I've built**
- REST APIs and asynchronous backends
- Multi-agent workflows with LangGraph and LangChain
- RAG pipelines with embeddings and vector search
- Deep learning models for NLP with TensorFlow and Keras
- Microservice and event-driven architectures

**🎯 Roles I'm open to**
- Backend Engineer
- Full-Stack Engineer
- AI / GenAI Engineer
- Software Engineer (general)

**🔧 Currently working on**
Adding MCP (Model Context Protocol) support to Trip Pilot AI.

---

## Tech Stack

<div align="center">

**Languages**

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java"/>
<img src="https://img.shields.io/badge/SQL-003B57?style=for-the-badge" alt="SQL"/>

**Backend**

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white" alt="Spring Boot"/>
<img src="https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Kafka"/>

**Databases and Caching**

<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"/>

**Cloud and DevOps**

<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
<img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black" alt="Render"/>

**AI / GenAI**

<img src="https://img.shields.io/badge/LLMs-412991?style=for-the-badge&logo=openai&logoColor=white" alt="LLMs"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"/>
<img src="https://img.shields.io/badge/LangGraph-4B2E83?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph"/>
<img src="https://img.shields.io/badge/Ollama-1F2937?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
<img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" alt="Groq"/>
<img src="https://img.shields.io/badge/TensorFlow_/_Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow / Keras"/>

</div>

---

## Featured Projects

### AgentStack: Multi-Agent AI Platform
**Tech:** Python, LangGraph, Qdrant, MongoDB, Redis, AWS S3, Docker, Firebase, Razorpay

- Built an AI platform covering chat, web search, code generation, PDF/PPT/image generation, PDF Q&A and image analysis, using LangGraph to classify intent and route each request to a specialized agent backed by its own LLM provider.
- Designed 4 independently deployable microservices (auth, chat, agents, billing) behind an API gateway, with RAG-based PDF Q&A using Gemini embeddings and Qdrant similarity search.
- Integrated Firebase Auth and Razorpay credit-based billing; containerized with Docker, backend on Render and frontend on Vercel.

### Real-Time Ride Matching System
**Tech:** Java, Spring Boot, Kafka, Redis, MySQL, Docker

- Designed an event-driven backend that separates ride management from driver matching, communicating asynchronously through Kafka so ride creation never blocks on matching.
- Used Redis geospatial indexes to track driver locations and find the nearest available drivers within a radius of the rider's pickup point.
- Persisted rides and driver state in MySQL via Spring Data JPA; one-command local setup with Docker Compose.

### Trip Pilot AI
**Tech:** Python, FastAPI, LangGraph, LangChain, Groq, PostgreSQL

- Built a full-stack AI travel planner that turns a natural-language request into flights, hotels and a day-by-day itinerary using specialized LangGraph agents with tool calling.
- Grounded outputs with live AviationStack and Tavily data, with error handling for API failures, and low-latency inference on Groq-hosted LLMs.
- FastAPI REST backend with PostgreSQL persisting conversation state per thread for follow-up refinements. *Next: adding MCP.*

### Moodline: Emotion Detection from Text
**Tech:** Python, TensorFlow/Keras, FastAPI

- Developed a 6-class emotion classification web app with a Bidirectional GRU, after benchmarking baseline RNN, LSTM and GRU models.
- Fixed severe class imbalance using computed class weights, improving minority-class recall and model stability.
- Built an async FastAPI backend with model lifecycle management for real-time predictions.

<div align="right">

<!-- Replace each REPO_NAME with your actual repo name -->
[AgentStack ↗](https://github.com/saisathwik22/REPO_NAME) · [Ride Matching ↗](https://github.com/saisathwik22/REPO_NAME) · [Trip Pilot AI ↗](https://github.com/saisathwik22/REPO_NAME) · [Moodline ↗](https://github.com/saisathwik22/REPO_NAME)

</div>

---

## Certifications

<div align="center">

| Certification | Issuer |
|:---|:---|
| **AWS Cloud Practitioner Essentials** | <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS"/> |
| **Data Science Essentials** | <img src="https://img.shields.io/badge/Cisco-1BA0D7?style=flat-square&logo=cisco&logoColor=white" alt="Cisco"/> |
| **Deep Learning** | <img src="https://img.shields.io/badge/Scaler_Topics-0B1F3A?style=flat-square" alt="Scaler Topics"/> |

</div>

---

## Contributions

<div align="center">

<img src="https://ghchart.rshah.org/40c463/saisathwik22" alt="GitHub contribution heatmap"/>
</div>

---


<details>
<summary><b>Easter egg: click to run <code>./secret.sh</code></b></summary>

<br/>

```bash
$ ./secret.sh
> Fun fact: I like systems that talk to each other,
> whether that's microservices over Kafka or agents over a LangGraph.
> Favorite debugging tool: print("here")
> Say hi → sathwik2822@gmail.com
```

</details>

<br/>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=3500&pause=1000&color=C7D2FE&center=true&vCenter=true&width=500&lines=Thanks+for+stopping+by;Open+to+backend%2C+full-stack+%26+AI+roles;Let's+build+something+great" alt="footer typing"/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:1e1b4b,100:312e81&height=120&section=footer" width="100%" alt="footer"/>

</div>
