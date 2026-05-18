import streamlit as st
import requests
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Site Migration Auditor", layout="wide")
st.title("🌐 Enterprise Site Migration Auditor")
st.caption("Built for Visual Testing on As-IS Website Migration")

# --- UI INPUTS ---
col1, col2 = st.columns(2)
with col1:
    source = st.text_input("Source URL", placeholder="https://")
with col2:
    staging = st.text_input("Staging URL", placeholder="https://")

 
BACKEND_URL = "https://ai-visual-auditor.onrender.com/compare"

if st.button("🚀 Run Audit", type="primary"):
    if not (source and staging):
        st.error("Please provide both Source and Staging URLs.")
    else:
        with st.spinner("Analyzing viewports... All data streaming securely in memory."):
            try:
                response = requests.post(
                    BACKEND_URL, 
                    json={"source_url": source, "staging_url": staging}, 
                    timeout=600
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Audit Complete!")
                    
                    # 1. RENDER EXCEL DOWNLOAD VIA MEMORY BASE64
                    excel_b64 = result.get("tabular_report_b64")
                    excel_filename = result.get("excel_filename", "Migration_Audit_Report.xlsx")
                    
                    if excel_b64:
                        excel_bytes = base64.b64decode(excel_b64)
                        st.download_button(
                            label="📥 Download Master Excel Audit",
                            data=excel_bytes,
                            file_name=excel_filename,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
                    
                    # 2. RENDER VISUAL EVIDENCE VIA MEMORY BASE64
                    visual_reports = result.get("visual_reports_b64", {})
                    
                    if visual_reports:
                        st.subheader("🖼️ Visual Evidence")
                        viewports = list(visual_reports.keys())
                        tabs = st.tabs([v.upper() for v in viewports])
                        
                        for idx, tab in enumerate(tabs):
                            vp_name = viewports[idx]
                            img_b64 = visual_reports[vp_name]
                            
                            with tab:
                                img_bytes = base64.b64decode(img_b64)
                                st.image(
                                    img_bytes, 
                                    caption=f"{vp_name.upper()} Comparison Map (Failures Outlined Red)", 
                                    use_container_width=True
                                )
                    else:
                        st.warning("No visual data found in response payload.")
                        
                else:
                    st.error(f"Backend Error: {response.status_code} - {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error(f"Connection Error: Unable to communicate with backend engine at: {BACKEND_URL}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Secure Architecture: App relies entirely on isolated system memory strings.")
