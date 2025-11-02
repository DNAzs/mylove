import streamlit as st
import random
import time

# 保持原有的消息和颜色数据
messages = [
    "早安，开启美好一天！",
    "天冷了，多穿衣服",
    "不顺心的话就找我叭",
    "多喝水哦~",
    "要天天开心吖~",
    "保持好心情",
    "照顾好自己",
    "别熬夜",
    "早点休息",
    "今天过的开心嘛",
    "今天也要加油哦！",
    "梦想成真",
    "保持微笑吖",
    "愿你所有烦恼都消失",
    "多吃水果",
    "要按时吃饭",
    "你值得被世界温柔以待",
    "好好爱自己",
    "顺顺利利",
    "愿你笑容常在。"
]

# 转换RGB为CSS颜色格式
warm_colors = [
    (255, 239, 213), (255, 228, 196), (255, 222, 173),
    (255, 182, 193), (255, 204, 153), (255, 250, 205),
    (255, 245, 238), (255, 228, 225), (255, 218, 185),
    (255, 160, 122), (255, 236, 139), (255, 215, 180),
    (255, 223, 211), (255, 240, 245), (255, 250, 240),
    (255, 239, 213), (255, 228, 181), (255, 192, 203),
    (255, 228, 225)
]
css_colors = [f"rgb({r},{g},{b})" for r, g, b in warm_colors]

# 页面配置
st.set_page_config(
    page_title="温馨提示",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS：实现卡片随机定位和样式
st.markdown("""
<style>
    .popup-card {
        position: absolute;
        width: 200px;
        height: 60px;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "微软雅黑";
        font-size: 18px;
        font-weight: bold;
        color: #333;
        z-index: 1;
    }
    .main-content {
        position: relative;
        height: 800px;  /* 限制显示区域高度 */
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# 初始化状态管理
if 'popups' not in st.session_state:
    st.session_state.popups = []
if 'generated' not in st.session_state:
    st.session_state.generated = False

# 控制区域
st.sidebar.header("控制选项")
max_count = st.sidebar.slider("生成数量", 10, 500, 300)
speed = st.sidebar.slider("生成速度(毫秒)", 10, 100, 20)
if st.sidebar.button("生成温馨提示"):
    st.session_state.popups = []  # 清空现有卡片
    st.session_state.generated = True

# 显示区域
st.title("温馨提示墙")
st.markdown('<div class="main-content" id="popup-container"></div>', unsafe_allow_html=True)

# 动态生成卡片
if st.session_state.generated and len(st.session_state.popups) < max_count:
    # 计算需要新增的卡片数量（每次刷新增加1个，模拟定时器效果）
    if len(st.session_state.popups) < max_count:
        idx = len(st.session_state.popups)
        msg = messages[idx % len(messages)]
        color = css_colors[idx % len(css_colors)]
        
        # 随机位置（基于显示区域大小）
        x = random.randint(50, 1100)  # 适配网页宽度
        y = random.randint(50, 700)   # 适配网页高度
        
        st.session_state.popups.append({
            "msg": msg,
            "color": color,
            "x": x,
            "y": y
        })
        
        # 刷新页面以显示新卡片
        time.sleep(speed / 1000)
        st.experimental_rerun()

# 渲染所有卡片
for i, popup in enumerate(st.session_state.popups):
    st.markdown(f"""
    <div class="popup-card" style="background-color: {popup['color']}; left: {popup['x']}px; top: {popup['y']}px;">
        {popup['msg']}
    </div>
    """, unsafe_allow_html=True)