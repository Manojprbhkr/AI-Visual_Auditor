# AI-Visual_Auditor
# 🔍 AI-Powered Visual & Structural Site Migration Auditor

🌐 [Click Here to Launch the Live Web App](https://ai-visualauditor.streamlit.app)

An automated enterprise-grade site migration audit utility designed to cross-examine and pinpoint differences between legacy platforms (e.g., Ektron) and modern digital experience environments (e.g., Optimizely). It maps layout deviations, detects text drift, and catalogs image anomalies across fully responsive device viewports.

---

## 🚀 Key Features & High Utility
- **Cross-Viewport Responsiveness:** Simulates and extracts elements simultaneously across **Desktop (1920x1080)**, **Tablet (768x1024)**, and **Mobile (375x667)** device targets using an optimized headless automated pipeline.
- **Advanced DOM Element Scraping:** Runs an adaptive semantic discovery script evaluating complex structures, layout boxes, nested grids, headers, footers, and active notification alerts.
- **Intelligent Component Matching:** Automatically pairs source components to destination counterparts using direct selector rules and front-end text fingerprinting models.
- **Volatile Secure Memory Processing:** Highly optimized for cloud environments. Full-page layout images and Excel worksheets stream directly through the runtime space using **Base64 memory maps** and **`BytesIO` buffers**, ensuring **zero persistent file traces or memory leaks on the host server disk**.

---

## 🛠️ System Architecture

The project utilizes a modern, completely decoupled, full-stack microservice structure:

- **Frontend (`ui.py`):** A responsive web app built with Streamlit. It handles inputs, parses encoded memory packets on-the-fly, builds interface tabs dynamically, and triggers multi-user file streams natively.
- **Backend (`main.py`):** An asynchronous FastAPI microservice running a headless Chromium browser engine managed by Playwright. It isolates multiple simultaneous user requests safely using individual UUID-tagged runtime boundaries.
- **Reporting Matrix:** Utilizes **Pillow (PIL)** for automated side-by-side snapshot stitching (highlighting missing layout components cleanly in bold red masks) and **OpenPyXL** for generating categorized multi-sheet master audit worksheets.

---

## 📦 Local Installation & Standalone Launch

To evaluate or run this infrastructure locally on a developer machine, clone the framework and run the local network routes:

### 1. Provision System Dependencies
```bash
# Clone the repository
git clone https://github.com
cd AI-Visual_Auditor

# Install project dependencies
pip install -r requirements.txt

# Provision headless browser framework binaries
playwright install --with-deps chromium
```

### 2. Run the Application Environment
Open two isolated terminal instances to run the standalone microservices:

* **Terminal 1 (Backend Engine Server):**
  ```bash
  python main.py
  ```
* **Terminal 2 (User Workspace Dashboard UI):**
  ```bash
  streamlit run ui.py
  ```

---

## 🛡️ Live Production Deployments
This codebase is completely cloud-agnostic. For persistent, zero-maintenance presentation links:
1. Host the underlying FastAPI scraping microservice engine on **Render** or **Koyeb** (Provisioned with a Linux environment containing structural system library overlays for Chromium).
2. Host the frontend user dashboard interface on **Streamlit Community Cloud** linked seamlessly back to your web service engine route.
