import streamlit as st
import g4f

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="AI Testcase Generator", page_icon="🧪")
st.title("🧪 Ainul AI TestCase Generator")
st.caption("Advanced AI Testing Solution - by Ainul Idham S.T, M.Kom")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Engine Status")
    st.success("Mode: AI Proxy Enabled")
    st.info("M.Kom Approach: Resilience in Technical Deployment.")

# --- INPUT ---
user_story = st.text_area("Masukkan User Story / Requirement:", height=150,
                          placeholder="Contoh: Fitur transfer BI-FAST...")

# --- LOGIKA GENERATE ---
if st.button("🚀 GENERATE DENGAN AI"):
    if not user_story:
        st.warning("Masukkan User Story-nya dulu.")
    else:
        try:
            with st.spinner("AI - idham : sedang memproses requirement..."):
                # Menghubungi AI Gemini via jalur alternatif
                response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4, # Kita bisa pakai GPT-4 atau Gemini di sini
                    messages=[{"role": "user", "content": f"""
                        Bertindaklah sebagai Senior QA Lead. 
                        Buatkan dokumen testing profesional dalam format Markdown untuk: "{user_story}"
                        Isi: Tabel Test Case (ID, Skenario, Langkah, Hasil, Prioritas) dan Script Playwright Typescript.
                        Bahasa: Indonesia.
                        """}],
                )
                
                st.success("✅ AI Berhasil Menghasilkan Test Suite!")
                st.markdown("---")
                st.markdown(response)
                
        except Exception as e:
            st.error(f"Terjadi kendala teknis: {e}")
            st.info("Coba restart aplikasi streamlit kamu.")

st.markdown("---")
st.caption("© 2026 Ainul idham | Built for Excellence")