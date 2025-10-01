# -*- coding: utf-8 -*-
"""
DIGITAL MATURITY ASSESSMENT - WEB APP
"""

import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import Anthropic AFTER checking API key
api_key = None

# Priority 1: Try Streamlit secrets (for Streamlit Cloud)
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
except:
    pass

# Priority 2: Try environment variable (for local)
if not api_key:
    api_key = os.getenv("ANTHROPIC_API_KEY")

# Check if API key exists
if not api_key or api_key == "your_api_key_here":
    st.error("""
    ⚠️ **API Key chưa được cấu hình!**
    
    **Hướng dẫn:**
    1. Vào Settings (góc dưới phải)
    2. Chọn tab "Secrets"
    3. Thêm dòng: `ANTHROPIC_API_KEY = "your-key-here"`
    4. Click Save
    
    **Lấy API key:** https://console.anthropic.com/settings/keys
    """)
    st.stop()

# Now import and initialize Anthropic
try:
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key)
    
    # Test connection
    st.sidebar.success("✅ API connected")
except Exception as e:
    st.error(f"❌ Không thể kết nối API: {str(e)}")
    st.stop()
# Check if API key exists
if not api_key or api_key == "your_api_key_here":
    st.error("""
    ⚠️ **API Key chưa được cấu hình!**
    
    **Hướng dẫn:**
    1. Vào Settings (góc dưới phải)
    2. Chọn tab "Secrets"
    3. Thêm dòng: `ANTHROPIC_API_KEY = "your-key-here"`
    4. Click Save
    
    **Lấy API key:** https://console.anthropic.com/settings/keys
    """)
    st.stop()

# Now import and initialize Anthropic
try:
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key)
    
    # Test connection
    st.sidebar.success("✅ API connected")
except Exception as e:
    st.error(f"❌ Không thể kết nối API: {str(e)}")
    st.stop()

# Cau hinh trang
st.set_page_config(
    page_title="Digital Maturity Assessment",
    page_icon="📊",
    layout="wide"
)

# CSS tuy chinh
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        background-color: #667eea;
        color: white;
        font-size: 18px;
        padding: 0.5rem 2rem;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #5568d3;
    }
    h1 {
        color: #667eea;
    }
    .score-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>📊 Đánh Giá Mức Độ Chuyển Đổi Số</h1>", unsafe_allow_html=True)
st.markdown("---")

# Gioi thieu
with st.expander("ℹ️ Về công cụ này"):
    st.write("""
    **Công cụ AI-Powered Assessment** giúp bạn:
    - Đánh giá mức độ số hóa của doanh nghiệp
    - So sánh với 50+ công ty cùng ngành tại VN
    - Nhận báo cáo chi tiết ngay lập tức
    - Đề xuất roadmap 12 tháng cụ thể
    
    **Thời gian:** 5 phút | **Chi phí:** Miễn phí
    """)

st.markdown("---")

# FORM ĐÁNH GIÁ
st.markdown("## 📋 Thông Tin Doanh Nghiệp")

col1, col2 = st.columns(2)

with col1:
    company_name = st.text_input(
        "Tên công ty *",
        placeholder="VD: ABC Company"
    )
    
    industry = st.selectbox(
        "Ngành nghề *",
        ["Chọn ngành...", "Retail (Bán lẻ)", "Manufacturing (Sản xuất)", 
         "Services (Dịch vụ)", "Other (Khác)"]
    )

with col2:
    employee_count = st.selectbox(
        "Số lượng nhân viên",
        ["Chọn...", "1-10", "11-50", "51-200", "201-500", "500+"]
    )
    
    revenue = st.selectbox(
        "Doanh thu hàng năm (tỷ VNĐ)",
        ["Chọn...", "<5", "5-20", "20-100", "100-500", ">500"]
    )

st.markdown("---")
st.markdown("## 🔍 Câu Hỏi Đánh Giá")

st.markdown("### 1. Quản lý dữ liệu khách hàng")
q1 = st.radio(
    "Công ty bạn quản lý dữ liệu khách hàng như thế nào?",
    [
        "1 - Excel/giấy tờ, không có hệ thống",
        "2 - Excel có cấu trúc, chia sẻ qua email",
        "3 - Phần mềm đơn giản (Google Sheets, Airtable)",
        "4 - CRM cơ bản (chưa tích hợp)",
        "5 - CRM chuyên nghiệp, tích hợp đầy đủ"
    ],
    key="q1"
)

st.markdown("### 2. Báo cáo doanh số")
q2 = st.radio(
    "Bạn tạo báo cáo doanh số bao lâu một lần?",
    [
        "1 - Không có báo cáo định kỳ",
        "2 - Hàng tháng, làm thủ công",
        "3 - Hàng tuần, làm thủ công",
        "4 - Hàng ngày, tự động một phần",
        "5 - Real-time dashboard, hoàn toàn tự động"
    ],
    key="q2"
)

st.markdown("### 3. Đo lường ROI Marketing")
q3 = st.radio(
    "Bạn có thể đo lường ROI của các chiến dịch marketing không?",
    [
        "1 - Không, không có tracking",
        "2 - Ước lượng sơ bộ",
        "3 - Đo được một phần (VD: chỉ online ads)",
        "4 - Đo được đa số kênh, nhưng không real-time",
        "5 - Đo chính xác mọi kênh, real-time"
    ],
    key="q3"
)

st.markdown("### 4. Thách thức chính")
challenges = st.text_area(
    "3 thách thức lớn nhất về công nghệ/quy trình hiện tại?",
    placeholder="VD: Dữ liệu bị phân mảnh, không có báo cáo tự động...",
    height=100
)

st.markdown("---")
st.markdown("## 📞 Thông Tin Liên Hệ")

col3, col4 = st.columns(2)

with col3:
    contact_name = st.text_input("Họ tên *")

with col4:
    contact_email = st.text_input("Email *")

st.markdown("---")

# NÚT SUBMIT
if st.button("🚀 Tạo Báo Cáo Ngay", use_container_width=True):
    
    # Validation
    if not company_name or not contact_name or not contact_email:
        st.error("⚠️ Vui lòng điền đầy đủ thông tin bắt buộc (*)")
    elif industry == "Chọn ngành...":
        st.error("⚠️ Vui lòng chọn ngành nghề")
    elif "@" not in contact_email:
        st.error("⚠️ Email không hợp lệ")
    else:
        # Tinh diem
        score_q1 = int(q1.split(" -")[0])
        score_q2 = int(q2.split(" -")[0])
        score_q3 = int(q3.split(" -")[0])
        
        score = round((score_q1 + score_q2 + score_q3) / 3, 1)
        
        # Hien thi diem
        st.markdown("---")
        st.markdown(f"""
        <div class="score-box">
            <h2>Điểm Số Hóa Của Bạn</h2>
            <h1 style="font-size: 72px; margin: 20px 0;">{score}/5.0</h1>
            <p style="font-size: 18px;">Đang phân tích chi tiết bằng AI...</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Goi AI
            status_text.text("🤖 Đang kết nối với AI...")
            progress_bar.progress(20)
            
            # Map industry
            industry_map = {
                "Retail (Bán lẻ)": "retail",
                "Manufacturing (Sản xuất)": "manufacturing",
                "Services (Dịch vụ)": "services",
                "Other (Khác)": "other"
            }
            industry_code = industry_map.get(industry, "other")
            
            # Benchmark
            benchmarks = {
                "retail": {"avg": 3.2, "top": 4.1},
                "manufacturing": {"avg": 2.8, "top": 3.9},
                "services": {"avg": 3.5, "top": 4.3},
                "other": {"avg": 3.0, "top": 4.0}
            }
            benchmark = benchmarks[industry_code]
            
            prompt = f"""Bạn là chuyên gia tư vấn chuyển đổi số tại Việt Nam.

THÔNG TIN DOANH NGHIỆP:
- Tên: {company_name}
- Ngành: {industry}
- Nhân viên: {employee_count}
- Doanh thu: {revenue} tỷ VNĐ/năm
- Điểm số hóa: {score}/5.0
- Trung bình ngành: {benchmark['avg']}/5.0
- Top 25% ngành: {benchmark['top']}/5.0

THÁCH THỨC CHÍNH:
{challenges if challenges else 'Chưa cung cấp'}

Hãy viết báo cáo phân tích (300-400 từ) bao gồm:

1. **Tóm tắt** (2-3 câu đánh giá tổng quan)

2. **Top 3 Gaps** (điểm yếu cần khắc phục ngay):
   - Gap 1: [Tên gap] - [Tại sao quan trọng] - [Chi phí/rủi ro nếu không fix]
   - Gap 2: ...
   - Gap 3: ...

3. **Quick Wins** (3 hành động trong 3 tháng):
   - Action 1: [Cụ thể, chi phí thấp, impact cao]
   - Action 2: ...
   - Action 3: ...

4. **Đề xuất công nghệ** (1-2 giải pháp phù hợp):
   - Tool/Platform: [Tên] - [Lý do] - [Chi phí ước tính VN]

5. **Roadmap 12 tháng** (timeline ngắn gọn):
   - Tháng 1-3: ...
   - Tháng 4-6: ...
   - Tháng 7-12: ...

Viết bằng tiếng Việt, phong cách chuyên nghiệp, dễ hiểu, CỤ THỂ với thị trường VN."""

            status_text.text("🧠 AI đang phân tích...")
            progress_bar.progress(40)
            
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            analysis = response.content[0].text
            
            progress_bar.progress(80)
            status_text.text("📝 Đang tạo báo cáo...")
            
            # Luu ket qua vao session state
            st.session_state.report_generated = True
            st.session_state.company_name = company_name
            st.session_state.score = score
            st.session_state.benchmark = benchmark
            st.session_state.analysis = analysis
            st.session_state.contact_email = contact_email
            
            progress_bar.progress(100)
            status_text.text("✅ Hoàn thành!")
            
            # Hien thi ket qua
            st.markdown("---")
            st.markdown("## 📊 Báo Cáo Chi Tiết")
            
            # So sanh
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.metric("Điểm của bạn", f"{score}/5.0")
            
            with col_b:
                delta_avg = round(score - benchmark['avg'], 1)
                st.metric(
                    "So với TB ngành", 
                    f"{benchmark['avg']}/5.0",
                    delta=f"{delta_avg:+.1f}"
                )
            
            with col_c:
                if score >= benchmark['top']:
                    percentile = "Top 25%"
                elif score >= benchmark['avg']:
                    percentile = f"Top {int(50 - ((score - benchmark['avg']) / (benchmark['top'] - benchmark['avg']) * 25))}%"
                else:
                    percentile = f"Bottom {int(50 - (score / benchmark['avg'] * 50))}%"
                st.metric("Vị trí trong ngành", percentile)
            
            st.markdown("---")
            
            # Noi dung phan tich
            st.markdown(analysis)
            
            st.markdown("---")
            
            # Luu file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"assessment_{company_name.replace(' ', '_')}_{timestamp}.txt"
            
            report_content = f"""BÁO CÁO ĐÁNH GIÁ CHUYỂN ĐỔI SỐ
{'='*70}

Công ty: {company_name}
Ngành: {industry}
Điểm: {score}/5.0
Trung bình ngành: {benchmark['avg']}/5.0
Top 25% ngành: {benchmark['top']}/5.0
Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M')}

{'-'*70}

{analysis}

{'-'*70}

Báo cáo được tạo bởi AI-Powered Assessment Tool
Website: yourcompany.com
Email: consulting@yourcompany.com
"""
            
            # Download button
            st.download_button(
                label="📥 Tải Báo Cáo (TXT)",
                data=report_content,
                file_name=filename,
                mime="text/plain"
            )
            
            # Call to action
            st.success("✅ Báo cáo đã được tạo thành công!")
            
            st.info("""
            ### 🎁 Nhận tư vấn miễn phí 30 phút
            
            Đặt lịch để:
            - Thảo luận chi tiết về báo cáo
            - Nhận thêm insights về vendor & giá thực tế VN
            - Điều chỉnh roadmap phù hợp với budget
            
            📧 Email: consulting@yourcompany.com  
            📞 Hotline: 0123 456 789
            """)
            
        except Exception as e:
            st.error(f"❌ Lỗi: {e}")
            st.info("""
            **Kiểm tra:**
            1. API key đã được setup chưa?
            2. Có kết nối internet không?
            3. Tài khoản Anthropic còn credit không?
            """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>© 2025 Your Consulting Company | 
    <a href="mailto:consulting@yourcompany.com">consulting@yourcompany.com</a> | 
    0123 456 789</p>
    <p style="font-size: 12px;">Báo cáo được tạo bởi AI-Powered Assessment Tool</p>
</div>

""", unsafe_allow_html=True)


